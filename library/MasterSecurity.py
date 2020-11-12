import os
import re
import sys
import base64

class MasterSec:
   def __init__(self, x):
      self.o = x
   def XsSecForm_Default(self):
      exection = ["<", "/", "-", ";", ":", "=", "'", ">", "{", "}"]
      text =  self.o
      if re.search(exection[0], text):
            return False
      elif re.search(exection[1], text):
            return False
      elif re.search(exection[2], text):
            return False
      elif re.search(exection[3], text):
            return False
      elif re.search(exection[4], text):
            return False
      elif re.search(exection[5], text):
            return False
      elif re.search(exection[6], text):
            return False
      elif re.search(exection[7], text):
            return False
      elif re.search(exection[8], text):
            return False
      elif re.search(exection[9], text ):
            return False
      else:
            return True

   def XsSecForm_Clean(self):
      exection = ["<", "/", "-", ";", ":", "=", "'", ">", "{", "}"]
      text = self.o
      if re.search(exection[0], text):
            return re.sub('\W+', '', text)
      elif re.search(exection[1], text):
            return re.sub('\W+', '', text)
      elif re.search(exection[2], text):
            return re.sub('\W+', '', text)
      elif re.search(exection[3], text):
            return re.sub('\W+', '', text)
      elif re.search(exection[4], text):
            return re.sub('\W+', '', text)
      elif re.search(exection[5], text):
            return re.sub('\W+', '', text)
      elif re.search(exection[6], text):
            return re.sub('\W+', '', text)
      elif re.search(exection[7], text):
            return re.sub('\W+', '', text)
      elif re.search(exection[8], text):
            return re.sub('\W+', '', text)
      elif re.search(exection[9], text):
            return re.sub('\W+', '', text)
      else:
            return False
  
  ##########Allow Chart
   def XsSecForm_Allow(self):
      regex = r"([$@%&*^.]+)" #a-zA-Z0-9
      text =  self.o
   
      if type(text) == int or type(text) == float:
            return False
      else:
            match = re.search(regex, text)
            if match:
                  return True #match.group()
            else:
                  return False
   ##############
   def CveFile(self):
      text =  self.o
      name, ext = os.path.splitext(text)
      exection =[".jpg", ".jpeg", ".png", ".pdf", ".docx", ".txt", ".xlsx", ".mp3", ".mp4"]
      if re.search(exection[0], ext):
            return True
      elif re.search(exection[1], ext):
            return True
      elif re.search(exection[2], ext):
            return True
      elif re.search(exection[3], ext):
            return True
      elif re.search(exection[4], ext):
            return True
      elif re.search(exection[5], ext):
            return True
      elif re.search(exection[6], ext):
            return True
      elif re.search(exection[7], ext):
            return True
      elif re.search(exection[8], ext):
            return True
      else:
            files = name+" "+ext
            return files

def ExtFiles(files, *kwargs):      
      name, ext = os.path.splitext(files)
      exection =["."]

      for data in kwargs:
          if data == "name":
                return name
          elif data == "ext":
                if re.search(exection[0], ext):
                    return re.sub('\W+', '', ext)
          elif data == 'all':
                return name, ext
          else:
                return False

def Base64File(files, *kwargs):
      files = files
      for data in kwargs:
            if data == 'encode':
                  with open(files, 'rb') as imagefile:
                        bytefiles = base64.b64encode(imagefile.read())
                        return bytefiles
            elif data == 'decode':
                        files = open(files, 'rb')
                        byte = files.read()
                        files.close()
                        bytefiles = base64.b64decode(byte)
                        return bytefiles
            else:
                  return False

print(' * Running Module: MasterSecurity')
