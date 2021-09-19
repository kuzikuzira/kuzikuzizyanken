from sys import argv

text=""
comment=""

import random

hand=argv[1]

num=random.randint(0,2)
hai=["ぐー","ちょき","ぱー"]

cpu=hai[num]

if hand==cpu:
  text="あいこ！気が合うな！好き！\n"

elif hand=="ぐー":
  comment="ひいっ！殴らないで！\n"
  text=hai[num]
  if cpu=="ちょき":
    text="人生の勝者！\n"
  elif cpu=="ぱー":
    text="負け犬が！何で負けたか明日までに考えといてください\n"

elif hand=="ぱー":
  comment="貴様と握手なんぞするつもりはない！\n"
  text=hai[num]
  if cpu=="ぐー":
    text="人生の勝者！\n"
  elif cpu=="ちょき":
    text="負け犬が！何で負けたか明日までに考えといてください\n"

elif hand=="ちょき":
  comment="蟹の真似事か!小ざかしい！\n"
  text=hai[num]
  if cpu=="ぱー":
    text="人生の勝者！\n"
  elif cpu=="ぐー":
    text="負け犬が！何で負けたか明日までに考えといてください\n"

else :
  text="ふざけないでください！\n"
print(comment)
print(cpu)
print(text)
