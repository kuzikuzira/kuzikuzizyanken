import random
print("じゃんけんしようぜ\n")
print("ぐー、ちょき、ぱーのどれかを入力してください\n")

hand=input()

if hand=="ぐー":
  print("ぐーをだしましたか…\n")

elif hand=="ぱー":
  print("ぱーをだしたな！\n")

else :
  print("ぐーかぱーをだしなさい！\n")

num=random.randint(0,2)
hai=["ぐー","ちょき","ぱー"]
print(hai[num])

cpu=hai[num]

while hand==cpu:
  print("あいこだ！もう一度！\n")
  hand=input()

  num=random.randint(0,2)
  hai=["ぐー","ちょき","ぱー"]
  print(hai[num])
  cpu=hai[num]

if hand=="ぐー":
  if cpu=="ちょき":
    print("人生の勝者！\n")
  elif cpu=="ぱー":
    print("負け犬が！何で負けたか明日までに考えといてください\n")

if hand=="ちょき":
  if cpu=="ぱー":
    print("人生の勝者！\n")
  elif cpu=="ぐー":
    print("負け犬が！何で負けたか明日までに考えといてください\n")

if hand=="ぱー":
  if cpu=="ぐー":
    print("人生の勝者！\n")
  elif cpu=="ちょき":
    print("負け犬が！何で負けたか明日までに考えといてください\n")



