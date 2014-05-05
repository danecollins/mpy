import sys
## functions to process html stub files

## substitute args in page stub and return
def gen_html_page(file, args):
	fp = open(file)
	output = fp.read()
	fp.close()
	for key in args.keys():
		pattern = '{' + key + '}'
		value = args[key]
		output = output.replace(pattern,value)

	return(output)


