#语言元素
#day2作业
'''
#1.华氏温度转为摄氏温度
# 华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$
hua=float(input("输入华氏温度："))
tem=(hua-32)/1.8
#打印结果，%f为浮点占位符
print("%f 华氏度 = %f 摄氏度" % (hua,tem))
#%f浮点占位   %.1f 浮点保留1位小数
print('%.1f华氏度 = %.1f摄氏度' % (hua, tem))
#f为浮点，{用变量替换占位符}
print(f'{hua:.1f}华氏度 = {tem:.1f}摄氏度')
'''

'''
# #2.输入圆的半径计算计算周长和面积
# #C=2pai R   S=PAI r*r
# r=float(input("输入半径："))
# c=2*3.14*r
# s=3.14*r*r
# print(f'圆的周长是{c:.1f};原的面积是{s:.1f}')
# print("圆的周长是%.1f；圆的面积是%.1f" % (c,s))
'''

#3.输入年份判断是不是闰年
year = int(input("请输入年份："))
#布尔值判断是否为闰年
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(str(year)+str(is_leap)+"闰年")

#print(f'{year:d} 是闰年 {is_leap:s}')