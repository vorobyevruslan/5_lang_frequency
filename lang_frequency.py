import re


def load_data(filepath):
    list_of_words = []
    with open(filepath) as opened_file:
        for line in opened_file:
            list_of_words += re.split(r'[:\.\?\!\*;,_—\[\]\s\d]', line.lower())
    return list_of_words


def get_most_frequent_words(text):
    vocabulary = {}
    for word in text:
        if word != '':
            if word in vocabulary:
                vocabulary[word] += 1
            else:
                vocabulary[word] = 1
    return sorted(vocabulary, key=vocabulary.__getitem__)


def show_10_words(vocabulary):
    for index in range(-1,-11,-1):
        print(vocabulary[index])


if __name__ == '__main__':
    filepath = input()
    text = load_data(filepath)
    vocabulary = get_most_frequent_words(text)
    show_10_words(vocabulary)
