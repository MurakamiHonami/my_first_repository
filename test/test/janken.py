import random
janken_list = ["グー","チョキ","パー"]
def janken(you):
    i = random.choice(janken_list)
    print(i)
    if i == you:
        return "あいこ"
    elif you == "グー" and i == "チョキ" or you == "チョキ" and i == "パー" or you == "パー" and i == "グー":
        return "勝ち" 
    else:
        return "負け"
    
you = input("じゃんけんを出してください(グー/チョキ/パー)")
result = janken(you)
while result == "あいこ":
    you = input("あいこでしょ(グー/チョキ/パー)")
    result = janken(you)
print(result)