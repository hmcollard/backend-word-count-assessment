#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "Haley Collard with some help from demo"

import sys


def create_word_dict(filename):
    """Returns a word/count dict for the given file."""
    my_dict = {}
    with open(filename) as f:
        for line in f.readlines():
            for word in line.lower().split():
                if word in my_dict:
                    my_dict[word] += 1
                else:
                    my_dict[word] = 1
    return my_dict

# class code:
# with open(filename) as f:
#     text = f.read().split()

# word_dict = {}
# for word in text:
#     if word not in word_dict:
#         word_dict[word] = 1
#     else:
#         word_dict[word] += 1
# sorted_words = sorted(list(word_dict.items()))
# for k, v in sorted_words:
#     print(f"{k} : {v}")


def print_words(filename):
    """Prints one per line '<word> : <count>', sorted
    by word for the given file.
    """
    new_dict = create_word_dict(filename)
    key_arr = []
    for key, value in new_dict.items():
        key_arr.append(str(key) + ': ' + str(value))
    key_arr.sort()
    for i, word in enumerate(key_arr):
        print(word)

# class code:
# def sort_by_count(t):
#     return t[1]

# def print_top(filename):
#     word_dict = create_word_dict(filename)
#     sorted_words = sorted(list(word_dict.items()), key=sort_by_count, reverse=True)
#     for k, v in sorted_words[:20]:
#       print(f"{k} : {v}")


def print_top(filename):
    """Prints the top count listing for the given file."""
    new_dict = create_word_dict(filename)
    sorted_list = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
    for word in sorted_list[:20]:
        print(str(word[0]) + ': ' + str(word[1]))


# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
