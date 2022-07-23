import json
import re

a=re.compile("ab")


fp=open('k7.txt','r')
for x,y in enumerate(fp):
    for i in re.finditer(a,y):
        print(i)