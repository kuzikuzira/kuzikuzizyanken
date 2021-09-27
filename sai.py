from sys import argv

import random

kai=int(argv[1])

num=int(argv[2])

i=0
while i < kai:
  dem=random.randint(1,num)
  i+=1
  print(dem)