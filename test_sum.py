"""
Test for primes_sum function
"""
import unittest
from main import primes_sum

class TestSum(unittest.TestCase):

    def test_sum(self):
        """This is a unit test for the prime sum function"""
        result = primes_sum([2,4,7])

        self.assertEqual(result, 13)


if __name__ == '__main__':
    unittest.main()

