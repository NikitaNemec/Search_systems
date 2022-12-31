from lab1.models.helpers.file_utils import load_files_data


class BasisIndex:
    def __init__(self, path=None):
        self.indexes = {}
        files_data = load_files_data() if path is None else load_files_data(path)
        self.index_files(files_data)

    # virtual
    def search(self, query):
        pass

    def get_indexes(self):
        if self.indexes is None:
            raise ValueError("No available indexes")
        return self.indexes

    # virtual
    def index_files(self, files_data):
        pass
