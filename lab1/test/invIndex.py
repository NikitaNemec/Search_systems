import unittest

from lab1.models.indexes.invIndex.invIndex import InvertedIndex
from lab1.test.basicIndex import BasisIndexTestCase


class InvertedIndexTestCase(unittest.TestCase, BasicIndexTestCase):
    _idx_maker = InvertedIndex('./dummyFiles')
    _idx_maker_class = InvertedIndex

    def check_data(self):
        indexes = self._idx_maker.get_indexes()

        # check if parsed all words
        self.assertTrue(len(indexes.keys()) == 4)

        # check parsed files
        self.assertTrue('word1' in indexes.keys())
        self.assertTrue('word2' in indexes.keys())
        self.assertTrue('word3' in indexes.keys())
        self.assertTrue('word4' in indexes.keys())

        # check if all files bind to word
        first_word_subset = indexes['word1']
        self.assertTrue(len(first_word_subset) == 2)
        self.assertTrue(first_word_subset[0] == 'test1.txt')
        self.assertTrue(first_word_subset[1] == 'test2.txt')
