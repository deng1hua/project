#最基础的条件判断
'''
a=1
b=2
if a>b:#判断a是否大于b,如果大于输出true，否则输出false
    print('true')
else:
    print('false')
'''
#if...elif...else,elif是在if...else的条件基础上，再加一个条件
'''
import random
num=random.randint(1,100)
print(num)
inpu1=int(input('number:'))
while True:
    if inpu1 > num:
        print('too big')
    elif inpu1 == num:
        print('true')
        break
    else:
        print('too small')
'''
#条件判断的多重嵌套
'''
a=1
b=2
if a<b:#首先判断a是否小于b
    if a+b==4:#然后判断a和b的和是否等于4
        print('true')
    else:
        print('false')
else:
    print('a大于b了！')
'''
#奇偶数分离
'''
numbers = [12,37,5,42,8,3]
odd=[]#存放奇数的列表
even=[]#存放偶数的列表
while len(numbers)>0:
    number=numbers.pop()
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)
'''
#互不相同且无重复的三位数
'''
d=[]
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a!=b) and (b!=c) and (a!=c):
                d.append([a,b,c])
print('多少个:%s'%len(d))
print(d)
'''
#判断某年某月某日是该年的第几天
'''
year=int(input('year:\n'))#输入年
month=int(input('month:\n'))#输入月
day=int(input('day:\n'))#输入日，在引号内都加入换行符，实现换行输入
months=[0,31,59,90,120,151,181,212,243,273,304,334]#定义一个每个月的天数列表months
if 0<month<=12:#判断输入的月数是否在大于0小于等于12范围内
    sum=months[month-1]#查找输入的月在months列表中对应的天数sum
else:#输入的日期有误
    print('date error')
sum+=day#日期变量递增
leap=0#定义一个leap=0的变量初始值
if (year%400==0) or ((year%4==0) and (year%100!=0)):#判断输入的年是否能被400或者4整除，但不能被100整除
    leap=1#leap变量值由0变为1
if (leap==1) and (month>2):#判断leap的变量值为1，输入的月份大于2
    sum+=1#sum变量递增加等于1
print('it is the %dth day'%sum)#输出sum是这个日期在这一年的第几天
'''
#if表达式
'''
var1=100
if var1:
    print('1 - if表达式为true')
    print(var1)
var2=0
if var2:
    print('2 - if表达式为true')#0的真值是false,1的真值是true
    print(var2)
print('goodbye!')
'''
#狗的年龄判断
'''
age=int(input('狗的年龄：'))
print(" ")
if age<=0:
    print('sorry,i do not know')
elif age==1:
    print('相当于14岁的人')
elif age==2:
    print('相当于22岁的人')
elif age>2:
    human=22+(age-2)*5
    print('对应人类年龄：%d'%human)

input('点击enter键退出')
'''
#判断一个数是否能被2和3整除
'''
num=int(input('number:'))
if num%2==0:
    if num%3==0:
        print('%d能被2和3整除'%num)
    else:
        print('%d能被2整除，不能被3整除'%num)
else:
    if num%3==0:
        print('%d不能被2整除，但能被3整除'%num)
    else:
        print('%d不能被2和3整除'%num)
'''
#在0-100内随机取一个数x，0-200随机取一个数y，判断这两个数的大小关系
'''
import random
x=random.choice(range(100))
y=random.choice(range(200))
if x>y:
    print('x:',x)
elif x==y:
    print('x+y:',x+y)
else:
    print('y:',y)
'''
#BMI的计算
'''
print('--欢迎使用BMI程序--')
name=input('请输入您的姓名：')
height=eval(input('请输入您的身高(m):'))#eval函数将字符串对象转换为具体的对象，比如字符串元组直接转换为元组
weight=eval(input('请输入您的体重(kg):'))
gender=input('请输入您的性别(F/M):')
BMI=float(float(weight)/float(height)**2)
if BMI<=18.4:
    print('姓名：',name,'身体状态：偏瘦')
elif BMI<=23.9:
    print('姓名：',name,'身体状态：正常')
elif BMI<=27.9:
    print('姓名：',name,'身体状态：超重')
elif BMI>=28:
    print('姓名：',name,'身体状态：肥胖')
import time
nowtime=time.asctime(time.localtime(time.time()))
if gender=='F':
    print(f'感谢{name}女士，在{nowtime}使用本程序')
elif gender=='M':
    print(f'感谢{name}先生，在{nowtime}使用本程序')
else:
    print('请输入正确的性别：')
'''
#选择结构中的单分支结构(只有一个if条件)
'''
money=10000
a=int(input('请输入取款金额:'))
if money>=a:
    money=money-a
    print('取款成功，余额%d元'%money)
'''
#选择结构中的双分支结构(有if、else两个条件)
'''
num=int(input('请输入一个整数：'))
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')
'''
#选择机构中的多分支结构(有if、elif、else多个条件)
'''
score=int(input('请输入您的分数：'))
if 90<=score<=100:
    print('A级，优秀')
elif 80<=score<90:
    print('B级，中有')
elif 70<=score<80:
    print('C级，良好')
elif 60<=score<70:
    print('D级，及格')
else:
    print('E级，极差')
'''
#if嵌套
'''
answer=input('你是会员吗：(y/n)?')
money=int(input('一共花费多少钱？'))
if answer=='y':
    if money>=200:
        print('八折优惠，请支付：',money*0.8)
    elif 100<=money<200:
        print('九折优惠，请支付：',money*0.9)
    else:
        print('没有优惠，请支付：',money)
else:
    if money>=200:
        print('8.5折优惠，请支付：',money*0.85)
    else:
        print('没有优惠，请支付：',money)
'''
#使用条件表达式比较两个数的大小
'''
a=int(input('number1:'))
b=int(input('number2:'))
print(str(a)+'大于等于'+str(b) if a>=b else str(a)+'小于'+str(b))#if的结果 if 条件 else else的结果
'''
#




