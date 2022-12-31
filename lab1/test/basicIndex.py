import unittest

import numpy

from lab1.models.indexes.basicIndex import BasicIndex


class BasisIndexTestCase:

    def check_empty_data(self):
        empty_idx = self._idx_maker_class('./dummyFilesEmpty')
        indexes = empty_idx.get_indexes()
        self.assertIsNotNone(indexes)
        self.assertTrue(len(indexes) == 0)

    def test_search(self):
        res_1 = ['test1.txt']
        res_both = ['test1.txt', 'test2.txt']
        res_2 = ['test2.txt']
        self.assertTrue(numpy.array_equal(self._idx_maker.search('word2'), res_1))
        self.assertTrue(numpy.array_equal(self._idx_maker.search('word1'), res_both))
        self.assertTrue(numpy.array_equal(self._idx_maker.search('word4'), res_2))
        self.assertTrue(self._idx_maker.search('word5') is None)

    def check_data(self):
        pass

    def run_tests(self):
        self.check_empty_data()
        self.check_data()
        self.test_search()