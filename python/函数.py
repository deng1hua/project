#自定义函数使用def定义函数名g,后面要添加括号
'''
n=2#函数体之外的变量为全局变量，影响不到函数值的改变
def g(n):#n为函数的形式参数，当调用该函数时，需要向函数添加参数值
    n=n*n-1#函数内的局部变量计算表达式
    return n#return函数返回值,没有这个当调用函数时会返回None值
print(g(5))#5为函数的实际参数
'''
#可变对象和不可变对象在函数体中的修改是否影响到实参的值
'''
def fun(arg1,arg2):
    print('arg1:',arg1)
    print('arg2:',arg2)
    arg1=100
    arg2.append(24)
    print('arg1:',arg1)
    print('arg2:',arg2)
n1=11
n2=[22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2) #将位置传递参数，arg1\arg2是形参，n1\n2是实参，形参和实参名称可以不一致
print('n1',n1)#arg1是不可变量，n1没有因为函数体中arg1值的改变而改变
print('n2',n2)#arg2是可变量，因此会改变n2列表的值
'''
#函数返回多个值是元组类型的数据
'''
def fun(num):
    odd=[]
    evn=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            evn.append(i)
    return odd,evn
print(fun([11,24,9,5,12]))
'''
#函数没有返回值(函数执行完毕之后，不需要给函数提供数据)，return可以省略不写
'''
def f1():
    print('r')
    #return
f1()
'''
#函数有一个返回值,函数中的变量是何种类型的数据，调用函数时就返回何种类型的数据
'''
def f2():
    f='hello'
    return f
print(type(f2()))
'''
#函数定义默认值参数
'''
def h(a,b=10):
    print(a,b)
h(100)#调用函数时，只有一个参数，b的值默认为10
h(100,20)#有两个参数时，b的值被改变为20
'''
#个数可变的位置参数
'''
def f(*args):
    print(args)
    print(args[0])#返回元组索引位置0处对应的元组的元素
#返回元组类型的数据
f(10)
f(1,2)
'''
#个数可变的关键字参数
'''
def f(**kwargs):
    print(kwargs)
#返回字典类型的数据
f(a=10)
'''
#既有位置参数，又有关键字参数，位置参数在前，没有关键字的数据组成一个元组，有关键字的组成一个字典
'''
def g(*args,**kwargs):
    return args,kwargs
print(g(10,20,a=11))
'''
#函数总结
'''
def func(a,b,c):#a,b,c是函数的形式参数
    print('a:',a)
    print('b:',b)
    print('c:',c)
func(10,20,30)#10、20、30是函数的实际参数也是位置参数，按顺序传递给对应的函数的形式参数
l=[11,22,33]
func(*l)#使用一个*，将l列表作为位置参数传入
func(a=100,c=200,b=300)#关键字参数传入
d={'a':5,'b':2,'c':3}
func(**d)#使用两个**，将d字典作为关键字参数传入
'''
#*之前的值既可以使用位置参数，也可以使用关键字参数传入，*之后的值只能使用关键字传入
'''
def g(a,b,*,c,d):
    print(a,b,c,d)
g(1,2,c=3,d=4)#前两个值是位置实参，后两个是关键字实参
'''
#函数定义处形参的顺序
'''
def f1(a,b,*,c,d,**kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(kwargs)
d={'e':6,'f':9}
f1(1,2,c=3,d=4,**d)
def f2(*args,**kwargs):
    print(args,kwargs)
f2(12,13,a=7,b=9)
'''
#全局变量和局部变量
'''
age=10#全局变量，对函数不起作用
def fi():
    global age#对局部变量声明为全局变量
    age=22#局部变量
    print(age)
fi()
print(age)#直接输出全局变量的值
'''
#递归函数
'''
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(5))
'''
#斐波拉契函数
'''
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(-6))
'''
#匿名函数(lambda+参数名+‘:’+表达式)
'''
sum=lambda arg1,arg2=5:arg1+arg2#将匿名函数赋给变量sum
print(sum(arg2=10,arg1=20))#lambda的实参也可以使用关键字传递参数
print(sum(1))#lambda函数也可以设置默认值参数
'''
#局部作用域(函数内部)
'''
a=int(3.3)
b=0
def outer():
    x=1
    def inner():
        y=2
        print(x)#在函数内部x找到了变量的值
    inner()
outer()
'''
#全局作用域
'''
a=int(3.3)
b=0
def outer():
    x=1
    def inner():
        y=2
        print(b)#在函数外部b找到变量的值
    inner()
outer()
'''
#内建变量
'''
a=int(3.3)
b=0
def outer():
    x=1
    def inner():
        y=2
        print(a)#在内建变量a找到了变量的值
    inner()
outer()
'''
'''
def hello():
    print('hello,world')
def execute(f):
    #函数也可以以另一个函数为其参数
    f()
execute(hello)
print(execute.__doc__)#使用函数的__doc__显示地输出函数的说明文档
'''
#函数可以指定参数的类型和返回值的类型
'''
def func(a:int,b:float,c:str) -> list:
    pass
'''
#关键字nonlocal只影响上一层函数的值，该关键字的函数的值是多少，它的上一层函数的值就是多少
a=1
def outer():
    a=2
    def inner():
        nonlocal a
        a=3
        print(a)
    inner()
    print(a)
outer()
print(a)



