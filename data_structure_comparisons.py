import sys
import re
import random
import timeit


# Takes the source text input from user, and tokenizes the text
def tokenizer(source_text):
    file = open(source_text)
    open_file = str(file.read().splitlines())
    tokenized_text = re.split(r'[,;!? ]', open_file)
    return tokenized_text


# List function
def list(length):
    dict_words = '/usr/share/dict/words'
    words_str  = open(dict_words, 'r').read()
    all_words  = words_str.split("\n")
    return all_words[0:length]

# histogram that takes a source text as input, and returns histogram data structure (dictionary)
def histogram_dic(tokenized_text):
    length = len(tokenized_text)
    i = 0
    histogram_Dictionary = dict()
    for i in xrange(length):
        # check to see if the dictionary key exists already
        if tokenized_text[i] in histogram_Dictionary:
            histogram_Dictionary[tokenized_text[i]] += 1
        else:
            histogram_Dictionary[tokenized_text[i]] = 1
    # removing some unnecssary words
    histogram_Dictionary.pop('', 0)
    return histogram_Dictionary

# takes user inputted word, as well as the histogram and returns whether the word exists
# Big-O complexity is: O(n)
def frequency_dict(word, histogram):
    length = len(histogram)
    if histogram.has_key(word):
        return histogram[word]
# Key does not exist
    else:
        print("Key does not exist")


def histogram_tuples(tokenized_text):
    histogram_tuple = []
    for word in tokenized_text:
        index = find(word, histogram_tuple)
        if index == None:
            histogram_tuple.append((word, 1))
        else:
            count = histogram_tuple[index][1]
            new_pair = (word, count + 1)
            histogram_tuple[index] = new_pair
    return histogram_tuple

# find function
def find(item, histogram_tuple):
    for index, pair in enumerate(histogram_tuple):
        if pair[0] == item:
            return index
    return None


# Big-O complexity is O(n):
def frequency_tuples(word, histogram):
    index = find(word, histogram)
    if index:
        word_count_pair = histogram[index]
        return word_count_pair[1]
    else:
        return 0


class Node(object):
    def __init__(self, data=None, next_node=None, freq=None):
        self.data = data
        self.freq = freq
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_freq(self):
        return self.freq

    def set_next(self, new_next):
        self.next_node = new_next


# List function
def list(length):
    dict_words = '/usr/share/dict/words'
    words_str = open(dict_words, 'r').read()
    all_words = words_str.split("\n")
    return all_words[0:length]


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data, freq):
        new_node = Node(data)
        new_node.freq = freq
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            return None
        return current

    def __str__(self):
        current = self.head
        return str(current.data)


def linkogram(words):
    linked_List = LinkedList()
    for i in words:
        if linked_List.search(i):
            a = linked_List.search(i)
            a.freq += 1
        else:
            linked_List.insert(i, 1)
    return linked_List


# Big-O complexity is: O(n)
def frequency_singlyLinkedList(word, linkogram):
    word = linkogram.search(word)
    return ("The word frequency is: " + str(word.freq))

# def random_word(histogram):
#     list = []
#     for key in histogram:
#         if histogram[key] == 1:
#             list.append(key)
#         else:
#             i = 0
#             while i < histogram[key]:
#                 list.append(key)
#                 i = i + 1
#     length = len(list) - 1
#     random_word = list[random.randint(0, length)]
#     return random_word
#
#
# def weighted_word(histogram):
#     # place holder for number of words
#     number_of_words = 0
#     for key in histogram:
#         number_of_words = number_of_words + histogram[key]
#     # assign the histogram[key] for a new probability
#     for key in histogram:
#         histogram[key] = histogram[key] / float(number_of_words)
#     # select random number between 0 and 1
#     random_Number = random.randint(0, 1)
#     # walk the list, subtracting weight of each number as you go, as you get to 0, choose the item
#     for key in histogram:
#         random_Number = random_Number - histogram[key]
#         if random_Number <= 0:
#             return key



if __name__ == '__main__':
    # source_text = raw_input('Enter Source text you would like to create a histogram data structure with: ')
    # # histogram that takes a source text as input, and returns histogram data structure (dictionarty)
    # tokenized_text = tokenizer(list(10))

    # List being used by words
    hundred_words = list(100)
    ten_thousand_words = list(1000)
    hundred_search = hundred_words[-1]
    ten_thousand_search = ten_thousand_words[-1]

    # dictionary analysis
    hundred_dictogram = histogram_dic(hundred_words)
    ten_thousand_dictogram = histogram_dic(ten_thousand_words)
    stmt  = "frequency_dict('{}', hundred_dictogram)".format(hundred_search)
    setup = "from __main__ import frequency_dict, hundred_dictogram"
    timer = timeit.Timer(stmt, setup=setup)
    iterations = 10000
    result = timer.timeit(number=iterations)
    print("frequency_dict() time for 100-word dictogram: " + str(result))

    # tuple analysis
    hundred_tuplegram = histogram_tuples(hundred_words)
    ten_thousand_tuplegram = histogram_tuples(ten_thousand_words)
    stmt  = "frequency_tuples('{}', hundred_tuplegram)".format(hundred_search)
    setup = "from __main__ import frequency_tuples, hundred_tuplegram"
    timer = timeit.Timer(stmt, setup=setup)
    iterations = 10000
    result = timer.timeit(number=iterations)
    print("frequency_tuple() time for 100-word tuplegram: " + str(result))

    hundred_linkogram = linkogram(hundred_words)
    ten_thousand_linkogram = linkogram(ten_thousand_words)
    stmt  = "frequency_singlyLinkedList('{}', hundred_linkogram)".format(hundred_search)
    setup = "from __main__ import frequency_singlyLinkedList, hundred_linkogram"
    timer = timeit.Timer(stmt, setup=setup)
    iterations = 10000
    result = timer.timeit(number=iterations)
    print("frequency_singlyLinkedList() time for 100-word linkogram: " + str(result))
    # print(frequency_tuples('a', histogram_tuple))

    # returns number of unique words in the histogram
    # number_of_unique_words = unique_words(histogram)
    # print("There are %s unique words" % number_of_unique_words)
    # word = raw_input("Which word would you like to check the frequency of? ")
    # print("The word: %s, appears %d number of times" % (word, frequency(word, histogram)))
