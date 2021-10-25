import unittest
import Prgram
class TestNum(unittest.TestCase):
    def test_isOddEven(self):
        self.assertAlmostEqual(Prgram.oddEven(221),'odd')
        self.assertAlmostEqual(Prgram.oddEven(2),'even')
        self.assertAlmostEqual(Prgram.oddEven(11),'odd')

if __name__=='__main__':
    unittest.main()