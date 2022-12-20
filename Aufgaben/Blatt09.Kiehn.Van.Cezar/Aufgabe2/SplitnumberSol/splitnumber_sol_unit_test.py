#!/usr/bin/env python3

import sys, unittest, string
from splitnumber_sol import splitnumber_sol

def run_test_cases(self,data):
  debug = False # set to True to show results of own function
  for number, terms_of_sum, solutions in data:
    your_solutions = splitnumber_sol(number,terms_of_sum)
    if debug:
      print('{}\t{}\t{}'.format(number,terms_of_sum, your_solutions))
    s_solutions = set(map(str,solutions))
    s_your_solutions = set(map(str,your_solutions))
    self.assertEqual(s_your_solutions,s_solutions)

class TestSplitnumber(unittest.TestCase):
  def test_cases_from_exercise_sheet(self):
    data = [(11,[2,3,5],[[2,2,2,2,3],[2,2,2,5],[2,3,3,3],[3,3,5]]),
            (32,[7,11,13],[[7,7,7,11]]),
            (38,[7,11,13],[[7,7,11,13]]),
            (45,[8,9],[[9,9,9,9,9]]),
            (47,[11,12,13,14],[[11,11,11,14],[11,11,12,13],[11,12,12,12]]),
            (47,[13,14],[])]
    run_test_cases(self,data)

  def test_17_cases(self):
    data = [(17,[7, 8],[])]
    run_test_cases(self,data)

  def test_37_cases(self):
    data = [(37,[5, 7],[[5, 5, 5, 5, 5, 5, 7]]),
            (37,[8, 9],[]),
            (37,[11, 12],[]),
            (37,[7, 11, 13],[[11, 13, 13]])]
    run_test_cases(self,data)

  def test_32_cases(self):
    data = [(32,[8, 9],[[8, 8, 8, 8]]),
            (32,[11, 12],[]),
            (32,[7, 11, 13],[[7, 7, 7, 11]])]
    run_test_cases(self,data)

  def test_33_cases(self):
    data = [(33,[8, 9],[[8, 8, 8, 9]]),
            (33,[11, 12],[[11, 11, 11]]),
            (33,[7, 11, 13],[[7, 13, 13], [11, 11, 11]])]
    run_test_cases(self,data)

  def test_34_cases(self):
    data = [(34,[8, 9],[[8, 8, 9, 9]]),
            (34,[11, 12],[[11, 11, 12]]),
            (34,[7, 11, 13],[[7, 7, 7, 13]])]
    run_test_cases(self,data)

  def test_35_cases(self):
    data = [(35,[8, 9],[[8, 9, 9, 9]]),
            (35,[11, 12],[[11, 12, 12]]),
            (35,[7, 11, 13],[[7, 7, 7, 7, 7], [11, 11, 13]])]
    run_test_cases(self,data)

  def test_36_cases(self):
    data = [(36,[8, 9],[[9, 9, 9, 9]]),
            (36,[11, 12],[[12, 12, 12]]),
            (36,[7, 11, 13],[[7, 7, 11, 11]])]
    run_test_cases(self,data)

  def test_38_cases(self):
    data = [(38,[8, 9],[]),
            (38,[11, 12],[]),
            (38,[7, 11, 13],[[7, 7, 11, 13]])]
    run_test_cases(self,data)

  def test_39_cases(self):
    data = [(39,[8, 9],[]),
            (39,[11, 12],[]),
            (39,[7, 11, 13],[[7, 7, 7, 7, 11], [13, 13, 13]])]
    run_test_cases(self,data)

  def test_40_cases(self):
    data = [(40,[8, 9],[[8, 8, 8, 8, 8]]),
            (40,[11, 12],[]),
            (40,[7, 11, 13],[[7, 7, 13, 13], [7, 11, 11, 11]])]
    run_test_cases(self,data)

  def test_41_cases(self):
    data = [(41,[8, 9],[[8, 8, 8, 8, 9]]),
            (41,[11, 12],[]),
            (41,[7, 11, 13],[[7, 7, 7, 7, 13]])]
    run_test_cases(self,data)

  def test_42_cases(self):
    data = [(42,[8, 9],[[8, 8, 8, 9, 9]]),
            (42,[11, 12],[]),
            (42,[7, 11, 13],[[7, 7, 7, 7, 7, 7], [7, 11, 11, 13]])]
    run_test_cases(self,data)

  def test_43_cases(self):
    data = [(43,[8, 9],[[8, 8, 9, 9, 9]]),
            (43,[11, 12],[]),
            (43,[7, 11, 13],[[7, 7, 7, 11, 11]])]
    run_test_cases(self,data)

  def test_44_cases(self):
    data = [(44,[8, 9],[[8, 9, 9, 9, 9]]),
            (44,[11, 12],[[11, 11, 11, 11]]),
            (44,[7, 11, 13],[[7, 11, 13, 13], [11, 11, 11, 11]])]
    run_test_cases(self,data)

  def test_45_cases(self):
    data = [(45,[8, 9],[[9, 9, 9, 9, 9]]),
            (45,[11, 12],[[11, 11, 11, 12]]),
            (45,[7, 11, 13],[[7, 7, 7, 11, 13]])]
    run_test_cases(self,data)

  def test_46_cases(self):
    data = [(46,[8, 9],[]),
            (46,[11, 12],[[11, 11, 12, 12]]),
            (46,[7, 11, 13],[[7, 7, 7, 7, 7, 11], [7, 13, 13, 13],
                             [11, 11, 11, 13]])]
    run_test_cases(self,data)

  def test_47_cases(self):
    data = [(47,[8, 9],[]),
            (47,[11, 12],[[11, 12, 12, 12]]),
            (47,[7, 11, 13],[[7, 7, 7, 13, 13], [7, 7, 11, 11, 11]])]
    run_test_cases(self,data)

  def test_48_cases(self):
    data = [(48,[8, 9],[[8, 8, 8, 8, 8, 8]]),
            (48,[11, 12],[[12, 12, 12, 12]]),
            (48,[7, 11, 13],[[7, 7, 7, 7, 7, 13], [11, 11, 13, 13]])]
    run_test_cases(self,data)

  def test_49_cases(self):
    data = [(49,[8, 9],[[8, 8, 8, 8, 8, 9]]),
            (49,[11, 12],[]),
            (49,[7, 11, 13],[[7, 7, 7, 7, 7, 7, 7], [7, 7, 11, 11, 13]])]
    run_test_cases(self,data)

unittest.main()
