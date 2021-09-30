import random

def col():
  num=random.randint(0,255)

  return num

def iro():
  r=col()

  g=col()

  b=col()

  return("https://fromkato.com/color/%02x%02x%02x.png"%(r,g,b))

#print(iro())

#%xは代入される値。％ｓだと文字列として代入。だから.pngは％ｘのあとでいい。