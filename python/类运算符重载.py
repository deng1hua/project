'''
class mynumber:
    def __init__(self,v):
        self.data=v
    def __repr__(self):#返回一个可以用来表示对象的可打印字符串
        return 'mynumber(%d)'%self.data
    def __add__(self, other):#加法运算符重载
        v=self.data+other.data
        return mynumber(v)#用v创建一个新的对象返回给调用者
    def __sub__(self, other):#减法运算符重载
        v=self.data-other.data
        return mynumber(v)
    def __mul__(self, other):
        return mynumber(self.data*other)
n1=mynumber(100)
n2=mynumber(200)
n3=n1+n2
print(n3)
print(n2-n1)
n5=n1*3
print(n5)
'''
'''
class Mylist:
    def __init__(self,iterable=()):
        self.data=list(iterable)
    def __repr__(self):
        return 'Mylist(%s)'%self.data
    def __mul__(self, other):
        return Mylist(self.data*other)
    #出现内建类型的错误时，需要加一个反向运算符重载
    def __rmul__(self, other):
        return Mylist(self.data*other)
    def __add__(self, other):
        return Mylist(self.data+other.data)
    def __neg__(self):#负号一元运算符
        g=(-x for x in self.data)
        return Mylist(g)
    def __pos__(self):#正号一元运算符
        g=(abs(x) for x in self.data)
        return Mylist(g)
    def __contains__(self, item):#in和not in运算符重载
        return True if item in self.data else False
    def __getitem__(self, item):#索引和切片运算符重载（取值）
        '索引取值,item绑定[]内的元素'
        print('item的值',item)
        return self.data[item]#返回data绑定列表中的第i个元素
    def __setitem__(self, key, value):#赋值
        print('__setitem__被调用,i=',key,'v=',value)
        self.data[key]=value
    def __delitem__(self, key):#删除索引和切片
        del self.data[key]
        return self
        if type(key) is int:
            print('用户正在用索引取值')
        elif type(key) is slice:
            print('用户正在用切片取值')
            print('切片的起点是：',key.start)
            print('切片的终点是：',key.stop)
            print('切片的步长是：',key.step)
        elif type(key) is str:
            print('用户正在用字符串进行索引操作')
        return self.data[key]

L1=Mylist([1,2,3])
'''
#L1*=3
#print(L1)
'''
L2=Mylist([4,5,6])
L2+=L1#(L2=L2+L1)
print(L2)
L3=-L2
print(L3)
L4=+L3
print(L4)
if 2 in L1:
    print('2在L1内')
print(3 in L1)
print(L1[2])
print(L1[2:])
'''
'''
class Student:
    def __init__(self, s):
        self.__score = s
    @property #使用@property装饰器创建方法实现对私有属性的操作
    def score(self):
        print('getter被调用')
        return self.__score
    @score.setter#使用方法名.setter,实现修改私有属性的值,使score方法可读可写
    def setScore(self, s):
        if 0 <= s <= 100:
            self.__score = s
    def getScore(self, s):
        #getter只是用来获取数据
        return self.__score
s = Student(20)
# s.setScore(100)
score = s.score
print('成绩是：', score)
'''



