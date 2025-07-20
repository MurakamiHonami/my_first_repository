import random

tiles=[]
tiles_type=""
for n in range(4):
    for i in range(3):
        tiles_type = ["m", "p", "s"][i]
        for j in range(1,10):
            if n==0 and j==5:
                tiles.append(str(j)+tiles_type+"*")
            else:
                tiles.append(str(j)+tiles_type)
for i in range(4):
    tiles+=["東","南","西","北","白","発","中"]

tiles_copy=tiles
tehai = random.sample(tiles, 13)
for i in tehai:
    tiles.remove(i)

ji19_tiles = ["東", "南", "西", "北", "白", "発", "中","1m","9m","1p","9p","1s","9s"]
ji_tiles=["東", "南", "西", "北", "白", "発", "中"]
remove_tiles=[]

def tile_sort(tile):
    sort_tehai=[]
    num=[]
    for pai in tile:
        if len(pai)==2 and "m" == pai[1]:
            num.append(pai)
    sort_tehai+=sorted(num)
    num=[]
    for pai in tile:
        if len(pai)==2 and "p" == pai[1]:
            num.append(pai)
    sort_tehai+=sorted(num)
    num=[]
    for pai in tile:
        if len(pai)==2 and "s" == pai[1]:
            num.append(pai)
    sort_tehai+=sorted(num)
    num=[]
    for pai in tile:
        if pai in ji_tiles:
           num.append(pai)
    sort_tehai+=sorted(num)
    return sort_tehai

def tsumo(tile):
    tumo=""
    tumo=random.choice(tile)
    tile.remove(tumo)
    return tumo


def shuntsu_cnt(tehai2):
    suits = ['m', 'p', 's']
    shuntsu =0
    tehai_copy=tehai2
    for suit in suits:
        suit_tiles = sorted([tile for tile in tehai_copy if len(tile) >= 2 and tile[1] == suit])
        numbers = [int(tile[0]) for tile in tehai_copy if len(tile) == 2 and tile[1] == suit]
        i=0
        while i<len(numbers)-2:
            if numbers[i]+1 in numbers and numbers[i]+2 in numbers:
                t1, t2, t3 = f'{numbers[i]}{suit}', f'{numbers[i]+1}{suit}', f'{numbers[i]+2}{suit}'

                tehai_copy.remove(t1)
                tehai_copy.remove(t2)
                tehai_copy.remove(t3)
                shuntsu += 1
                suit_tiles = sorted([tile for tile in tehai_copy if len(tile) >= 2 and tile[1] == suit])
                numbers = [int(tile[0]) for tile in tehai_copy if len(tile) == 2 and tile[1] == suit]
                i = 0
            else:
                i+=1
    return shuntsu,tehai2

def kotsu_cnt(tehai):
    kotsu=0
    j=0
    while j<len(tehai)-2:
        if tehai[j]==tehai[j+1] and tehai[j+1]==tehai[j+2]:
            kotsu+=1
            tehai.remove(tehai[j+2])
            tehai.remove(tehai[j+1])
            tehai.remove(tehai[j])
            j=0
        else:
            j+=1
    return kotsu,tehai
def toitsu_cnt(tehai):
    toi=0
    j=0
    while j<len(tehai)-1:
        if tehai[j]==tehai[j+1]:
            toi+=1
            tehai.remove(tehai[j+1])
            tehai.remove(tehai[j])
            j=0
        else:
            j+=1
    return toi,tehai
def hora(hand):
    shuntsu,tehai2 = shuntsu_cnt(hand[:])
    # print(shuntsu,tehai2)
    kotsu,tehai2=kotsu_cnt(tehai2[:])
    # print(kotsu,tehai2)
    toi,tehai2=toitsu_cnt(tehai2[:])
    # print(toi,tehai2)
    if shuntsu+kotsu==4 and toi==1:
        return True
    else:
        return False

def rare_yaku_judge(tehai):
    cnt=0
    for tile in ji19_tiles:
        if tile in tehai:
            cnt+=1
    toi,tehai=toitsu_cnt(tehai)
    if toi==7:
        print("七対子")
        return True
    if cnt==13 and toi ==1:     
        print("国士無双")
        return True
    
def is_tanyao(tehai):
    tan=True
    for tile in tehai:
        if tile in ji19_tiles:
            tan=False
    return tan

def is_honro(tehai):
    for tile in tehai:
        if len(tile)==2 and tile[0] in "2345678":
            return False
    return True

def is_chinitsu(tehai):
    suits = ['m', 'p', 's']
    for ji in ji_tiles:
        for tile in tehai:
            if ji==tile:
                return False
    for suit in suits:
        cnt=0
        for tile in tehai:
            if tile[1] == suit:
                cnt+=1
        if cnt==len(tehai):
            return True
    return False

def is_honitsu(tehai):
    cnt=0
    remove=[]
    i=0
    for tile in tehai:
        for ji in ji_tiles:
            if ji==tile:
                cnt+=1
                remove.append(ji)
        i+=1
    if cnt==0:
        return False
    for r in remove:
       tehai.remove(r)
    suits = ['m', 'p', 's']
    for suit in suits:
        cnt=0
        for tile in tehai:
            if tile[1]==suit:
                cnt+=1
        if len(tehai)==cnt:
            return True
    return False

def is_ittsu(tehai):
    suits = ['m', 'p', 's']
    for suit in suits:
        cnt=0
        for i in range(1,10):
            if f"{i}{suit}" in tehai:
                cnt+=1
        if cnt==9:
            return True
    return False

def is_sanshoku(tehai):
    suits=['m','p','s']
    for i in range(1,8):
            if f"{i}{suits[0]}" in tehai and f"{i+1}{suits[0]}" in tehai and f"{i+2}{suits[0]}" in tehai:
                if f"{i}{suits[1]}" in tehai and f"{i+1}{suits[1]}" in tehai and f"{i+2}{suits[1]}" in tehai:
                    if f"{i}{suits[2]}" in tehai and f"{i+1}{suits[2]}" in tehai and f"{i+2}{suits[2]}" in tehai:
                        return True
    return False

def yaku_judge(tehai):
        if is_chinitsu(tehai[:]):
            print("清一色")
        if is_honitsu(tehai[:]):
            print("混一色")
        if is_honro(tehai[:]):
            print("混老頭")
        if is_ittsu(tehai[:]):
            print("一気通貫")
        if is_sanshoku(tehai[:]):
            print("三色同順")
        if is_tanyao(tehai[:]):
            print("タンヤオ")

hand = ["1p","2p","3p","1m","東","東","2m","3m","1s","2s","3s","8p","8p","8p"]
hand = tile_sort(hand)
print(hand)
if hora(hand[:]) or rare_yaku_judge(hand[:]):
    yaku_judge(hand[:])
    print("和了")

wanpai=random.sample(tiles, 14)
for i in wanpai:
    tiles.remove(i)

bahuu={0:"東",1:"南"}
jihuu={0:"東",1:"南",2:"西",3:"北"}
jihuu_index=random.randint(0,3)
tehai_sorted = tile_sort(tehai)

for ba in range(2):
        for j in range(4):
            cnt=0
            dora=random.choice(wanpai)
            while len(tiles)/4 > 0:
                cnt+=1
                print(f"{bahuu[ba]}{j+1}局{cnt}巡目,自風は{jihuu[jihuu_index]},ドラは{dora}です")
                if cnt>1:
                    print("捨て牌:"," ".join(remove_tiles))
                print("手牌:", " ".join(tehai_sorted))
                input("ツモ:Enter")
                tumo = tsumo(tiles)
                print("手牌:", " ".join(tehai_sorted),tumo)
                tehai_sorted.append(tumo)
                if hora(tehai_sorted[:]) or rare_yaku_judge(tehai_sorted[:]):
                    yaku_judge(tehai_sorted[:])
                    print("和了!")
                    break
                da=int(input("打牌(0～13):"))
                remove_tiles.append(tehai_sorted[da])
                tehai_sorted.remove(tehai_sorted[da])
                tehai_sorted = tile_sort(tehai_sorted)
            tiles=tiles_copy
        jihuu_index=(jihuu_index+1)%4

