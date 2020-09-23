import math
import pandas as pd

ry = int(input("年利を入力してください(単位:%)")) #年利
rm = ((1+ ry/100)**(1/12)-1) #年利から月利を計算
rm_percent = rm*100
print("月利は" + str(rm_percent) + "%です")
ganpon = int(input("元本を入力してください。(単位:円)"))
year = int(input("運用年数を入力してください。(単位:年)"))
month = year*12
hikidashi = int(input("毎月引き出したい金額を入力してください(単位:円)"))
zandaka = ganpon

def kekka():
    global zandaka
    global rm
    global ganpon
    global hikidashi
    shuturyoku = []
    while(zandaka >0):
        zougen = (ganpon * (rm) - hikidashi)
        for i in range(month):
            zandaka = zandaka + zougen
        print("元本" +str(ganpon) +"円を" + "年利" +str(ry) + "%で運用した場合" +"毎月" + str(hikidashi) + "円引き出すと" +str(year)+ "年後に" +str(zandaka) +"円の残高です")
        if zandaka >0:
            zandaka = ganpon
            hikidashi = hikidashi + 1000
        shuturyoku.append("元本" +str(ganpon) +"円を" + "年利" +str(ry) + "%で運用した場合" +"毎月" + str(hikidashi) + "円引き出すと" +str(year)+ "年後に" +str(zandaka) +"円の残高です")
        print(shuturyoku)
    export_html = ''.join(shuturyoku)
    print(export_html)


kekka()