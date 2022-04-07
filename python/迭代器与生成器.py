#迭代器
#l=[1,2,3,4]
#it=iter(l)#创建迭代器对象
#print(next(it))#输出迭代器的下一个元素
#print(next(it))
'''
#迭代器对象可以用for循环遍历,for循环就是不断地调用迭代器的next方法
for i in it:
    print(i,end=',')
'''
'''
#也可以使用next函数
import sys
while True:
    try:#把next输出迭代器的下一个元素的函数可能发生的错误放在try内
        print(next(it))
    except StopIteration:#捕捉当迭代器对象迭代完后的中断异常，执行退出程序
        sys.exit()
'''
#迭代器可用生成列表来理解
'''
l=[i for i in range(0,15)]#列表生成式遍历0到15的数字
print(l)
for i in l:#for循环遍历列表的所有元素
    print(i)
'''
#yield后面可以加多个数值,但返回的值是元组类型的一个生成器对象，yield对应的值在函数调用时不会直接返回，而是通过调用next方法返回值
'''
def get():
    m=0
    n=2
    l=['s',1,3]
    k={1:1,2:2}
    p=('2','s','t')
    while True:
        m+=1
        yield m
        yield m,n,l,k,p
i=get()
print(next(i))#首次输出迭代器的值，只输出m的值
print(next(i))#再次输出迭代器的值，输出m,n,l,k,p的值
print(next(i))
print(next(i))
print(type(next(i)))
print(type(next(i)))
'''
#字符串也是可迭代的
'''
for i in 'hello':
    print(i)
'''
'''
#列表可迭代对象使用方括号
for i in [None,3,4.5,"foo",lambda : "moo",object,object()]:
    print('{0} {1}'.format(i,type(i)))
#元组可迭代对象使用圆括号
for i in (None,3,4.5,"foo",lambda : "moo",object,object()):
    print('{0} {1}'.format(i,type(i)))
'''
#以斐波拉契数列来实现一个迭代器
'''
class fib:
    def __init__(self,n):
        self.prev=0
        self.cur=1
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n>0:
            value=self.cur
            self.cur=self.prev+self.cur
            self.prev=value
            self.n-=1
            return value
        else:
            raise StopIteration
f=fib(10)
print([i for i in f])
'''
#用生成器实现斐波拉契数列
'''
def fib(n): #定义fib函数，向函数接收一个n参数
    prev,sur=0,1 #定义两个变量的初始值为0和1
    while n>0: #创建当n>0的循环
        n-=1 
        yield sur #用生成器关键字yield sur来返回sur的值
        prev,sur=sur,prev+sur #定义变量的表达式
print([i for i in fib(10)])
'''
#生成器表达式，用圆括号
'''
g=(x*2 for x in range(3))
print(g)
'''
#使用生成器返回前n项自然数的平方
'''
def g(n):
    for i in range(n):
        yield i**2
print([i for i in g(5)])
'''
#普通函数实现返回前n项自然数的平方
'''
def g(n):
    l=[]
    for i in range(n):
        l.append(i**2)
    return l
print(g(5))
'''
#输入一段文字，判断每个单词的首字母出现的位置
'''
def words(text):
    result=[]
    if text:
        result.append(0)
    for index,letter in enumerate(text,1):#enumerate函数将一个可遍历的数据对象组合为一个索引序列，同时输出数据和它对应的索引值，一般用在for循环中
        if letter==' ':
            result.append(index)
    return result
print(words('hello word'))
'''
#使用生成器实现【少了创建列表、像列表中添加数据和返回列表对象这些步骤】
'''
def words(text):
    if text:
        yield 0
    for index,letter in enumerate(text,1):
        if letter==' ':
            yield index
print(words('hello word'))
print([i for i in words('hello word')])
'''




