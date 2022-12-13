#!/usr/bin/env python3

import unittest, string
from splitnumber_exists import splitnumber_exists

def run_test_cases(self,data):
  debug = False # set to True to show results of own function
  for number, terms_of_sum, split_list, stddev in data:
    exists = splitnumber_exists(number,terms_of_sum)
    if split_list is None:
      self.assertFalse(exists)
    else:
      if debug:
        print('{}\t{}\t{}'.format(number,terms_of_sum, exists))
      self.assertTrue(exists)

class TestSplitnumber(unittest.TestCase):
  def test_cases_from_exercise_sheet(self):
    data = [(11, [2, 3, 5], [2, 2, 2, 2, 3], 0.45),
            (32, [7, 11, 13], [7, 7, 7, 11], 2.0 ),
            (38, [7, 11, 13], [7, 7, 11, 13], 3.0),
            (45, [8, 9], [9, 9, 9, 9, 9], 0.0),
            (47, [11, 12, 13, 14], [11, 12, 12, 12], 0.5),
            (47, [13, 14], None, None)]
    run_test_cases(self,data)

  def test_17_cases(self):
    data = [(17,[7, 8],None,None)]
    run_test_cases(self,data)

  def test_37_cases(self):
    data = [(37,[5, 7],[5, 5, 5, 5, 5, 5, 7],0.76),
            (37,[8, 9],None,None),
            (37,[11, 12],None,None),
            (37,[7, 11, 13],[11, 13, 13],1.15)]
    run_test_cases(self,data)

  def test_32_cases(self):
    data = [(32,[8, 9],[8, 8, 8, 8],0.00),
            (32,[11, 12],None,None),
            (32,[7, 11, 13],[7, 7, 7, 11],2.00)]
    run_test_cases(self,data)

  def test_33_cases(self):
    data = [(33,[8, 9],[8, 8, 8, 9],0.50),
            (33,[11, 12],[11, 11, 11],0.00),
            (33,[7, 11, 13],[11, 11, 11],0.00)]
    run_test_cases(self,data)

  def test_34_cases(self):
    data = [(34,[8, 9],[8, 8, 9, 9],0.58),
            (34,[11, 12],[11, 11, 12],0.58),
            (34,[7, 11, 13],[7, 7, 7, 13],3.00)]
    run_test_cases(self,data)

  def test_35_cases(self):
    data = [(35,[8, 9],[8, 9, 9, 9],0.50),
            (35,[11, 12],[11, 12, 12],0.58),
            (35,[7, 11, 13],[7, 7, 7, 7, 7],0.00)]
    run_test_cases(self,data)

  def test_36_cases(self):
    data = [(36,[8, 9],[9, 9, 9, 9],0.00),
            (36,[11, 12],[12, 12, 12],0.00),
            (36,[7, 11, 13],[7, 7, 11, 11],2.31)]
    run_test_cases(self,data)

  def test_38_cases(self):
    data = [(38,[8, 9],None,None),
            (38,[11, 12],None,None),
            (38,[7, 11, 13],[7, 7, 11, 13],3.00)]
    run_test_cases(self,data)

  def test_39_cases(self):
    data = [(39,[8, 9],None,None),
            (39,[11, 12],None,None),
            (39,[7, 11, 13],[13, 13, 13],0.00)]
    run_test_cases(self,data)

  def test_40_cases(self):
    data = [(40,[8, 9],[8, 8, 8, 8, 8],0.00),
            (40,[11, 12],None,None),
            (40,[7, 11, 13],[7, 11, 11, 11],2.00)]
    run_test_cases(self,data)

  def test_41_cases(self):
    data = [(41,[8, 9],[8, 8, 8, 8, 9],0.45),
            (41,[11, 12],None,None),
            (41,[7, 11, 13],[7, 7, 7, 7, 13],2.68)]
    run_test_cases(self,data)

  def test_42_cases(self):
    data = [(42,[8, 9],[8, 8, 8, 9, 9],0.55),
            (42,[11, 12],None,None),
            (42,[7, 11, 13],[7, 7, 7, 7, 7, 7],0.00)]
    run_test_cases(self,data)

  def test_43_cases(self):
    data = [(43,[8, 9],[8, 8, 9, 9, 9],0.55),
            (43,[11, 12],None,None),
            (43,[7, 11, 13],[7, 7, 7, 11, 11],2.19)]
    run_test_cases(self,data)

  def test_44_cases(self):
    data = [(44,[8, 9],[8, 9, 9, 9, 9],0.45),
            (44,[11, 12],[11, 11, 11, 11],0.00),
            (44,[7, 11, 13],[11, 11, 11, 11],0.00)]
    run_test_cases(self,data)

  def test_45_cases(self):
    data = [(45,[8, 9],[9, 9, 9, 9, 9],0.00),
            (45,[11, 12],[11, 11, 11, 12],0.50),
            (45,[7, 11, 13],[7, 7, 7, 11, 13],2.83)]
    run_test_cases(self,data)

  def test_46_cases(self):
    data = [(46,[8, 9],None,None),
            (46,[11, 12],[11, 11, 12, 12],0.58),
            (46,[7, 11, 13],[11, 11, 11, 13],1.00)]
    run_test_cases(self,data)

  def test_47_cases(self):
    data = [(47,[8, 9],None,None),
            (47,[11, 12],[11, 12, 12, 12],0.50),
            (47,[7, 11, 13],[7, 7, 11, 11, 11],2.19)]
    run_test_cases(self,data)

  def test_48_cases(self):
    data = [(48,[8, 9],[8, 8, 8, 8, 8, 8],0.00),
            (48,[11, 12],[12, 12, 12, 12],0.00),
            (48,[7, 11, 13],[11, 11, 13, 13],1.15)]
    run_test_cases(self,data)

  def test_49_cases(self):
    data = [(49,[8, 9],[8, 8, 8, 8, 8, 9],0.41),
            (49,[11, 12],None,None),
            (49,[7, 11, 13],[7, 7, 7, 7, 7, 7, 7],0.00)]
    run_test_cases(self,data)

unittest.main()
