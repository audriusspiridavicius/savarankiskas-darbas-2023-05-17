import os.path


def read_file_data(file_path):
    """

    :param file_path: the path of the file this function going to read
    :return: returns the content of the given file
    """
    data = None
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = file.readlines()
    return data


def write_data_to_file(data, filename):
    """

    :param data: the data which will be written to file with given name
    :param filename: the name of the file where data will be written
    :return: returns nothing
    """
    with open(filename, "w") as file:
        file.write(str(data))

