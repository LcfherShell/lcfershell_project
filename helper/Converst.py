import re
import requests

def ConvertMany(number, conv):
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s +conv.join(reversed(groups))

#print(ConvertMany(1000, '.'))
def Digits(num):
    count = 0
    if num == 0:
        return 1
    
    if num < 0:
        num *= -1

    while (num >= 10**count):
        count += 1
        num += num%10

    return count

print(' * Running Module: Converst')
