from data import DICTIONARY, LETTER_SCORES

def load_words(dict_file=DICTIONARY):
    """ (txt file) -> list of str

    Return all lines from dict_file as a list of strings.

    >>> load_words()
    ['A', 'a', 'aa' ... 'Zyzzogeton']
    """
    with open(dict_file) as f:
        words_list = f.read().splitlines()

    return words_list
