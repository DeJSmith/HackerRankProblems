import math
import os
import random
import re
import sys


def sherlockAndAnagrams(s):
  subs = []
  anagrams = 0

  for i in range(len(s)):
    subs.append(sorted(s[:i]))

  for sub in subs:


  
