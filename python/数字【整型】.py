'''
#数字运算
a=1
b=2
#数字的加法运算
print(a+b)
#减法运算
print(a-b)
#乘法运算
print(a*b)
#幂运算
print(3**2)
#除法运算
print(a/b)
#除法运算取余数
a1=5
b1=2
print(a1%b1)
#除法取整除
print(a1//b1)
#比较运算
print(a==b)
print(a!=b)
#加减乘除幂混合运算[先算幂，再算乘除，最后算加减]
print(1+10-3*4/6**2)
'''

'''
#进制转换
n=100
print(bin(n))#n=100是十进制数，十进制转二进制
print(oct(n))#十进制转八进制
print(hex(n))#十进制转十六进制
'''

'''
#数字类型转换
n=100
print(float(n))#将整数n转换为浮点数
print(complex(n))#将整数n转换为复数
n1=3.3
print(int(n1))#将浮点数n1转换为整数
print(complex(n1))#将浮点数n1转为复数
print(complex(n,n1))#将n和n1转为复数
'''

'''
#数学函数
print(abs(-100))#返回数字的绝对值，正数还是正数，负数转为正数
print(max(11,25,2,39,15))#返回一个序列的最大值
print(min(11,25,2,39,15))#返回一个序列的最小值
print(round(3.14159,3))#返回一个浮点数的四舍五入值，第二个参数表示保留几位小数
'''

'''
#数学运算模块math
import math
print(math.pi)#返回圆周率Π
print(math.e)
print(math.ceil(4.1))#返回一个数的天花板数,只要小数部分大于0，整数就要加1
print(math.floor(4.99999))#返回一个数的地板数，直接输出浮点数的整数部分
print(math.exp(1))#返回e的1次幂
print(math.expm1(1))#返回e的1次幂减1
print(math.fabs(-12.3))#返回一个数的绝对值
print(math.log(100,10))#返回第二个数的二次幂等于100
print(math.log2(4))#返回以2为基底，4的对数
print(math.log10(100))#返回以10为基底，100的对数
print(math.modf(3.2))#返回浮点数的小数部分和整数部分，整数部分以浮点数表示
print(math.pow(2,3))#返回2的3次方的结果
print(math.sqrt(4))#返回4的平方根【2的平方是4，因此4的平方根是2】
'''

'''
#随机数函数
import random
print(random.choice(range(10)))#从0到10内随机输出一个整数
print(random.randrange(1,9,2))#从指定的1到9、步长为2范围内，随机输出一个整数
#指定了随机数生成器种子，两次调用random方法结果相同
random.seed(10)
print(random.random())#随机生成一个浮点数，它的范围在[0,1)内
random.seed(10)
print(random.random())
#未指定随机数生成器种子，两次结果不同
random.seed()
print(random.random())
random.seed()
print(random.random())
lst=[1,2,3,4,5]
random.shuffle(lst)#将列表序列随机排序
print(lst)
print(random.uniform(1,10))#从指定范围内随机生成一个浮点数
print(round(random.uniform(1,10),2))#先从指定范围内随机生成一个浮点数，然后使用round函数生成这个浮点数的四舍五入值，保留两位
'''

'''
#布尔值
n=1
print(bool(n))#整数非0为true
n=0
print(bool(n))#整数为0为false
l=[]
print(bool(l))#空列表为false
print(bool(None))#None的布尔值为false
'''






