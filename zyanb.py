from sys import argv

import random

hand=(argv[1])

num=random.randint(0,2)
hai=["ぐー","ちょき","ぱー"]

cpu=hai[num]

if hand=="ぐー":
  print("ぐーをだしましたか…\n")
  print(hai[num])
  if cpu=="ちょき":
    print("人生の勝者！\n")
  elif cpu=="ぱー":
    print("負け犬が！何で負けたか明日までに考えといてください\n")

elif hand=="ぱー":
  print("ぱーをだしたな！\n")
  print(hai[num])
  if cpu=="ぐー":
    print("人生の勝者！\n")
  elif cpu=="ちょき":
    print("負け犬が！何で負けたか明日までに考えといてください\n")

elif hand=="ちょき":
  print("蟹の真似事か!小ざかしい！\n")
  print(hai[num])
  if cpu=="ぱー":
    print("人生の勝者！\n")
  elif cpu=="ぐー":
    print("負け犬が！何で負けたか明日までに考えといてください\n")

else :
  print("ふざけないでください！\n")

while hand==cpu:
  print("あいこだ！もう一度！\n")
  hand=input()

  num=random.randint(0,2)
  hai=["ぐー","ちょき","ぱー"]
  print(hai[num])
  cpu=hai[num]

  if hand=="ぐー":
    print("ぐーをだしましたか…\n")
    print(hai[num])
    if cpu=="ちょき":
      print("人生の勝者！1\n")
    elif cpu=="ぱー":
      print("負け犬が！何で負けたか明日までに考えといてください\n")

  elif hand=="ぱー":
    print("ぱーをだしたな！\n")
    print(hai[num])
    if cpu=="ぐー":
      print("人生の勝者！2\n")
    elif cpu=="ちょき":
      print("負け犬が！何で負けたか明日までに考えといてください\n")

  elif hand=="ちょき":
     print("蟹の真似事か!小ざかしい！\n")
     print(hai[num])
     if cpu=="ぱー":
       print("人生の勝者！3\n")
     elif cpu=="ぐー":
       print("負け犬が！何で負けたか明日までに考えといてください\n")

  else :
    print("ふざけないでください！\n")

