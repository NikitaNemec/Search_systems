from os import listdir
from os.path import isfile, join

default_path = "datatext"


def get_datatext_names(path=default_path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def get_datatext_data(datatext_names, path=default_path):
    data_list = []
    for data in datatext_names:
        data_list.append(read_datatext_datatext(path + "\\" + data))
    return data_list


def load_datatext_data(path=default_path):
    datatext_names = get_datatext_names(path)
    return list(zip(datatext_name, get_files_data(datatext_names, path)))


def read_text_datatext(datatext_path):
    with open(datatext_path, 'r') as f:
        return f.read()
