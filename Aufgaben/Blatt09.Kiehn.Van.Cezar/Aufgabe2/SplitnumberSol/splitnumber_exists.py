def splitnumber_exists(remain,terms_of_sum_remain):
  if remain == 0:
    return True
  for idx, this_term in enumerate(terms_of_sum_remain):
    if remain >= this_term and \
       splitnumber_exists(remain - this_term,terms_of_sum_remain[idx:]):
      return True
  return False
