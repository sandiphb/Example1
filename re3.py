#Functions

#match()
#sabse pehle available hai kya ,start

# import re
# a="ab"
# m=re.match(a,"abcz")
# #print(m.start())
# #"abcz" ,for start with z , returns None
# print(m)


#findall()
#
# import re
# m=re.findall("[A-Z]","abcz")
# #abc checks if abc present ,returns in form of list
# print(m)

#search()
import re
a='ab'
m=re.search(a,"abcz")
#search given string in whole string
print(m)

#sub
#replacement or substitution
import re
m=re.sub("[A-Z]","**","abc4TRz")
#search given string in whole string
print(m)


#subn
#kitne bar replace hua hai
# import re
# m=re.subn("[A-Z]","*","abc4TRz")
# #search given string in whole string
# print(m)


#split
# import re
# m=re.split(",","khushboo,Team of,data engineers")
# #search given string in whole string
# print(m)


#compile
#finditer

#fullmatch
# import re
# s="abc"
# m=re.fullmatch(s,"abcddkds8&")
# #Puri string match honi chahiye
# print(m)

#space+ ne 2/3 space tithe replace \s+



