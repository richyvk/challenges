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


def calc_word_value():
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    pass


def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass


if __name__ == "__main__":
    pass # run unittests to validate
