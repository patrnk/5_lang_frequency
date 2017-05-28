from collections import Counter
from argparse import ArgumentParser
from sys import argv


def read_text_from_file(filepath):
    with open(filepath) as text_file:
        return text_file.read()


def remove_nonalpha_chars(text, ignore_list=[]):
    filtered_list = [char for char in list(text) if char.isalpha() or char in ignore_list]
    filtered_text = ''.join(filtered_list)
    return filtered_text


def get_most_frequent_words(text, top_counter):
    filtered_text = remove_nonalpha_chars(text, [' ', '\n'])
    words = filtered_text.lower().split()
    common_words_info = Counter(words).most_common(top_counter)
    common_words = [word for word, _ in common_words_info]
    return common_words


def parse_args(argv):
    parser = ArgumentParser()
    parser.add_argument(
        'filepath',
        type=str,
        help='File containing the text'
    )
    parser.add_argument(
        '--top',
        type=int,
        default=10,
        help='A number of most common words to display'
    )
    return parser.parse_args(argv)
                        

if __name__ == '__main__':
    args = parse_args(argv[1:])
    text = read_text_from_file(args.filepath)
    most_common_words = get_most_frequent_words(text, args.top)
    print(' '.join(most_common_words))
