import sys
import re


# Takes the source text input from user, and tokenizes the text
def tokenizer(source_text):
    file = open(source_text)
    open_file = str(file.read().splitlines())
    tokenized_text = re.split(r'[,;!? ]', open_file)
    return tokenized_text


# histogram that takes a source text as input, and returns histogram data structure (dictionarty)
def histogram(source_text):
    length = len(source_text)
    i = 0
    histogram_Dictionary = dict()
    for i in xrange(length):
        # check to see if the dictionary key exists already
        if source_text[i] in histogram_Dictionary:
            histogram_Dictionary[source_text[i]] += 1
        else:
            histogram_Dictionary[source_text[i]] = 1
    return histogram_Dictionary

# Takes a histogram as input, and returns number of unique words (for example they only appear once)
def unique_words(histogram):
    list_Of_Values = list(histogram.values())
    length = len(list_Of_Values)
    unique_words = 0
    for i in xrange(length):
        if list_Of_Values[i] == 1:
            unique_words += 1
    return unique_words

# takes user inputted word, as well as the histogram and returns whether the word exists
def frequency(word, histogram):
    length = len(histogram)
    if histogram.has_key(word):
        return histogram[word]
# Key does not exist
    else:
        print("Key does not exist")
    # for i in xrange(length):
    #     # check to see if the word even exists
    #     if word == histogram[i]:
    #         return ("The word %s appears %d of times" % word, histogram[i])
    #     else:
    #         return("Sorry this doesn't exist")
    #

def random_word(histogram):
    print(histogram)
    

def weighted_word(histogram):

if __name__ == '__main__':
    source_text = raw_input('Enter Source text you would like to create a histogram data structure with: ')
    # histogram that takes a source text as input, and returns histogram data structure (dictionarty)
    tokenized_text = tokenizer(source_text)
    histogram = histogram(tokenized_text)
    # returns number of unique words in the histogram
    # number_of_unique_words = unique_words(histogram)
    # print("There are %s unique words" % number_of_unique_words)
    # word = raw_input("Which word would you like to check the frequency of? ")
    # print("The word: %s, appears %d number of times" % (word, frequency(word, histogram)))
    print("This is a random word from the histogram: %s" % random_word(histogram))
    print("This is a weighted word from the histogram: %s" % weighted_word(histogram))
