import utilities
import sys

# define departments
SL = '4079'
COGS = '1090'
MK = '6079'
RD = '2443'
GA = '9095'
BS = '0'

# map of all accounts by departments
account_balance = {}
account_desc = {}

def print_output():

	fo = open('income_statement.csv','w')
	print "REVENUE"
	print >> fo, "REVENUE"
	total = 0
	dept_balances = account_balance[BS]
	amount = round(-1*dept_balances['40010'],2) # round to 2 places
	total = total + amount
	amount = '{:,}'.format(amount).rjust(14) # format to add commas and right justify
	print "     40010\t",amount,"\tRevenue"
	print >> fo, ',40010,"%s",Revenue' % (amount)
	
	
	amount = round(-1*dept_balances['64010'],2) # round to 2 places
	total = total + amount
	amount = '{:,}'.format(amount).rjust(14) # format to add commas and right justify
	print >> fo, ',64010,"%s",Reseller commissions' % (amount)
	print "     64010\t",amount,"\tReseller commissions"
	

	
	print "   Total = ", '{:,}'.format(total),"\n"
	print >> fo, ',Total,"%s"\n' % ('{:,}'.format(total))
	
	print "EXPENSES"
	print >> fo, 'EXPENSES'
	sections = ( ('General and Administrative',GA),
	             ('Research and Development',RD),
				 ('Sales and Marketing',SL) )
	
	for (title,dept) in sections:
		print "  ",title
		print >> fo, ',',title
		total = 0
		dept_balances = account_balance[dept]
		for key in sorted(dept_balances.keys()):
			amount = round(dept_balances[key],2) # round to 2 places
			total = total + amount
			amount = '{:,}'.format(amount).rjust(14) # format to add commas and right justify
			print "     ",key,"\t",amount,"\t",account_desc[key].rstrip("\n")
			print >> fo, ',%s,"%s",%s' % (key,amount,account_desc[key].rstrip("\n"))

		print "   Total = ", '{:,}'.format(total),"\n"
		print >> fo, ',Total,"%s"\n' % ('{:,}'.format(total))

	print
	fo.close()


def process_file(filename,scale):
	print "processing file", filename
	file = open(filename)

	for line in file.readlines():

		(d1,d2,dept,acct,d3,d4,d5,amt1,amt2,desc) = line.split(',')

		if (amt2 <> ""):
			amount = float(amt2) * -1
		else:
			amount = float(amt1)
			
		if (desc.startswith('NI Acquisition')): 
			print "NI Acq - excluding: ",amount
			continue

		#print "1=",amt1,"    2=",amt2,"      end=",amount

		# merge sales and marketing
		if (dept == MK) : dept = SL
		if (dept == '0000') : dept = BS

		if (dept in account_balance):
			dept_balances = account_balance[dept]
		else:
			print "adding department", dept
			dept_balances = {}

		# multiply amount by scale to take into account for initial balances
		dept_balances[acct] = dept_balances.get(acct,0) + (amount*scale)

		# is this necessary? it is for initial creation
		account_balance[dept] = dept_balances
		account_desc[acct] = desc

	file.close()





# determine number of files to read
# if two, the second one is initial balances
print sys.argv

if len(sys.argv) == 3:
	starting_balance_file = sys.argv[2]
	starting_balance = True
	input_file = sys.argv[1]
else:
	starting_balance = False
	input_file = sys.argv[1]

if (starting_balance):
	print "will process",input_file,"using starting balances in",starting_balance_file
else:
	print "will process",input_file

if (starting_balance):
	process_file(starting_balance_file,-1)

process_file(input_file,1)
print '============================================================'
print_output()