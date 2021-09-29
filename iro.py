import random

def col():
  num=random.randint(0,255)
  return num

r=col()

g=col()

b=col()

print("https://fromkato.com/color/%x%x%x.png"%(r,g,b))