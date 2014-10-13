## python 3.X

in_name = "cm_analysis.md"

fin = open(in_name)
fout = open(in_name+".wiki","w")

line = fin.readline()

while(line):
    lastline = line
    line = fin.readline()
    if line.startswith('-----'):
        ### lastline is a header
        print('h1. ' + lastline, file=fout)
        line = fin.readline()
        continue
    
    if line.startswith('!'):
        ## plot inserted
        name = line[line.rfind('/'):]
        name = name[1:name.rfind('.png')+4]
        print('!'+name+'!', file=fout)
        continue
        
    fout.write(line)
        
fin.close()
fout.close()
    
    