"""

  Completed on: 13/10/2020
  Difficulty: Easy
  Url: https://www.hackerrank.com/challenges/two-strings/problem

"""

import math
import os
import random
import re
import sys


# Complete the twoStrings function below.
def twoStrings(s1, s2):
  return "YES" if set(s1) & set(s2) else "NO"



print(twoStrings('hello', 'hello'))