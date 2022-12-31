from lab1.models.helpthings.str_utils import clear_word
from lab1.models.indexes.basicIndex import BasisIndex


class InvertedIndex(BasisIndex):
    def index_files(self, files_data):
        for file in files_data:
            name, text = file
            for word in list(map(clear_word, text.split(' '))):
                if word in self.indexes:
                    self.indexes[word].append(name)
                else:
                    self.indexes[word] = [name]

    def search(self, query):
        if not self.indexes:
            raise ValueError("No available indexes")
        if query.lower() not in self.indexes:
            return None
        return self.indexes[query.lower()]