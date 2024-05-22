#!/usr/bin/env python3

def return_evens(num_list):
    new_list = [num for num  in num_list if num % 2 == 0]
    # new_list = []
    # for num in num_list:
    #     if num % 2 == 0:
    #         new_list.append(num)
    return new_list
    #pass

def make_exclamation(sentence_list):
    ammended_sentence = [f"{char}!" for char in sentence_list]
    return ammended_sentence
    pass


print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))

# print(return_evens([1, 4, 7, 9, 12]))