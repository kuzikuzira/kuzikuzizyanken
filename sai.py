from sys import argv

import random

text=""

kai=int(argv[1])

num=int(argv[2])

if kai<=100 and num<=100:

  i=0
  while i < kai:
    dem=random.randint(1,num)
    i+=1
    text=text+str(dem)

else:
  text="無理っす。\nできねっす。"
print(text)
