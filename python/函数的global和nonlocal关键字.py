'''
global:全局变量
nonlocal:外层嵌套函数的变量
使用总结：
1、局部作用域改变全局变量用global， global同时还可以定义新的全局变量
2、内层函数改变外层函数变量用nonlocal， nonlocal不能定义新的外层函数变量，只能改变已有的外层函数变量
,同时nonlocal不能改变全局变量
'''
#一、没有关键字
'''
a=10  #a1全局变量对函数没有影响
def outer():
    a=9  #a2局部变量
    def inner():
        a=8  #a3嵌套函数的局部变量
        print(a)
    inner()
    print(a)
outer()
print(a) #a1、a2、a3是三个不同的变量
'''
#二、global关键字：声明此变量为全局变量
#1、用于在局部作用域中修改全局变量
'''
a=10  #全局变量的值变成a2
def outer():
    global a
    a=9  #a2局部变量声明为全局变量
    def inner():
        a=8
        print(a)
    inner()
    print(a)
outer()
print(a)  #a1、a2都是全局变量，a3还是局部变量
'''
#2.如果没有在函数外层定义全局变量，在函数中对局部变量加global关键字可以使其成为新的全局变量
'''
def outer():
    a=9
    def inner():
        global a #声明a3为全局变量，只改变全局变量的值，外层函数的变量值不改变
        a=8
        print(a)
    inner()
    print(a) #a2还是9
outer()
print(a) #a3、a1都是全局变量值8
'''
#3.outer没有局部变量
'''
def outer():
    def inner():
        global a #声明a3为全局变量
        a=8
        print(a) #输出a3=8
    inner()
    print(a)  #因为outer函数中未定义变量，a2的值默认改变为全局变量，输出a2=8
outer()
print(a) #输出全局变量a1的值8
'''
#二、nonlocal关键字，只改变嵌套函数中的变量值
'''
a=10
def outer():
    a=9
    def inner():
        nonlocal a #使嵌套函数中的局部变量值都改变为8
        a=8
        print(a)#输出a3=8
    inner()
    print(a)#输出a2=8
outer()
print(a)#对全局变量无影响，输出a1=10
'''
#
'''
a=10
def outer():
    a=9
    def inner():
        a=8
        def oinner():
            nonlocal a 
            a=7
            print(a) #输出a4=7
        oinner()
        print(a) #nonlocal关键字只对其上一层函数起作用，只会改变a3的值，输出a3=7
    inner()
    print(a) #输出a2=9
outer()
print(a) #输出a1=10
'''
#nonlocal关键字只能放在内层函数，放在外层函数中会报错
'''
a=10
def outer():
    nonlocal a
    a=9
    def inner():
        a=8
        print(a)
    inner()
    print(a)
outer()
print(a)
'''
