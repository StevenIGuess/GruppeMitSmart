#!/usr/bin/env python3

import unittest, string
from pwgen_functions import structure_string_is_valid, \
                            structure_elements_list, \
                            randstring, \
                            word_dict_get

class TestPwGenFunctions(unittest.TestCase):
  def test_structure_elements(self):
    struct_str_list = ['w4p2d2w5','w1','d11','p54','p1w1d1','p5d1w5']
    struct_str_pairs_list = [[('w', 4), ('p', 2), ('d', 2), ('w', 5)],
                             [('w', 1)],
                             [('d', 11)],
                             [('p', 54)],
                             [('p', 1), ('w',1), ('d',1)],
                             [('p', 5), ('d', 1), ('w', 5)]]
    self.assertEqual(len(struct_str_list),len(struct_str_pairs_list))
    for struct_str, struct_str_pairs in zip(struct_str_list,
                                            struct_str_pairs_list):
      self.assertTrue(structure_string_is_valid(struct_str))
      self.assertEqual(structure_elements_list(struct_str),
                       struct_str_pairs)
    for struct_str in ['d100','w11','p100','p53']:
      self.assertTrue(structure_string_is_valid(struct_str))
    struct_str_list_invalid = ['','1d','x1','d-1','blabap5w2','xd2','dp2y',
                               'd0','p0w1d0','d1w4bla','d1d']
    for struct_str in struct_str_list_invalid:
      self.assertFalse(structure_string_is_valid(struct_str))
  def test_randstring(self):
    for alphabet in [string.digits,string.punctuation]:
      for length in [1,2,4,7,8]:
        for _ in range(10):
          s = randstring(alphabet,length)
          self.assertEqual(len(s),length)
          self.assertTrue(all([cc in alphabet for cc in s]))
  def test_word_list(self):
    expected_word_dict_lengths = {1: 43,
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
    computed_word_dict_lengths = {k : len(v) for k,v in word_dict.items()}
    self.assertEqual(expected_word_dict_lengths,computed_word_dict_lengths)

unittest.main()
