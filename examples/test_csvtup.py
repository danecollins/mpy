from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict,Counter
 
from csvtup import read_csv



import unittest
class CSVtests(unittest.TestCase):
    def test_basic_csv(self):
        # Most basic reading of csv file, but with some blank lines in it
        rows = read_csv('./csv/booking_goals.csv',ignore_after_blank=False,dialect='excel')
        assert len(rows) == 95
        row0 = rows[0]
        assert row0.Amount == '1200000'
        assert row0.Final  == '986539'
        assert row0.Goal   == 'AP-JPE-NT'
        assert rows[94].Goal == 'WW-quota'
        assert rows[94].pct_of_goal == '0.902'

    def test_tab_separated(self):
        ## Simplest tab-separated file
        rows = read_csv('./csv/file1.tsv',dialect='excel-tab')
        assert len(rows) == 27
        assert rows[0].custid == '10000'
        assert rows[26].a2013 == '53953.57'

    def test_odd_delimiter(self):
        ## Using odd delimiter and extra header line
        rows = read_csv('./csv/odd_head_and_foot.txt',ignore_after_header=1,dialect='excel',delimiter="|")
        assert len(rows) == 21
        assert rows[0].custid == '1'
        assert rows[1].custname == 'Inside Contactless'
        assert rows[20].city == 'VA'

    def test_excel_from_sfdc(self):
        ## Excel file from SFDC with issues
        rows = read_csv('./csv/excel_from_sfdc.csv',encoding='latin1',dialect='excel')

        assert len(rows) == 18004

    def test_passing_in_names(self):
        names = ['CustID','CY2010','CY2011','CY2012','CY2013']
        rows = read_csv('./csv/file1.tsv',fields=names,dialect='excel-tab')
        assert len(rows) == 27
        assert rows[0].CustID == '10000'
        assert rows[26].CY2013 == '53953.57'

    def test_cdb_account_dump(self):
        rows = read_csv('csv/accts_cdb.txt',ignore_after_header=1,delimiter='|',dialect='excel',encoding='latin1')
        assert len(rows) == 3500
        assert rows[3499].custid == '9999'


unittest.main()
