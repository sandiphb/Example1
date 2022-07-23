#----------------
# import re
# a=re.compile("ab")
# reobj=a.finditer("abaaba")
# for i in reobj:
#     print(i.start(),"...",i.group())

#---------------
# import re
# reobj=re.finditer("ab","abaaba")
# for i in reobj:
#     print(i.start(),"...",i.group())

#---------------
# import re
# #obj1=re.finditer("[abc]","aaa2$b6ccZ") #either a or b or c
# obj1=re.finditer("[^abc]","aaa2$b6ccZ") #except abc
#
# for i in obj1:
#     print(i.start(), "...", i.group())

#------------
# import re
# obj1=re.finditer("[a-z]","aaa2$b6ccZ") #lower case
# "[0-9]" "[A-Z]" [a-zA-Z0-9][^a-z]
# for i in obj1:
#     print(i.start(), "...", i.group())

import re
obj1=re.finditer("[a-z]","a aa2$b6ccZ") #lower case
#\s space ,\S except ,\d digit \D \w word character except space and special \W
#\. complete string
#combination \s\d
#[\s\d]
#[a-z][\s]
for i in obj1:
    print(i.start(), "...", i.group())


