import os
import re
import sys

class Validator:
   def __init__(self, x):
      self.o = x
   def ValidatorForm(self):
      exection = ["@"]
      text =  self.o
      if re.search(exection[0], text):
            return False
      else:
            return True
