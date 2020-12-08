#函数和模块的使用
'''
练习1：实现计算求最大公约数和最小公倍数的函数。

def gcd(x,y):
    #求最大公约数 大数在前
    (x,y) = (y,x) if x > y else (x,y)
    for f in range(x,0,-1):
        if x % f == 0 and y % f ==0:
            return f

def lcm(x,y):
    #求最小公倍数
    return x*y // gcd(x,y)
'''

'''
练习2：实现判断一个数是不是回文数的函数。
'''
def is_palindrome(num):
    temp = num
    reserve_num = 0
    while temp > 0 :
        reserve_num = reserve_num * 10 + temp % 10
        temp //= 10
    return reserve_num == num

#is_palindrome(121)


'''
练习3：实现判断一个数是不是素数的函数。
'''
from math import sqrt
def prime(num):
    for factor in range(2,int(sqrt(num)+1)):
        if num % factor ==0 :
            return False
    return True if num != 1 else False

#prime(29)

'''
练习4：写一个程序判断输入的正整数是不是回文素数。

if __name__ == '__main__':
    num = int(input("请输入正整数："))
    if is_palindrome(num) and prime(num):
        print("%d是回文素数" % num)
'''

