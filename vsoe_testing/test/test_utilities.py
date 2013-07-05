import unittest
from utilities import striplf

class TestUtilityFunctions(unittest.TestCase):

	def test_striplf_value(self):
		self.assertEqual(striplf('fubar\n'),'fubar')
		self.assertEqual(striplf('fubar'),'fubar')
		
	def test_striplf_type(self):
		try:
			self.failUnlessRaises(AttributeError, striplf(3))
		except AttributeError:
			### need to catch Attrib Error or tests fail
			1
		
if __name__ == '__main__':
	unittest.main()
	