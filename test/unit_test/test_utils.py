import sys

sys.path.insert(0, '../../src/')  # noqa

import my_utils
import unittest
import random
import os
import statistics


class TestMathLib(unittest.TestCase):
    def setUp(self):
        self.data_file = os.path.join(os.path.dirname(__file__),
                                      '..',
                                      'func',
                                      'data',
                                      'functional_test_data.csv')
        self.outDir = os.path.join(os.path.dirname(__file__),
                                   'output')
        self.test_file = os.path.join(os.path.dirname(__file__),
                                      'output',
                                      'test.png')

    def test_mean_random(self):
        A = [random.randint(-1000, 1000) for i
             in range(random.randint(0, 100))]
        avg = my_utils.mean(A)
        self.assertEqual(statistics.mean(A), avg)

    def test_mean_nonInt(self):
        A = [random.uniform(-1000, 1000) for i
             in range(random.randint(0, 100))]
        with self.assertRaises(ValueError):
            avg = my_utils.mean(A)

    def test_mean_emptyList(self):
        A = []
        with self.assertRaises(ValueError):
            avg = my_utils.mean(A)

    def test_median_random(self):
        A = [random.randint(-1000, 1000) for i
             in range(random.randint(0, 100))]
        med = my_utils.median(A)
        self.assertEqual(statistics.median(A), med)

    def test_median_nonInt(self):
        A = [random.uniform(-1000, 1000) for i
             in range(random.randint(0, 100))]
        with self.assertRaises(ValueError):
            avg = my_utils.median(A)

    def test_mmedian_emptyList(self):
        A = []
        with self.assertRaises(ValueError):
            avg = my_utils.median(A)

    def test_stdv_random(self):
        A = [random.randint(-1000, 1000) for i
             in range(random.randint(0, 100))]
        stdv = my_utils.stdv(A)
        self.assertAlmostEqual(statistics.stdev(A), stdv)

    def test_stdv_nonInt(self):
        A = [random.uniform(-1000, 1000) for i
             in range(random.randint(0, 100))]
        with self.assertRaises(ValueError):
            avg = my_utils.median(A)

    def test_stdv_emptyList(self):
        A = []
        with self.assertRaises(ValueError):
            avg = my_utils.stdv(A)

    def test_plot_boxplot_folder_gen(self):
        self.assertFalse(os.path.isdir(self.outDir),
                         "The directory already exists")
        result = my_utils.get_column(self.data_file, 0,
                                     "China",
                                     result_column=3)
        my_utils.plot_boxplot(result, "test", 'test')

        self.assertTrue(os.path.isdir(self.outDir))

    def test_plot_boxplot_file_gen(self):
        self.assertFalse(os.path.isdir(self.test_file),
                         'This file already exists')

        result = my_utils.get_column(self.data_file, 0,
                                     "China",
                                     result_column=3)

        my_utils.plot_boxplot(result, "test", "test")

        self.assertTrue(os.path.exists(self.test_file),
                        "The file was not created")

    def test_get_data_columns(self):
        columns = my_utils.get_data_columns(self.data_file)
        expected = ['\ufeffArea', 'Year', 'Savanna fires', 'Forest fires',
                    'Crop Residues', 'Rice Cultivation',
                    'Drained organic soils (CO2)', 'Pesticides Manufacturing',
                    'Food Transport', 'Forestland',
                    'Net Forest conversion', 'Food Household Consumption',
                    'Food Retail', 'On-farm Electricity Use', 'Food Packaging',
                    'Agrifood Systems Waste Disposal', 'Food Processing',
                    'Fertilizers Manufacturing', 'IPPU',
                    'Manure applied to Soils', 'Manure left on Pasture',
                    'Manure Management', 'Fires in organic soils',
                    'Fires in humid tropical forests',
                    'On-farm energy use', 'Rural population',
                    'Urban population',
                    'Total Population - Male', 'Total Population - Female',
                    'total_emission', 'Average Temperature ¬∞C']
        self.assertEqual(expected, columns)

    def tearDown(self):
        if os.path.isdir(self.outDir):
            try:
                os.remove(self.test_file)
                os.rmdir((self.outDir))
            except OSError:
                pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
