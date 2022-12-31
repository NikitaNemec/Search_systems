import unittest

from lab1.models.indexes.fwdIndex.fwdIndex import ForwardIndex
from lab1.test.basicIndex import BasisIndexTestCase


class ForwardIndexTestCase(unittest.TestCase, BasicIndexTestCase):
    _idx_maker = ForwardIndex('./dummyFiles')
    _idx_maker_class = ForwardIndex

    def check_data(self):
        indexes = self._idx_maker.get_indexes()

        # check if parsed all files
        self.assertTrue(len(indexes.keys()) == 2)

        # check parsed files
        self.assertTrue('test1.txt' in indexes.keys())
        self.assertTrue('test2.txt' in indexes.keys())

        # check if parsed all words
        first_file_subset = list(indexes['test1.txt'])
        self.assertTrue(len(first_file_subset) == 3)
        self.assertTrue('word1' in first_file_subset)
        self.assertTrue('word2' in first_file_subset)
        self.assertTrue('word3' in first_file_subset)

