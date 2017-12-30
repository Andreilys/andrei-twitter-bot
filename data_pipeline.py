import pandas as pd
import numpy as np
import string
import os

class CleanData():
    def __init__(self):
        self.df = pd.read_csv("barackobama.csv", encoding='latin-1')
        self.data = self.df.loc[:,("text")]
        self.remove_chars()
        self.remove_links()
        self.remove_space()

    def remove_chars(self):
        char_set = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ','0123456789', '0123456789abcdefABCDEF', '01234567','0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', ' \t\n\r\x0b\x0c']
        total_list = []
        for chars in char_set:
            total_list = total_list + (list(chars))
        #remove chars not in list
        remove_list = []
        for text in  self.data:
            for char in text:
                if char not in total_list:
                    total_list = total_list + list(char)
                    self.data = self.data.str.replace(char, " ")

    def remove_space(self):
        def space_remover(string):
            return " ".join(string.split())
        self.data = self.data.apply(space_remover)

    def remove_links(self):
        self.data = self.data.str.replace(r'http.*', "")
        self.data = self.data.str.replace(r'@.*\Z', "")
        self.data = self.data.str.replace(r's', "")

if __name__ == "__main__":
    data = CleanData().data
    for d in data:
        with open('obama_tweets.txt', 'a') as the_file:
            d = d + "\n"
            the_file.write(d)
