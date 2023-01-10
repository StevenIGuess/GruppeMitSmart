#!/usr/bin/env python3

import unittest, string
from pwgen import password_generate
from pwgen_functions import word_dict_get, structure_elements_list

def make_struct_str(cc,nums):
  return ''.join(['{}{}'.format(cc,m) for m in nums])

def check_password_length(pw,struct_str):
  ms = [m for _, m in  structure_elements_list(struct_str)]
  return len(pw) == sum(ms)

def check_password_content(word_dict,pw,struct_str):
  idx = 0
  for t, m in structure_elements_list(struct_str):
    if t == 'w':
      if pw[idx:idx+m] not in word_dict[m]:
        return False
    else:
      assert t in 'dp'
      alphabet = string.digits if t == 'd' else string.punctuation
      for cc in pw[idx:idx+m]:
        if cc not in alphabet:
          return False
    idx += m
  return True
    
class TestPwGen(unittest.TestCase):
  def test_passwort_generate(self):
    word_dict_lengths = {1: 43,
                         2: 122,
                         3: 726,
                         4: 2143,
                         5: 3132,
                         6: 3987,
                         7: 4041,
                         8: 3385,
                         9: 2510,
                         10: 1570,
                         11: 884,
                         12: 435,
                         13: 253,
                         14: 99,
                         15: 32,
                         16: 10,
                         17: 2}
    word_dict = word_dict_get()
    some_p = make_struct_str('p',range(1,5+1))
    some_d = make_struct_str('d',range(1,5+1))
    all_w = make_struct_str('w',word_dict_lengths.keys())
    struct_str_list = ['w4p2d2w5',some_p,some_d,all_w]
    expected_choice_lists = [[2143,1024,100,3132],
                             [32, 1024, 32768, 1048576, 33554432],
                             [10, 100, 1000, 10000, 100000],
                             list(word_dict_lengths.values())]
    for struct_str, cl in zip(struct_str_list,expected_choice_lists):
      pw, choice_list = password_generate(word_dict,struct_str)
      self.assertEqual(choice_list,cl)
      self.assertTrue(check_password_length(pw,struct_str))
      self.assertTrue(check_password_content(word_dict,pw,struct_str))

unittest.main()
