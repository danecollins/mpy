
from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict
from collections import Counter

paths = defaultdict(list)
c = Counter()

def ip2loc(ip):
	if   ip.startswith('10.16.48'):
		return('ES1 ')
	elif ip.startswith('10.16.49'):
		return('ES2 ')
	elif ip.startswith('10.21.0'):
		return('CO1 ')
	elif ip.startswith('10.21.1'):
		return('CO2 ')
	elif ip.startswith('10.22.64'):
		return('WI  ')
	elif ip.startswith('10.16.40'):
		return('CA  ')
	elif ip.startswith('10.100.8'):
		return('UK  ')
	elif ip.startswith('10.83.9'):
		return('FI  ')
	else:
		return('HOME')

with open('atlassian-confluence-access.log','U') as fp:
	for line in fp.readlines():
		c['lines'] += 1

		if line.startswith('2014') and line.find('doFilter') <> -1:
			line = line.rstrip()
			#udata=line.decode("utf-8")
			#line=udata.encode("ascii","ignore")

			parts = line.split(' ')
			if len(parts) == 12:
				if '-' in parts[9]:
					(vm,used) = parts[9].split('-')
				elif '+' in parts[9]:
					(vm,used) = parts[9].split('+')
					used = '-' + used
				else:
					print('ERROR in format of VM on {}'.format(parts[9]))
					print(line)
					vm=0
					used=0

				user = parts[6]
				if user == 'dcollins' or user == 'mreed':
					user += ' adm'

				try:
					d = { 'date' : parts[0],
						  'time' : parts[1][0:-4],
						  'user' : user,
					      'VMava' : int(vm),
					      'VMused' : int(used),
					      'time' : int(parts[10]),
					      'office' : ip2loc(parts[11]),
					      'IP' : parts[11] }
					c['loglines'] +=1
					paths[parts[8][24:]].append(d)
				except Exception as inst:
					print(inst)
					#print('Error on line {}'.format(c['lines']))
					print(line)
					exit(1)
			else:
				pass
				print('skipping:',line)


print("{} lines in log file".format(c['lines']))
print("{} access log lines".format(c['loglines']))
for (p,v) in paths.items():
	### we only want to print things out if one access was > 2s
	if [x['time'] for x in v if x['time']>2000]:
		if len(v)>2:
			print(p)
			for x in sorted(v, key=lambda x: x['time'], reverse=True):
				print('     %5d %s %-9s - %s' % (x['time'], x['office'], x['user'],x['IP'] ))



