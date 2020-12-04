#判断分支

'''
#练习1：英制单位英寸与公制单位厘米互换
#1英寸=2.54厘米  拆分为值和单位
value = float(input("请输入长度："))
unit = str(input("请输入单位："))
#判断单位为 英寸或厘米
if unit == "英寸" or unit == "inch":
    print("%f英寸 = %f厘米" % (value,value*2.54))
elif unit == "厘米" or unit == "cm":
    print("%f厘米 = %f英寸" % (value,value/2.54))
else:
    print("请输入有效单位")
'''

'''
#练习2：百分制成绩转换为等级制成绩
要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。

#根据分数分段，判断输出成绩等级
grade = float(input("请输入成绩："))
if grade >= 90:
    print("成绩为A")
elif grade >= 80 :
    print("成绩为B")
elif grade >= 70 :
    print("成绩为C")
elif grade >= 60 :
    print("成绩为D")
else: 
    print("成绩为E")
'''

'''
#练习3：输入三条边长，如果能构成三角形就计算周长和面积。
套用海伦公式 S*S = p(p-a)(p-b)(p-c)   p = (a+b+c)/2 
运算符 ** 代表乘方;* 代表乘法
三角形判定  a+b>c  a-b<c

import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a+b>c and a+c>b and b+c>a:
    print("周长：%s" % (a+b+c))
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    #area =  (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("面积=%s" % s)
else:
    print("不是三角形")
'''



