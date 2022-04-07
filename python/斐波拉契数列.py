#斐波拉契数列（两个元素的总和确定了下一个数）
'''
a,b=0,1#确定a,b的初始值
while b<10:#设置b值的范围
    print(b,end=',')#关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
    a,b=b,a+b#创建关系表达式
'''
#print() sep 参数使用：
'''
a=10;b=20;c=30
print(a,b,c,sep='|')
'''
#使用递归方式求斐波纳契数列
'''
n=int(input('请输入一个整数：'))
def fab(n):
    if n<1:
        print('输入有误！')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)
print(fab(n))
'''
#使用列表记录n-1项，可以很大程度上减少重复计算量.利用字典记录也可以实现相同运算.
'''
n=int(input('请输入一个整数：'))
def fab(n):
    if n<1:
        print('输入有误！')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)
result=[]
for i in range(1,n+1):
    result.append(fab(i))
print(result)

n=int(input('请输入一个整数：'))
dic={0:0,1:1}
def fib(n):
    if n in dic:
        return dic[n]
    else:
         temp=fib(n-1)+fib(n-2)
         dic[n]=temp
         return temp
for i in range(n):
    print(fib(i+1),end='')
'''
# 非递归算法求解第n项数斐波那契数列
'''
a,b,i=0,1,0
result=[]
n=int(input('输入一个大于0的整数：'))
while i<n:
    result.append(b)
    a,b=b,a+b
    i+=1
print(result[n-1])
'''
#关于递归和两个变量计算斐波那契
'''
import time
#计算递归斐波那契时间消耗
n=int(input('请输入一个整数：'))
start=time.time()
def fab(n):
    if n<1:
        print('输入有误！')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)
print(fab(n))
end=time.time()
print('运行时间：%.2f秒'%(end-start))
#计算两个变量时间消耗
start=time.time()
a,b=0,1
cn=1
while cn<n:
    a,b=b,a+b
    cn+=1
print(b)
end=time.time()
print('运行时间：%.2f秒'%(end-start))
'''
#尾递归算法实现
'''
import time
n=int(input('请输入一个整数：'))
a=0
b=1
start=time.time()
def F(n,a,b):
    if n==0:
        return a
    return F(n-1,b,a+b)
print(F(n,a,b))
end=time.time()
print('运行时间：%.2f秒'%(end-start))
'''
#使用input函数来限定函数的最大值
'''
maxx=int(input('斐波拉契数列的最大值（忽略第一个数字0）:'))
a,b=0,1
while(b<=maxx):
    print(b,end=',')
    a,b=b,a+b
'''
#限制斐波拉契数列的数量
'''
num=int(input('斐波拉契数列的数量（忽略第一个数字0）'))
a,b=0,1
while(num>0):
    print(b,end=',')
    a,b=b,a+b
    num=num-1
'''
#利用无限循环函数可以让这个程序无限打印斐波那契数列的值
'''
a,b,c=0,1,1
while(c==1):
    print(b,end=',')
    a,b=b,a+b
'''