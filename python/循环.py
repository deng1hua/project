'''
#while循环
i=0#设置初始值
while i<3:#循环条件
    print(i)
    i+=1#变量递增，如果没有这个，会一直循环输出0
#for...in...循环
for i in range(3):
    print(i)
'''
#不需要使用自定义变量，可以写成 _
'''
for _ in range(3):
    print('love')
'''

'''
for i in '1234':
    print(i)
    '''
#练习
'''
#设置正确密码，最多输入三次
i=0
while i<3:
    i+=1
    num=input('password:')
    if num=='888':
        print('true')
        break
    else:
        print('false')
'''
'''
#输出一个三行四列的矩形
i=0
while i<3:#定义行数
    j=0
    while j<4:#定义列数
        print('*',end='\t')
        j+=1
    print()
    i+=1
'''
#输出一个直角三角形
'''
i=0
while i<5:
    j=0
    while j<i+1:
        print('*',end='\t')
        j+=1
    print()
    i+=1
'''
#输出一个倒立的直角三角形
'''
i=0
while i<5:
    j=0
    while j<5-i:
        print('*',end='\t')
        j+=1
    print()
    i+=1
'''
#九九乘法表
'''
i=0
while i<9:
    i+=1
    j=0
    while j<i:
        j+=1
        print(f'{i}*{j}={i*j}',end='\t')
    print()
'''
#有1、2、3、4四个数字，它们可以组成多少组不同的三位数，分别是什么？
'''
count=0
i=1
while i<5:
    j=1
    while j<5:
        k=1
        while k<5:
            if i!=j and j!=k and i!=k:
                print(i*100+j*10+k)
                count+=1
            k+=1
        j+=1
    i+=1
print(count)
'''
#输出1到100的所有偶数，并求和
'''
sum=0
i=1
while i<=100:
    i+=1
    if i%2==0:
        sum+=i
        print(i)
print(sum)
'''
#100到999的水仙花数
'''
i=100
while i<1000:
    a=i//100
    b=i//10%10
    c=i%10
    if i==a**3+b**3+c**3:
        print(i)
    i+=1
'''
#输出2到100的所有质数
'''
i=2
while i<100:
    flag=1
    j=2
    while j<i:
        if i%j==0:
            flag=0
        j+=1
    if flag:
        print(i,end='\t')
    i+=1
'''
#输入一个数，判断是否为质数
'''
num=int(input('number:'))
flag=1
i=2
while i<num:
    if num%i==0:
        flag=0
    i+=1
if flag:
    print(i,'是质数')
else:
    print(i,'不是质数')
'''
#有一个四位数，满足abcd*4=dcba
'''
i=1000
while i<2500:
    num=i*4
    a=i//1000
    b=i%1000//100
    c=i%1000%100//10
    d=i%10
    e=num//1000
    f=num%1000//100
    g=num%1000%100//10
    h=num%10
    if a==h and b==g and c==f and d==e:
        print(i)
    i+=1
'''
#求阶乘
'''
num=int(input('number:')) #输入一个数num
res=1 #定义一个变量res的值为1
for i in range(1,num+1): #遍历1到num+1
    res*=i #阶乘等于res*=i
print('%d的阶乘为：%d'%(num,res))
'''
#求最大公约数和最小公倍数
'''
num1=int(input('number:')) #输入num1
num2=int(input('number:')) #输入num2
min_num=min(num1,num2) #求两个数中最小的数
for i in range(1,min_num+1): #遍历1到最小的数+1
    if num1%i==0 and num2%i==0: #如果两个数同时除以一个数，余数为0
        max_commer=i #最大公约数就是那个数
min_commer=(num1*num2)/max_commer #最小公倍数等于两个数相乘除以最大公约数
print('%d和%d的最大公约数是：%d'%(num1,num2,max_commer))
print('%d和%d的最小公倍数是：%d'%(num1,num2,min_commer))
'''
#死循环
#while True: #条件为true
 #   print('hello')
#计算1到100的和
'''
sum=0
i=1
while i<=100:
    sum+=i
    i+=1
print(sum)
'''
#向左直角三角形
'''
i=1
while i<=5:
    j=1
    while j<=5-i:
        print(' ',end='')
        j+=1
    while (j>5-i and j<=5):
        print('*',end='')
        j+=1
    print()
    i+=1
'''
#倒立向左直角三角形
'''
i=1
while i<=5:
    j=1
    while j<i:
        print(' ',end='')
        j+=1
    while j>=i and j<=5:
        print('*',end='')
        j+=1
    print()
    i+=1
'''
#猜数字游戏，利用random模块从1到100中随机输出一个数，输入一个数判断是大于、小于还是等于这个数，等于这个数就结束循环，只有5次输入机会
'''
import random
num=random.randint(1,100)
print(num)
i=1
while i<=5:
    ber=int(input('number:'))
    if ber>num:
        print('number is too big')
    elif ber==num:
        print('great true!')
        break
    else:
        print('number is too small')
    i+=1
'''
#原九九乘法表逆时针输出
'''
for i in range(9,0,-1):
    for j in range(1,i):
        print('\t',end='')
    for k in range(i,10):
        print('%d*%d=%d'%(i,k,k*i),end='\t')
    print()
'''
#








