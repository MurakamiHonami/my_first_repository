import random

tiles=[]
tiles_type=""
for n in range(4):
    for i in range(3):
        tiles_type = ["萬", "筒", "索"][i]
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
ji_tile=["東", "南", "西", "北", "白", "発", "中"]
remove_tiles=[]

def tile_sort(tile):
    sort_tehai=[]
    num=[]
    for pai in tile:
        if "萬" in pai:
            num.append(pai)
    sort_tehai+=sorted(num)
    num=[]
    for pai in tile:
        if "筒" in pai:
            num.append(pai)
    sort_tehai+=sorted(num)
    num=[]
    for pai in tile:
        if "索" in pai:
            num.append(pai)
    sort_tehai+=sorted(num)
    num=[]
    for pai in tile:
        if pai in ji19_tiles:
           num.append(pai)
    sort_tehai+=sorted(num)
    return sort_tehai

def tsumo(tile):
    tumo=""
    tumo=random.choice(tile)
    tile.remove(tumo)
    return tumo


def shuntsu_cnt(tehai):
    suits = ['m', 'p', 's']
    shuntsu =0
    tehai2=tehai
    

    for suit in suits:
        suit_tiles = sorted([tile for tile in tehai2 if len(tile) >= 2 and tile[1] == suit])
        numbers = [int(tile[0]) for tile in tehai2 if len(tile) == 2 and tile[1] == suit]
        i=0
        while i<len(numbers)-2:
            if numbers[i+1]==numbers[i]+1 and numbers[i+2]==numbers[i]+2:
                t1, t2, t3 = f'{numbers[i]}{suit}', f'{numbers[i+1]}{suit}', f'{numbers[i+2]}{suit}'

                tehai2.remove(t1)
                tehai2.remove(t2)
                tehai2.remove(t3)
                shuntsu += 1
                suit_tiles = sorted([tile for tile in tehai2 if len(tile) >= 2 and tile[1] == suit])
                numbers = [int(tile[0]) for tile in tehai2 if len(tile) == 2 and tile[1] == suit]
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
    shuntsu,tehai = shuntsu_cnt(hand[:])
    kotsu,tehai2=kotsu_cnt(tehai[:])
    toi,tehai3=toitsu_cnt(tehai2[:])
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
    for ji in ji_tile:
                if ji in tehai:
                    return False
    suits=[]
    for tile in tehai:
        if tile[1] in suits:
            suits.append(tile[1])
        else:
            return False
    return len(suits)==1

def is_ittsu(tehai):
    suits = ['m', 'p', 's']
    for suit in suits:
        numbers=[int(tile[0]) for tile in tehai if tile[1]==suit]
        cnt=0
        if len(numbers)==9:
            for i in range(1,10):
                if f"{i}{suit}" in tehai:
                    cnt+=1
            if cnt==9:
                return True
    return False

def is_honitsu(tehai):
    for tile in ji_tile:
        if tile in tehai:
            tehai.remove(tile)
    suits = ['m', 'p', 's']
    for suit in suits:
        if all(len(tile)==2 and tile[1] == suit for tile in tehai):
                return True
    return False

def yaku_judge(tehai):
        if is_chinitsu(tehai[:]):
            print("清一色")
        elif is_honro(tehai[:]):
            print("混老頭")
        if is_honitsu(tehai[:]):
            print("混一色")
        if is_ittsu(tehai[:]):
            print("一気通貫")
        if is_tanyao(tehai[:]):
            print("タンヤオ")

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

