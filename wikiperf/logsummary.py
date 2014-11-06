
paths = {}
with open('atlassian-confluence.log') as fp:
	for line in fp.readlines():
		if line.startswith('2014'):
			line.rstrip()
			parts = line.split()
			try:
				time = parts[6][1:len(parts[6])-3]
			except:
				continue

			#if int(time)>5000:
			#	print(line)
			if 'batch.js' in line:
				path = parts[8]
				if path in paths:
					paths[path].append(int(time))
				else:
					paths[path] = [int(time) ]

for key in paths:
	times = paths[key]
	mintime = min(times)
	maxtime = max(times)
	if (maxtime>3000):
		print(key)
		print("   min:   ", mintime)
		print("   max:   ", maxtime)
		print("   times: ",paths[key])
