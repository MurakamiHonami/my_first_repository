import random

def tiles_update(tiles_data):
    # 同じものを４つ作る
    for tiles_cnt in range(TILES_CNT):
        # 牌の種類ごとに作る
        for tiles_type_cnt in range(TILES_TYPE_CNT):
            # 牌の目を1から10で生成
            for tiles_number in range(1,10):
                tiles_keep = str(tiles_number) + tiles_type[tiles_type_cnt]
                # 牌のうち1つの5の目を赤ドラにする
                if tiles_cnt == 0 and tiles_number == 5: tiles_keep += "*"
                tiles_data.append(tiles_keep)
    for i in range(4):
        tiles_data+=["東","南","西","北","白","発","中"]
    
    return tiles_data

# 牌のソート
def tile_sort(tehai,tiles_type):

    # アフター
    character_keep = []
    sort_tehai=[]
    # マンズ、ピンズ、ソウズの順にソート
    for tiles_type_cnt in range(TILES_TYPE_CNT):
        sort_tehai_type=[]
        for pai in tehai:
            # 数牌なら
            if pai[0].isdigit():
                    if pai[1] == tiles_type[tiles_type_cnt]: sort_tehai_type.append(pai)
            # 字牌なら
            # 最後の繰り返し処理で通るようにする(字牌数*3追加してしまうため)
            elif tiles_type_cnt == 2:
                character_keep.append(pai)

            # 同じ種類間で数字のソート
            sort_tehai_type.sort()
        sort_tehai+=sort_tehai_type
    
    # 字牌を末尾に追加
    for character in character_keep:
        sort_tehai.append(character)
    
    return sort_tehai


def tsumo(tile):
    tumo=""
    tumo=random.choice(tile)
    tile.remove(tumo)
    return tumo


def shuntsu_cnt(tehai2):
    suits = ['m', 'p', 's']
    shuntsu =0
    tehai_copy=tehai2.copy()
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
    shuntsu,tehai2 = shuntsu_cnt(hand)
    # print(shuntsu,tehai2)
    kotsu,tehai3=kotsu_cnt(tehai2)
    # print(kotsu,tehai2)
    toi,tehai4=toitsu_cnt(tehai3)
    # print(toi,tehai2)
    if shuntsu+kotsu==4 and toi==1:
        return True
    else:
        return False


    
def is_tanyao(tehai):
    tan=True
    for tile in tehai:
        if tile in character_and_1or9_tiles:
            tan=False
    return tan

def is_honro(tehai):
    for tile in tehai:
        if len(tile)==2 and tile[0] in "2345678":
            return False
    return True

def is_chinitsu(tehai):
    suits = ['m', 'p', 's']
    for ji in character_tiles:
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
        for ji in character_tiles:
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


def rare_yaku_judge(tehai):
    cnt=0
    for tile in character_and_1or9_tiles:
        if tile in tehai:
            cnt+=1
    toi,tiles_data=toitsu_cnt(tehai[:])
    if toi==7:
        print("七対子")
        return True
    if cnt==13 and toi ==1:     
        print("国士無双")
        return True
   
def yaku_judge(tehai):
        if is_chinitsu(tehai):
            print("清一色")
        if is_honitsu(tehai):
            print("混一色")
        if is_honro(tehai):
            print("混老頭")
        if is_ittsu(tehai):
            print("一気通貫")
        if is_sanshoku(tehai):
            print("三色同順")
        if is_tanyao(tehai):
            print("タンヤオ")

#メインルーチン
# リフォーム後
tiles_data=[]    # 場に出る手牌
tiles_type = ["m", "p", "s"]    #牌の種類保持
TILES_CNT = 4  #1つの牌の個数
TILES_TYPE_CNT = 3 #マンズ、ピンズ、ソウズの3つの種類

# 牌の更新
tiles_data = tiles_update(tiles_data)


tiles_copy=tiles_data
tehai = random.sample(tiles_data, 13)
for i in tehai:
    tiles_data.remove(i)

character_and_1or9_tiles = ["東", "南", "西", "北", "白", "発", "中","1m","9m","1p","9p","1s","9s"]
character_tiles=["東", "南", "西", "北", "白", "発", "中"]
remove_tiles=[]


wanpai=random.sample(tiles_data, 14)
for i in wanpai:
    tiles_data.remove(i)

bahuu={0:"東",1:"南"}
jihuu={0:"東",1:"南",2:"西",3:"北"}
jihuu_index=random.randint(0,3)
tehai_sorted = tile_sort(tehai,tiles_type)
number=[f"{x}" for x in range(14)]

for ba in range(2):
        for j in range(4):
            cnt=0
            dora=random.choice(wanpai)
            while len(tiles_data)/4 > 0:
                if hora(tehai_sorted.copy()) or rare_yaku_judge(tehai_sorted.copy()):
                    yaku_judge(tehai_sorted.copy())
                    print("和了!")
                    exit()
                flg=True
                cnt+=1
                print(f"{bahuu[ba]}{j+1}局{cnt}巡目,自風は{jihuu[jihuu_index]},ドラは{dora}です")
                if cnt>1:
                    print("捨て牌:"," ".join(remove_tiles))
                print("手牌:", " ".join(tehai_sorted))
                input("ツモ:Enter")
                tumo = tsumo(tiles_data)
                tehai_sorted.append(tumo)
                tehai_sorted=tile_sort(tehai_sorted,tiles_type)
                print("手牌:", " ".join(tehai_sorted))
                print("    :  0  1  2  3  4  5  6  7  8  9  10  11  12  13")
                while flg:
                    da=input("打牌(0～13):")
                    if da in number:
                        da=int(da)
                        break
                    else:
                        print("入力が誤っています")
                remove_tiles.append(tehai_sorted[da])
                tehai_sorted.remove(tehai_sorted[da])
                tehai_sorted = tile_sort(tehai_sorted,tiles_type)
            tiles_data=tiles_copy
        jihuu_index=(jihuu_index+1)%4

