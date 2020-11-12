import re

def clean(name):
#search = input('Masukan Email: ')
     get = re.findall(r"^\w+", name)
     for check in get :
        	return check
        	
def nclean(name):
        foo = name
        ss = foo.replace(" ", "").rstrip()[:2].upper()
        minsprice = float(ss)
        output = str(round(minsprice))
        return output
        
def spaclean(name):
        foo = name
        output = foo.replace(" ", "")
        return output

def mclean(name):
     num_format = re.compile(r'^\-?[1-9][0-9]*\.?[0-9]*')
     isnumber = re.match(num_format, name)
     if isnumber:
        resl = ''.join(i for i in name if not i.isdigit())
        return resl
     else:
        return name

print(' * Running Module: MasterValidations')
