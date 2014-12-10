from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict,Counter

import publish
import unittest
import os


class TestPublish(unittest.TestCase):
    def test_get_file_list1(self):
        files = publish.get_file_list('list1.txt')
        assert files[0].frompath == 'publish.txt'
        print(files[0].topath)
        assert files[0].topath.startswith('\\users\\dane\\ignore_path_check')

    def test_get_file_list2(self):
        files = publish.get_file_list('list2.txt')
        assert files[0].frompath == 'publish.txt'
        assert files[0].topath.startswith('\\users\\dane')

    def test_get_file_list3(self):
        files = publish.get_file_list('list3.txt')
        assert files[0].frompath == 'publish.txt'
        assert files[0].topath.startswith('\\users\\dcollins\\ignore_path_check')

    def test_get_file_list4(self):
        files = publish.get_file_list('list4.txt')
        assert files[0].frompath == 'publish.txt'
        assert files[0].tofile.startswith('\\users\\dane\\ignore_path_check\\foo.txt')

unittest.main()