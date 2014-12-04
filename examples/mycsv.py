from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict,Counter
from collections import namedtuple
import codecs
import csv

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

## Notes:
##   - blank lines are always ignored
##   - if ignore_after_blanks is true, reading stops at first blank line
##   - limitation: currently column names must be valid identifiers (can't be numbers)
##   - spaces in header names will be replaces with _
##
##
def read_csv(filename,encoding='utf-8',\
             ignore_after_header=0,ignore_after_blank=True,**kwargs):

    with codecs.open(filename,'r',encoding=encoding) as fp:
        reader = unicode_csv_reader(fp, **kwargs)
        fields = next(reader)
        fields = [x.replace(' ','_') for x in fields]
        number_of_fields = len(fields)
        for i in range(ignore_after_header):
            next(reader)
        CSVF = namedtuple('CSVF',fields)
        rows = list()

        for x in reader:
            if ignore_after_blank and len(x)==0: break
            if len(x) > 0:
                rows.append(CSVF._make(x))

    return(rows)


if __name__ == '__main__':

    import unittest
    class TestParserFunctions(unittest.TestCase):
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
            rows = read_csv('./csv/odd_head_and_foot.txt',ignore_after_header=1,dialect='excel',delimiter=b"|")
            assert len(rows) == 21
            assert rows[0].custid == '1'
            assert rows[1].custname == 'Inside Contactless'
            assert rows[20].city == 'VA'

        def test_excel_from_sfdc(self):
            ## Excel file from SFDC with issues
            rows = read_csv('./csv/excel_from_sfdc.csv',encoding='latin1',dialect='excel')

            assert len(rows) == 18004

    unittest.main()


