#列表
'''
l=[1,2,3,4]#创建列表，使用方括号[],括号内的数据可以是int,float,str等，单个数据使用‘,’分隔
l2=list([1,2])#列表创建的第二种方式，使用list关键字
print(l[2])#获取列表索引位置对应的元素,l[索引从0开始，-1为列表的最后一个元素]
print(l.index(2))#获取列表元素对应的索引值
print(l[1:3])#获取列表切片对应的元素
l.append('x')#在列表末尾添加一个元素
l.extend(['a','b'])#将另一个列表添加到该列表末尾
l[1:0]=['s','d',None]#将另一个列表插入到该列表切片指定的位置
l.insert(1,'q')#在列表指定的索引位置插入单个元素
l[0]='d'#修改指定索引位置的元素
l.remove('q')#删除列表的某个元素
l.pop()#不加参数，默认删除列表的最后一个元素，加参数删除指定索引位置的列表元素
del l[1:3]#删除列表的多个元素
print(l)
print(l.count('d'))#获取列表元素出现的次数
q=l.copy()#复制整个列表
#l2.sort(reverse=True)#从大到小排序列表
#l2.sort()#不加参数从小到大排序
print(l)
l.reverse()#列表反向排序
print(l)
l.clear()#清空列表或者 del l[:]
print(l)
'''
'''
lst=[i*2 for i in range(1,25,2)]#列表生成式
print(lst)
print(len(lst))#计算列表的长度
print(max(lst))#求列表的最大值
print(min(lst))#求列表的最小值
l2=['a','b']
l3=lst+l2#列表组合，直接将两个列表的元素放入到一个列表中
print(l3)
print(['hill']*2)#列表元素重复
print('a' in l3)#判断元素是否在列表中
for x in l3:#列表遍历
    print(x,end='\t')
l3+=['c','d','e']#列表拼接
print(l3)
l3=[l2,['hill']]#列表嵌套，将另外两个列表嵌套到该列表中
print(l3)
'''
#创建二维列表
'''
l=[[0 for i in range(5)] for i in range(5)]
print(l)
l[0].append(3)
l[0].append(5)
l[2].append(7)
print(l)
'''
#列表的复制，使用copy模块
'''
import copy
a=[1,2,3]
b=a
c=copy.copy(a)
b[0]='b'
print(a)
print(b)
print(c)
'''
#使用列表自带的copy，重新开辟内存空间存储新列表
'''
i=[0,1,2,3,4]
j=i.copy()
j=j+['a','b','c']
print(i)
print(j)
'''
'''
list_empty=[None]*10#创建占用十个元素的空间，却不包含任何内容的列表
print(list_empty)
'''
#列表切片和反向列表元素
'''
a=[1,2,3,4]
b='abcdef'
print(a[1:2])
print(b[2:])
print(a[::-1])
print(b[::-1])
print(list(reversed(a)))
print(list(reversed(b)))
'''
#通过切片方法复制列表,结果生成了两个列表
'''
f=['pizza','falafel','carrot cake']
ff=f[:]
print(f)
print(ff)
print(f is ff)
'''
#列表是链式存储结构，不是顺序存储结构
'''
a=[1,2,3,4,5]
for i in range(len(a)):
    print(id(a[i]))
a[1]=100
print('--------')
for i  in range(len(a)):
    print(id(a[i]))
'''
#列表的函数或者说方法的对象不仅可以是字符串，也可以是列表对象
'''
l=['google','runoob',1997,2002]
l2=[1,2,3,4]
l2.append(l)
print(l2)
'''
'''
list1=['google','runoob',1997,2002]
for i in range(len(list1)):#遍历列表的长度
    print(i)
for i in list1:#直接遍历列表
    print(i)
for i in range(len(list1)-1,-1,-1):#反向遍历列表的长度
    print(i)
for i in reversed(list1):#反向遍历列表
    print(i)
for i in list1[::-1]:#通过切片反向遍历列表
    print(i)
'''
