#気温に関するデータの読み取り
with open("weather.txt","r",encoding="utf-8") as f:
    weatherlist=[]
    cnt=0
    total=0.0
    for i in range(3):
        lines=f.readline()
        date,temp=lines.strip().split(",")
        weather=float(temp)
        total+=weather
        cnt+=1
        weatherlist.append((date,weather))

avg=total/float(cnt)
print(f"平均気温:{avg}度")
weatherlist.sort(key=lambda x: (-x[1],x[0]))
for i,(date,weather) in enumerate(weatherlist,start=1):
    print(f"{i}番目に気温が高い日は {date} の {weather}度")

weatherlist.sort(key=lambda x: (x[1],x[0]))
for i,(date,weather) in enumerate(weatherlist,start=1):
    print(f"{i}番目に気温が低いのは {date} の {weather}度")