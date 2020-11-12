import string
import random
import re
import os

KEY_LEN = 20
def base_str(name):
    return name   

def clean_str(name):
    exection = ["<", "/", "-", ";", ":", "=", "'", ">", "{", "}"]
    text =  name
    if re.search(exection[0], text):
       output = re.sub('\W+', '', text)

    elif re.search(exection[1], text):
       output = re.sub('\W+', '', text)

    elif re.search(exection[2], text):
       output = re.sub('\W+', '', text)

    elif re.search(exection[3], text):
       output = re.sub('\W+', '', text)
    elif re.search(exection[4], text):
       output = re.sub('\W+', '', text)
    elif re.search(exection[5], text):
       output = re.sub('\W+', '', text)
    elif re.search(exection[6], text):
       output = re.sub('\W+', '', text)
    elif re.search(exection[7], text):
       output = re.sub('\W+', '', text)
    elif re.search(exection[8], text):
       output = re.sub('\W+', '', text)
    elif re.search(exection[9], text):
       output = re.sub('\W+', '', text)
    else:
       output = text

    return output

def key_gen(name, **tx):
    text = tx
    for key, value in text.items():
        select = key
    if select == 'clean':
       keylist = [random.choice(clean_str(name)) for i in range(KEY_LEN)]
    else:  
       keylist = [random.choice(base_str(name)) for i in range(KEY_LEN)]
    
    output = "".join(keylist)
    return output