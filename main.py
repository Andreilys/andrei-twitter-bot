import histogram
import hashtable
import Heap
from text_tokenizer import *
from hashtable import *
from histogram import *
from Heap import MaxHeap
from markovChain import SentenceGenerator
import twitter
from os.path import join, dirname
from dotenv import load_dotenv
import os

# If we subtract the Unix dictionary's keys from our word count dict's keys,
#  we can find specialized/jargon words in our corpus or words
# we didn't normalize. We can even use this to refine our regular expressions
# and normalization techniques!

if __name__ == '__main__':
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path, verbose=True)
    api = twitter.Api(consumer_key=os.environ.get('CONSUMER_KEY'),
                      consumer_secret=os.environ.get('CONSUMER_SECRET'),
                      access_token_key=os.environ.get('ACCESS_TOKEN'),
                      access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET'))

    user_input = "obama_tweets.txt"
    tokenized_text = text_Parser(user_input)
    # TODO are we supposed to rewrite the histogram function to incorporate our hash table?
    histogram = histogram(tokenized_text)
    max_heap = MaxHeap()
    for i in histogram:
        max_heap.insert((i, histogram[i]))
    words = "obama_tweets.txt"
    tokenized_text = text_Parser(words)
    sentence_generator = SentenceGenerator(10)
    List = sentence_generator.build_dict(tokenized_text)
    sentence = sentence_generator.generate_sentences(List)
    # status = api.PostUpdate(sentence)
    # print(status.text)
