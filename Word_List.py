import random
import string

def New_Word_func(file):
    with open(file) as f:
        word_list = f.read().splitlines()
        random_num = random.randint(0, len(word_list)-1)
        return word_list[random_num]