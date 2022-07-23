#Quantifiers

import re
obj1=re.finditer("a{2}","aaa2$b6zcacaZa aa") #lower case
#"a" numbe rof times
#a+ at least kitne bar hai
#a* sagle combination and single
#a? at most
#a{2} aa wala find
#a{a,aaa} min ek bar max 3 bar

for i in obj1:
    print(i.start(), "...", i.group())