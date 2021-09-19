from sys import argv

import random

hand=argv[1]

num=random.randint(0,2)
hai=["ぐー","ちょき","ぱー"]

cpu=hai[num]

if hand==cpu:
  print("あいこ！気が合うな！好き！\n")

elif hand=="ぐー":
  print("ひいっ！殴らないで！\n")
  print(hai[num])
  if cpu=="ちょき":
    print("人生の勝者！\n")
  elif cpu=="ぱー":
    print("負け犬が！何で負けたか明日までに考えといてください\n")

elif hand=="ぱー":
  print("貴様と握手なんぞするつもりはない！\n")
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


