from models.helpers.str_utils import clear_word
from models.indexes.fwdIndex.fwdIndex import ForwardIndex
from models.indexes.invIndex.invIndex import InvertedIndex

indexer = ForwardIndex()

print(indexer.search('Garibaldi'))

