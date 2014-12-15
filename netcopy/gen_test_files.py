from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict,Counter

import os

for i in range(5):
	with open('test_file{}.bin'.format(i),'wb') as fp:
		fp.write(bytearray(os.urandom(1000000)))

