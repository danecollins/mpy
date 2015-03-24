import re


def clean_name(name):
    name = name.title()
    name = name.replace('  ', ' ')
    x = name
    name = re.sub(' *\(.*master.*\) *', '', name)
    name = re.sub(' *\(.*eluxe.*\) *', '', name)
    name = re.sub(' *\(.*ive.*\) *', '', name)
    name = re.sub(' *\(.*oundtrack.*\) *', '', name)
    name = re.sub(' *\(.*edition.*\) *', '', name)
    name = re.sub(' *\(.*onus.*\) *', '', name)
    name = re.sub(' *\[.*\] *', '', name)
    if x != name:
        print('cleaned {} == {}'.format(x, name))
    return name



def fuzzify(name):
    x = name
    name = name.lower()
    name = re.sub(' *\(.*\) *', '', name)  # remove stuff in parens
    name = re.sub('[] -_"\'.]', '', name)
    return x

names = set()
fuzzies = set()

with open('album.txt') as fp:
    for line in fp.readlines():
        line = line.strip()
        name = clean_name(line)
        if name in names:
            #print('Duplicate found by cleaning: {} == {}'.format(line, name))
	    pass
        else:
            names.add(name)
            fuzzy = fuzzify(name)
            if fuzzy in fuzzies:
                print('Duplicate fuzzy name: {} == {}'.format(line, fuzzy))
            else:
                fuzzies.add(fuzzy)

#for x in sorted(fuzzies):
#    print(x)
