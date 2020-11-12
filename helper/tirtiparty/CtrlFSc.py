import re
import os
import sys

def DbName(search, lists):
  text = search
  lists = lists
  for data in lists:
    if re.search(data, text):  
      return data
  return False
  