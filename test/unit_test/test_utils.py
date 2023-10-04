import sys

sys.path.insert(0, '../../src/')  # noqa

import my_utils
import unittest
import random
import os
import statistics


class TestMathLib(unittest.TestCase):
    def test_mean_random(self):
        A = [random.randint(-1000, 1000) for i in range(random.randint(0,100))]
        avg = my_utils.mean(A)
        self.assertEqual(statistics.mean(A), avg)

    def test_mean_nonInt(self):
        A = [random.uniform(-1000, 1000) for i in range(random.randint(0,100))]
        with self.assertRaises(ValueError):
            avg = my_utils.mean(A)
    
    def test_mean_emptyList(self):
        A = []
        with self.assertRaises(ValueError):
            avg = my_utils.mean(A)

    def test_median_random(self):
        A = [random.randint(-1000, 1000) for i in range(random.randint(0,100))]
        med = my_utils.median(A)
        self.assertEqual(statistics.median(A), med)
    
    def test_median_nonInt(self):
        A = [random.uniform(-1000, 1000) for i in range(random.randint(0,100))]
        with self.assertRaises(ValueError):
            avg = my_utils.median(A)
    
    def test_mmedian_emptyList(self):
        A = []
        with self.assertRaises(ValueError):
            avg = my_utils.median(A)
    
    def test_stdv_random(self):
        A = [random.randint(-1000, 1000) for i in range(random.randint(0,100))]
        stdv = my_utils.stdv(A)
        self.assertAlmostEqual(statistics.stdev(A), stdv)

    def test_stdv_nonInt(self):
        A = [random.uniform(-1000, 1000) for i in range(random.randint(0,100))]
        with self.assertRaises(ValueError):
            avg = my_utils.median(A)
    
    def test_stdv_emptyList(self):
        A = []
        with self.assertRaises(ValueError):
            avg = my_utils.stdv(A)
    

def main():
    unittest.main()

if __name__ == '__main__':
    main()