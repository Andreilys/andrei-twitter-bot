import sys
from random import shuffle

command_Args = sys.argv[1:]
shuffle(command_Args)

print("Shuffled list: %s " % command_Args)
