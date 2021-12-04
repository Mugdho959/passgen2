import string
import random
s1=string.ascii_letters
s2=string.digits
s3=string.punctuation
passlist=[]

passlist.extend(s1)
passlist.extend(s2)
passlist.extend(s3)
#shuffel The list
random.shuffle(passlist)
#print(passlist)
l=int(input("Enter the password lenth: \n"))
print(f"Your {l} lenth password is")
#This is print first digit
print("".join(passlist[0:l]))
#This is print random digit
#print("".join(random.sample(passlist,l)))
