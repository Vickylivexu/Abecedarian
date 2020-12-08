#构造程序逻辑
'''
1.寻找水仙花数。

说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数
该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。

#确认数字范围  3位数
for num in range(100,1000):
    low = num % 10  #个位数
    mid = num // 10 % 10 #十位数
    high = num // 100   #百位数
    if num ==low ** 3 + mid ** 3 + high ** 3:
        print(num)
'''

'''
正整数反转，例如：将12345变成54321

num = int(input("num = "))
reversed_num = 0    #声明变量reversed_num 反转数
while num >0:
    reversed_num = reversed_num * 10 + num % 10 #反转数十位以上转换+个位数
    num //= 10  #位数缩减运算
print(reversed_num)
'''

'''
2.百钱百鸡问题。
说明：百钱百鸡是我国古代数学家[张丘建](https://baike.baidu.com/item/%E5%BC%A0%E4%B8%98%E5%BB%BA/10246238)
在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，
问公鸡、母鸡、小鸡各有多少只？

#有多组解
for gong in range (1,20):
    for mu in range (1,33):
        xiao = 100-gong-mu
        if gong * 5 + mu * 3 + xiao / 3 ==100:
            print(gong,mu,xiao)
'''

'''
3.CRAPS赌博游戏。

说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。

from random import randint

money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜')
            money += debt
            needs_go_on = False

print('你破产了, 游戏结束!')
'''

'''
生成斐波那契数列的前20个数。

说明：斐波那契数列（Fibonacci sequence），又称黄金分割数列，是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）
在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，所以这个数列也被戏称为"兔子数列"。
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。

a = 0
b = 1
for _ in range(20): #执行20次
    a , b = b , a+b
    print(a,end=" ")
'''

'''
找出10000以内的完美数。

说明：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。

import math
for num in range (1,10000):
    result = 0
    for factor in range(1,int(math.sqrt(num))+1):   #限定约数范围
        if num % factor ==0:
            result += factor
            if factor >1 and num // factor != factor:
                result += num //factor
    if result == num:
        print(num)
'''

'''
输出100以内所有的素数。

说明：素数指的是只能被1和自身整除的正整数（不包括1）。
'''
from math import sqrt
for num in range(2,100):
    is_prime = True
    for factor in range(2,int(sqrt(num))+1):
        if num % factor == 0 :
            is_prime = False
            break
    if is_prime:
        print(num ,end=" ")
