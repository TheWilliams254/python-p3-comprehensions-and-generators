#!/usr/bin/env python3

def return_evens(num_list):
    evens = [n for n in num_list if n % 2 == 0]
    return evens
    pass
print(return_evens([0, 1, 3, 5, 7, 8, 9]))
def make_exclamation(sentence_list):
    exclamation_list = [s + "!" for s in sentence_list]
    return exclamation_list
    pass
make_exclamation(["Hello", "I am doing great", "Python is fun"])