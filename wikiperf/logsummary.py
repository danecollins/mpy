
from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict
from collections import Counter

paths = defaultdict(list)
c = Counter()

def ip2loc(ip):
	if (ip.startswith('10.16.48') or ip.startswith('10.16.49')):
		return('ES')
	elif ip.startswith('10.21.0'):
		return('CO')
	elif ip.startswith('10.22.64'):
		return('WI')
	elif ip.startswith('10.16.40'):
		return('CA')
	else:
		return('HO')

with open('atlassian-confluence.log','U') as fp:
	for line in fp.readlines():
		c['lines'] += 1

		if line.startswith('2014') and line.find('doFilter') <> -1:
			line = line.rstrip()

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

				try:
					d = { 'date' : parts[0],
						  'time' : parts[1][0:-4],
						  'user' : parts[6],
					      'VMava' : int(vm),
					      'VMused' : int(used),
					      'time' : int(parts[10]),
					      'office' : ip2loc(parts[11]),
					      'IP' : parts[11] }
					c['loglines'] +=1
					paths[parts[8]].append(d)
				except:
					print('Error on line {}'.format(c['lines']))
					print(line)
			else:
				pass
				#print('skipping:',line)


print("{} lines in log file".format(c['lines']))
print("{} access log lines".format(c['loglines']))
for (p,v) in paths.items():
	if len(v)>2:
		print(p)
		for x in v:
			print('     %5d %s %s - %s' % (x['time'], x['office'], x['user'],x['IP'] ))



