#类
'''
class people:  #类定义【class 类名:】
    private='广东' #类实例共有的属性
    def __init__(self,name,age): #初始化类实例的属性
        self.name=name #self .类属性名=类属性名
        self.age=age
    def method(self): #定义类的实例方法
        print('我叫%s，今年%d岁，来自%s'%(self.name,self.age,self.private))
p1=people('jack',22) #创建类的实例
p1.method() #调用实例p1的method方法
print(people.private) #private属性类也可以调用
p2=people('tom',20)
p2.method() #p1、p2的private值相同
p1.grade=19 #添加类实例p1自己的属性，grade属性被p1独占，p2没有该属性
print(p1.grade)
#print(p2.grade)
people.private='四川' #更新private的值
p1.method()
p1.age=23 #更新实例p1属性的值
print(p1.age)

#类的单继承【student类继承people类的属性和方法】
class student(people):
    people.private #继承people类的共有属性，直接类名.属性名
    city='南充' #创建student类自己的共有属性
    def __init__(self,name,age,grade): #初始化实例属性，即使只调用一个父类的初始化属性，
        people.__init__(self,name,age) #调用people类的初始化属性方法 类名.__init__(self,属性名)
        self.grade=grade #创建自己的初始化属性
    def speak(self): #定义类的实例方法
        people.method(self) #继承父类people的实例方法
        print('年级：%d'%(self.grade)) #创建自己的实例方法
s1=student('tom',19,18)
s1.speak()

#类的多重继承【一个子类继承自多个父类】
class child(student,people):
    def __init__(self,name,age,grade,sex):
        people.__init__(self,name,age)
        student.__init__(self,name,age,grade)
        self.sex=sex
    def m(self):
        student.speak(self)
        print('性别：%s'%(self.sex))
c1=child('jack',12,6,'male')
c1.m()
'''

#类的封装【将类的属性和方法封装】对外隐藏，对内可见
#对test类添加装饰器property，将方法name伪装成属性
'''
class test:
    def __init__(self,name):
        self.__name=name #私有属性，对内可见，外部无法访问
    @property #将一个类方法转变成一个类属性，只读属性,获取属性值方法
    def name(self):
        return self.__name
    @name.setter #设置属性值方法
    def name(self,value):
        self.__name=value
    @name.deleter #删除属性值方法
    def name(self):
        del self.__name
t=test('jack')
print(t.name) # #如果一个方法伪装成属性，对象.方法名 就会自动调用该方法，就可以实现外部对封装类的属性的访问
'''

#多态
'''
class Animal(object):
    def __init__(self,name):
        self.name=name
    def method(self):
        print('this is animal')
class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
    def method(self):
        print('this is dog')
class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
    def method(self):
        print('this is cat')
a=Animal('donwu')
d=Dog('狗')
c=Cat('猫')
a.method()
d.method()
c.method()
'''

#__init__和__new__的区别
#__new__是在创建实例之前调用的，它是用来创建实例然后返回实例对象，是静态方法
#__init__是创建实例完成之后调用的，然后设置对象属性的一些初始值，通常用在初始化一个类实例的时候，是实例方法
#_new__先被调用，__init__后被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数。
'''
class Book(object):
    def __new__(cls,title):
        print('this is __new__')
        return super(Book,cls).__new__(cls)
    def __init__(self,title):
        print('this is __init__')
        super(Book, self).__init__()
        self.title=title
b=Book('this is python book')
print(b.title)
'''
#__new__的作用，是当你继承一些不可变的类时，提供给你一个自定义这些类实例化的过程，还有实现自定义的metaclass
#例如集成一个永远都是正数类型的数据
'''
class PositiveInterger(int):
    def __new__(cls, value):
        return super(PositiveInterger,cls).__new__(cls,abs(value))
i=PositiveInterger(-3)
print(i)
'''
#__new__是类级别的方法
'''
1.是在类准备将自身实例化时调用，并且至少要有一个cls参数，此参数在实例化时由python解释器提供
2.静态方法，即使不加静态装饰器@staticmethod
3.要求有返回值，return 父类 super(类本身，cls).__new__(cls,自己设置的参数)
'''
'''
class A(object):
    pass
a=A()
print(a) #默认调用object类的__new__方法
'''
'''
class A(object):
    def __new__(cls):
        return 'abc' #重写new方法，就改变了类实例的值
a=A()
print(a) #对类实例本身进行修改，new方法返回什么值，类实例就输出什么值
'''
#通过new方法实现单例
'''
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance=super(Singleton,cls).__new__(cls)
        return cls._instance
a=Singleton()
b=Singleton()
c=Singleton()
print(a)
print(b)
print(c)
'''
#__init__实例级别的方法
'''
1.有一个参数self，就是__new__返回的实例
2.__init__()在__new()的基础上完成初始化动作，不需要返回值；
3.若__new__()没有正确返回当前类cls的实例，那__init__()将不会被调用
4.创建的每个实例都有自己的属性，方便类中的实例方法调用；
'''
'''
class B:
    def __new__(cls):
        print('__new__方法被调用') #new方法下没有返回值return
    def __init__(self):
        print('__init__方法被调用')
b=B()
print(b) #init方法没被调用
'''
'''
class B:
        def __new__(cls):
            print('__new__方法被调用')
            return super(B,cls).__new__(cls) #new方法返回了当前类cls的实例，__init__会被调用
        def __init__(self):
            print('__init__方法被调用')
b = B()
print(b)
'''
#重写子类覆盖了父类的方法
'''
class a:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def method(self):
        print('我叫%s,今年%d岁'%(self.name,self.age))
class b(a):
    def __init__(self,name,age,sex):
        a.__init__(self,name,age)
        self.sex=sex
    def method(self):
        print('我叫%s，性别：%s'%(self.name,self.sex))
b1=b('tom',12,'male')
b1.method()
super(b,b1).method() #返回a类的method方法下定义的内容，super(子类名，子类实例).实例方法
'''

#类的私有属性
'''
class Counter:
    __secretcount=0 #私有变量
    publiccount=0 #公开变量
    def __init__(self,s,p):
        self.__secretcount=s
        self.publiccount=p
    def count(self):
        self.__secretcount+=1
        self.publiccount+=1
        print(self.__secretcount)
c1=Counter(1,1)
print(c1.publiccount) #访问实例的公开属性
print(c1._Counter__secretcount) #访问实例的私有属性，实例._类名__私有属性
'''

#类的私有方法
'''
class a:
    def __init__(self,A,B):
        self.A=A
        self.B=B
    def method(self): #公开的实例方法
        print('this is %s,one %s'%(self.A,self.B))
    def __rds(self): #私有实例方法
        print('this is a secert method')
a1=a('python','java')
a1.method() #访问公有方法
a1._a__rds() #访问私有方法 实例._类名__私有方法
'''

#类的三种方法
'''
class a:
    @staticmethod #静态方法修饰符
    def jintai():
        print('这是一个静态方法') #静态方法类和实例对象都可访问，类和实例的任何属性、方法都不能传递
    @classmethod #类方法修饰符，类方法(cls)
    def clas(cls):
        print('这是一个类方法') #类方法类和实例都可访问，只能传递类的属性和方法
    def shili(self): #实例方法(self)
        print('这是一个实例方法')
a.jintai()
a.clas()
#a.shili() #类可以访问它的静态和类方法，但不能访问实例方法
a1=a() #类的实例三种方法都可访问
a1.jintai()
a1.clas()
a1.shili()
'''

#类的一些常见方法
'''
class eample:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self): #返回一个描述类的实例的字符串对象
        return 'eample(%d,%d)'%(self.a,self.b)
    def __repr__(self): #也是返回一个描述类的实例的字符串对象
        return 'eample(%d)'%(self.a)
    def 

e1=eample(1,2)
print(e1.__str__())
print(e1.__repr__())
'''

#类的内置属性方法
class a(object):
    pass
class b(object):
    pass
class c(a,b):
    pass
print(a.__base__)#输出a类的父类(所有类的父类都是object)
print(c.__base__)#输出c类的第一个父类
print(c.__bases__)#输出除object类之外的所有c类的父类
print(c.__mro__)#输出c类的所有继承关系
print(c.__module__) #返回__main__
print(c.__basicsize__)#输出c类的字节大小
print(a.__subclasses__())#输出a类的子类






