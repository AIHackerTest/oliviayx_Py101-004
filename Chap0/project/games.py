# coding=utf-8
import random
num = random.randint(1, 20)
your_num = int( input("请输入你的数字>>>") )
#print (num)
i = 0
if 0 <= your_num <= 20:
    while i<=10:
        if your_num < num:
            print ("你的数字小了")
        elif your_num > num:
            print ("你的数字大了")
        else:
            print ("你猜对了")
            break
        your_num = int( input("请输入你的数字>>>") )
        i+=1
    else:
        print ("你猜的次数太多了，游戏结束。")
else:
    print ("你猜的数字不在范围内，游戏结束。")
