import pickle


def read_pickle_file(filename):
    data_from_file = None
    print(f"filename {filename}")
    with open(filename, "rb") as datafile:
        data_from_file = pickle.load(datafile)
    return data_from_file


def save_to_picle_file(data, filename):
    data_from_file = []
    try:
        data_from_file = read_pickle_file(filename)
    except FileNotFoundError:
        print("file was not found.")
    except EOFError:
        print("file is empty")
        pass
    with open(filename, "wb") as datafilewrite:
        data = data_from_file + data
        pickle.dump(data, datafilewrite)
