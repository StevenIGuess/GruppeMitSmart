#!/usr/bin/env python3
#title	Sorting a list of strings by their length

unsorted_word_list = ['ag','ga','a','aaa','ca']
#lst{SortWordListbyLength}
length_sorted_word_list = sorted(unsorted_word_list,key=len)
print('length_sorted_word_list = {}'
       .format(length_sorted_word_list))
#lstend#
