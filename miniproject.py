# RANDOM PASSWORD GENERATOR
import random
import string
for j in range(1,3):
 pass_len=8
 charValues=string.ascii_letters+string.digits+string.punctuation

 filename = ""
 for i in range(pass_len):
  filename+=random.choice(charValues)
  f=open(filename,"w")
  data=f.write()
  print(data)
 j+=1

 #f=open("practice.txt","w")
# data=f.write()
# print(data)