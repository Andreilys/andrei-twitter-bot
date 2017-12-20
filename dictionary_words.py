import random
import sys


# This function returns maximum amount of words in the text file
def max_Word_Finder(a_string):
    num_words = 0
    for line in a_string:
        num_words += len(line.split())
    return num_words


# This function returns "x" number of randomly generated numbers
def random_Number_Generator():
    file = open('stoicism.txt')
    # read file and split the lines
    a_string = file.read().splitlines()
    max_Words = max_Word_Finder(a_string)
    random_Number = random.randrange(0, max_Words)
    return random_Number


# List Generator
def random_Word_Finder(total):
    file = open('stoicism.txt')
    # read file and split the lines
    word_List = file.read().splitlines()
    words = word_List[0].split(' ')
    list_Of_Words = []
    count = 0
    while (count < total):
        list_Of_Words.append(words[random_Number_Generator()])
        count = count + 1
    return list_Of_Words

if __name__ == '__main__':
    # file name does not count as argument, need to convert to int
    total = int(sys.argv[1])
    file = open('stoicism.txt')
    # read file and split the lines
    word_list = file.read().splitlines()
    # finds maximum number of words used
    # randomly generates numbers with the max word ceiling
    print("Random List of words: %s" % random_Word_Finder(total))
