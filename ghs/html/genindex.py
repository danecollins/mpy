from abi import urltools


def parse_command_file(fp):
	data = {
		'name' : "missing",
		'title' : "missing",
		'desc' : "missing",
		'web' : "missing",
		'wiki' : "missing"
	}
	data['args'] = []
	for line in fp.readlines():
		if (line.startswith('#DOC')):
			line = line[5:] # remove #DOC
			line = line.rstrip("\r\n")
			(field,value) = line.split(": ")
			if (field == 'args'):
				(argname,argval) = value.split(" - ")
				data['args'].append( (argname, argval) )
			else:
				data[field] = value
	return(data)


def output_command_string(data):
	str1 = """
<h3>{title}</h3>
<div class="row"> <div class="col-lg-1"></div><div class="col-lg-9">
<p>{desc}</p>
<table class="table table-bordered">
<tr><td colspan=2>The following arguments are supported:
<dl class="dl-horizontal">
"""
	str2 = ""
	for argument in data['args']:
		str2 = str2 + """
	<dt>%s</dt>
	<dd>%s</dd>
""" % argument

	str2 = str2 + """
</dl>
</tr>
</td>
"""
	str3 = """
<tr class="success">
	<td><strong>Web syntax</strong></td>
	<td>{web}</td>
</tr>
<tr class="warning">
	<td><strong>Confluence syntax</strong></td>
	<td>{wiki}</td>
</tr>
</table>
</div></div></div>
"""
	return( str1.format(**data) + str2 + str3.format(**data))


with open('index.html','w') as fout:
	with open('index.stub.html') as fp:
		fout.write(fp.read())

	for cmd in urltools.get_command_list():
		filename = '../abi/' + cmd + '.py'
		print("Working on file: " + filename)
		with open(filename) as fp:
			data = parse_command_file(fp)

		
		fout.write(output_command_string(data))

	fout.write('\n</html>\n')


