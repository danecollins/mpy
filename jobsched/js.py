from __future__ import print_function
from __future__ import unicode_literals
import codecs
import re
import time
from collections import defaultdict

filename = 'AWR_JobScheduler_x64_log.txt'
#filename = 'AWR_JobScheduler_x64_log_2014-10-22T15_32_23.0976.txt'


class Jobs:
	__JOBLIST__ = []

	def add(self,job):
		self.__JOBLIST__.append(job)

	def get_list(self):
		return(self.__JOBLIST__)

	def find_by_number(self,n):
		jobs_matching_number = [x for x in self.__JOBLIST__ if x.job['number'] == n]
		if len(jobs_matching_number)==0:
			print('Could not find job with number {}'.format(n))
			print(l)
		elif len(jobs_matching_number)>1:
			print('jobs_matching_number {} jobs with number {}'.format(len(jobs_matching_number),n))
			assert len(jobs_matching_number) < 2
		else:
			return(jobs_matching_number[0])

	def number_of_jobs(self):
		return( len(self.__JOBLIST__))

	def durations(self):
		min = 10000
		max = 0
		mean = 0
		count = 0
		for j in self.__JOBLIST__:
			d = j.job['duration']
			if type(d) == float:
				if d < min : min=d
				if d > max : max=d
				count += 1
				mean += d

		mean = mean / count
		return( {'min':round(min,1), 'max':round(max,1), 'mean':round(mean,1),'count':count})



class Job:
	__JOB_COUNTER__=0
	def __init__(self):
		self.job = defaultdict(str)

	@staticmethod
	def parse_job_message(self,str):
		str = str.rstrip()
		(tm, rest) = str.split(' - ',1)
		(time_stamp,fractseconds) = tm.split('.')
		msgtm = time.strptime(time_stamp, "%Y-%m-%dT%H:%M:%S")
		float_time = time.mktime(msgtm)  
		float_time += float(fractseconds)/10000
		(num,cmd) = rest.split(': ',1)
		job_number = num[4:]
		return(float_time,job_number,cmd)

	def submitted(self,message):
		# 2014-11-05T12:45:43.0188 - Job 1: Submitted. Name="mpiexec:3.0", User="dhoekstr", Priority=1
		(message_time,job_number,command) = Job.parse_job_message(self,message)
		command = command[len('submitted. '):]
		self.job['id'] = 'JOB' + str(Job.__JOB_COUNTER__)
		Job.__JOB_COUNTER__ += 1
		self.job['submitted'] = message_time
		self.job['number'] = job_number

		## submitted command contains pairs of name=value keyword pairs
		for keyword_pair in [f.strip() for f in command.split(',')]:
			(name,value) = keyword_pair.split('=')
			self.job['S_'+name] = value.rstrip('"').lstrip('"')

	def creating(self,message):
		# 2014-11-05T12:46:42.0140 - Job 1: Creating Process C:\Program Files\AWR\V11\mpiexec.exe  
		# -np 8 -localonly "C:\Program Files\AWR\V11\grsim.exe" "C:\ProgramData\AWR\Design Environment\
		# 11.
		(message_time,job_number,command) = Job.parse_job_message(self,message)
		self.job['start'] = message_time
		if self.job['submitted'] == '':
			## we the start time got lost in a server restart
			self.job['queued'] = 'NA'
		else:
			self.job['queued'] = self.job['start'] - self.job['submitted']

	def releasing(self,message):
		# 2014-11-05T13:56:43.0531 - Job 1: releasing 8 processors (processor reservations available 
		# before:0, after:8)
		(message_time,job_number,command) = Job.parse_job_message(self,message)
		self.job['stop'] = message_time
		if self.job['start'] == '':
			## we the start time got lost in a server restart
			self.job['duration'] = 'NA'
		else:
			self.job['duration'] = self.job['stop'] - self.job['start']

	def request_info(self,message):
		#014-10-21T12:37:31.0010 - Job 1: MaxProcessors=8, MinProcessors=1, 
		#ThreadsPerProcessor=1, PreferredPerf="low", PreferredMemCap="low".
		(message_time,job_number,command) = Job.parse_job_message(self,message)
		for keyword_pair in [f.strip() for f in command.split(',')]:
			(name,value) = keyword_pair.split('=')

			self.job['R_'+name] = value.rstrip('.').rstrip('"').lstrip('"')

	def reserving(self,message):
		#2014-10-21T12:37:31.0665 - Job 1: reserving 8 processors (0 processor 
		#reservations remaining)
		(message_time,job_number,command) = Job.parse_job_message(self,message)
		num_proc = command[10:command.find(' processors')]
		self.job['processors'] = int(num_proc)


	def exit_status(self,message):
		#2014-10-21T12:37:59.0573 - Job 1: (AXIEM:1.0) Ended. Exit status: 0
		(message_time,job_number,command) = Job.parse_job_message(self,message)
		self.job['exit'] = command.split(': ')[1]

	def job2xml(self):
		start = self.job['start']
		s  = '  <Jobs>\n'
		s += '  <Job>\n'
		s += '    <id>{}</id>\n'.format(self.job['id'])
		if start <> '':
			s_time = time.localtime(start)
			value = time.strftime("%d %b %Y %H:%M:%S",s_time)
		else:
			value = 'NA'
		s += '    <StartTime>{}</StartTime>\n'.format(value)
		s += '    <Duration>{}</Duration>\n'.format(self.job['duration'])
		s += '    <User_Name>{}</User_Name>\n'.format(self.job['S_User'])
		s += '    <Simulator>{}</Simulator>\n'.format(self.job['S_Name'])
		s += '    <Priority>{}</Priority>\n'.format(self.job['S_Priority'])
		s += '    <MinProcessors>{}</MinProcessors>\n'.format(self.job['R_MinProcessors'])
		s += '    <ThreadsPerProc>{}</ThreadsPerProc>\n'.format(self.job['R_ThreadsPerProcessor'])
		s += '    <MaxProcessors>{}</MaxProcessors>\n'.format(self.job['R_MaxProcessors'])
		s += '    <QueueTime>{}</QueueTime>\n'.format(self.job['queued'])
		s += '    <PrefPerf>{}</PrefPerf>\n'.format(self.job['R_PreferredPerf'])
		s += '    <ExitStatus>{}</ExitStatus>\n'.format(self.job['exit'])
		s += '  </Job>\n</Jobs>\n'
		return(s)

	def job2json(self):
		print(self.job)


	def __str__(self):
		return(self.job['id'])

	def __repr__(self):
		return('Job({})'.format(self.job))

	@classmethod
	def restart_scheduler(self,joblist):
		# when the scheduler is restarted it will start reusing job numbers so we need to kill
		# the number on all the active jobs
		for x in joblist.get_list():
			x.job['number']=0


desired = [ 'Remote Queue',
            'Processing Command Line',
            'started'
            'Submitted'
          ]


with codecs.open(filename,encoding='utf-8') as fp:

	jobre = re.compile('- Job \d\d*:')
	joblist = Jobs()

	for line in fp.readlines():
		line = line.rstrip()

		if line.find('Submitted.') <> -1:
			j = Job()
			j.submitted(line)
			joblist.add(j)
		elif line.find('Creating Process') <> -1:
			job_number = jobre.search(line).group()[6:-1] # removes the -Job and :
			j = joblist.find_by_number(job_number)
			j.creating(line)
		elif line.find('releasing') <> -1:
			job_number = jobre.search(line).group()[6:-1] # removes the -Job and :
			j = joblist.find_by_number(job_number)
			j.releasing(line)
		elif line.find('Processing Command Line')<>-1:
			Job.restart_scheduler(joblist)
		elif line.find('MaxProcessors')<>-1:
			job_number = jobre.search(line).group()[6:-1] # removes the -Job and :
			j = joblist.find_by_number(job_number)
			j.request_info(line)
		elif line.find('Exit status')<>-1:
			job_number = jobre.search(line).group()[6:-1] # removes the -Job and :
			j = joblist.find_by_number(job_number)
			j.exit_status(line)

	Job.restart_scheduler(joblist)

print( 'Number of jobs = {}'.format(joblist.number_of_jobs()))
print( 'Job duration statistics = {}'.format(joblist.durations()))
