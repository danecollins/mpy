from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict
import pdb
import re

prod_pattern = re.compile('[A-Z][A-Z][A-Z]_\d\d\d')
feat_pattern = re.compile('LicFeat_[^\s,]*')

bits = set()
products = set()
matrix = defaultdict(list)

with open('LicensePackages.h') as fp:
    for line in fp.readlines():
        x = prod_pattern.search(line)
        if x:
            product = x.group()
            products.add(product)

        x = feat_pattern.findall(line)
        if x:
            for fb in x:
                fb = fb[fb.find('_')+1:]
                matrix[product].append(fb)

# we need to add in the bundles that are generated in licensing.

# MWO_246B
tmp_bits = list(matrix['MWO_226'])
tmp_bits.append('.XEM_001')
tmp_bits.append('.XEM_100')
matrix['MWO_246B'] = tmp_bits

# MWO_146B
tmp_bits = list(matrix['MWO_126'])
tmp_bits.append('.XEM_001')
tmp_bits.append('.XEM_100')
matrix['MWO_146B'] = tmp_bits

# MWO_186B
tmp_bits = list(matrix['MWO_146B'])
tmp_bits.append('.ANA_001')
tmp_bits.append('.ANA_100')
matrix['MWO_186B'] = tmp_bits

# matrix['.EM ANA_001'] = matrix.pop('ANA_001')
# matrix['.EM ANA_003'] = matrix.pop('ANA_003')
# matrix['.EM ANA_100'] = matrix.pop('ANA_100')
# matrix['.EM ANA_300'] = matrix.pop('ANA_300')
# matrix['.EM XEM_001'] = matrix.pop('XEM_001')
# matrix['.EM XEM_100'] = matrix.pop('XEM_100')
# matrix['.EM ACE_100'] = matrix.pop('ACE_100')

# collect up all the products and feature bits
products = sorted(matrix.keys())
for v in matrix.values():
    for x in v:
        bits.add(x)
bits = sorted(bits)

print('Product,', ",".join(products))

for bit in sorted(bits):
    # if bit == 'ACE':
    #     pdb.set_trace()

    print(bit, ',', end='')
    for product in products:
        if bit in matrix[product]:
            print('X,', end='')
        else:
            print(' ,', end='')
    print()
