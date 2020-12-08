#循环结构
'''
#1~100求和
运算符加法赋值c += a   即为 c = c+a

sum = 0
for i in range(1,101):
    sum += i
print(sum)
'''

'''
99乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d" % (i,j,i*j),end ="\t")
    print()
'''

'''
判断一个正整数是不是素数
素数仅可被1和自己整除的整数

from math import sqrt
num = int(input("输入一个正整数:"))
#取目标值的平方根为中间数
mid = int(sqrt(num))
is_prime = True
for x in range(2,mid+1):
    if num % x == 0 :
        is_prime = False
        break

if is_prime and num != 1:
     print("%d是素数" % num)
else:
    print("%d不是素数" % num)
'''
'''
练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。

x = int(input("x="))
y = int(input("y="))
#取值从大到小递减，故取模为0，当前值则为最大公约数
for f in range(x,0,-1):
    if x % f == 0 and y % f ==0:
        print("%d和%d的最大公约数的%d" % (x, y, f))
        print("%d和%d的最小公倍数的%d" % (x, y, x*y//f))
        break
'''

'''
练习3：打印如下所示的三角形图案

row = int(input("输入行数："))
#几行打印几个*
for i in range(row):
    for j in range(i + 1):
        print('*',end="")
    print()

#每行打印*和空格数量相等，取差值
for i in range(row):
    for j in range(row):
        if j<row -i -1:
            print(" ",end="")
        else:
            print("*",end="")
    print()
#每行打印的*和空格数量相等 *为奇数每行*的数量为（2*row-1）；空格数量为
for i in range(row):
    for j in range(row -i -1):
        print(" ",end="")
    for j in range(2*i +1):
        print("*",end="")
    print()
'''

