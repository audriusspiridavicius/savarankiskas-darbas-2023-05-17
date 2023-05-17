import statistics
def get_word_first_letter(words):
    letters = [word[0].upper() for word in words]

    return letters


def get_unique_records(values):

    unique_values = set(values)

    return tuple(unique_values)


def get_mean(items_list):
    result = []
    for item in items_list:
        string_value = ""
        numbers_mean = 0
        for element in item:
            if type(element) is str:
                string_value = element
            else:
                numbers_mean = statistics.mean(element)
        result.append(tuple([string_value, numbers_mean]))
    return result