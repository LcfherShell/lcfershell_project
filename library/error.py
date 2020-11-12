import sys
import requests
import os
import pip
import getopt

class Checked:
    def __init__(self, x):
          self.o = x
    def Check(self):
          modulename = self.o 
          if modulename not in sys.modules:
              pip.main(['install', modulename])
          return True

         
module= Checked("sys")
print(module.Check())

version = '1.0'
verbose = False
output_filename = 'default.out'

print('ARGV      :', sys.argv[1:])

options, remainder = getopt.getopt(sys.argv[1:], 'o:v', ['output=', 
                                                         'verbose',
                                                         'version=',
                                                         ])
print('OPTIONS   :', options)

for opt, arg in options:
    if opt in ('-o', '--output'):
        output_filename = arg
    elif opt in ('-v', '--verbose'):
        verbose = True
    elif opt == '--version':
        version = arg
    else:
        print(False)

print('VERSION   :', version)
print('VERBOSE   :', verbose)
print('OUTPUT    :', output_filename)
print ('REMAINING :', remainder)