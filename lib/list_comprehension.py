#!/usr/bin/env python3

def return_evens(num_list):

    list_comprehension = [ n for n in num_list if n % 2 == 0]

    return(list_comprehension)

def make_exclamation(sentence_list):
    ex_list = [ word + "!" for word in sentence_list]
    
    return(ex_list) 