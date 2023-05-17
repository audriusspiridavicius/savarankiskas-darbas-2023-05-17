def get_word_first_letter(words):
    letters = [word[0].upper() for word in words]

    return letters


def get_unique_records(values):

    unique_values = set(values)

    return tuple(unique_values)