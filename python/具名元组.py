'''
#创建可命名元组对象
import collections
User=collections.namedtuple('User','name age id')#第一个参数是可命名元组对象，第二个参数是这个元组的字段名
user=User('tester',22,445083)
print(user)
'''
#具名元组的特有属性
'''
from collections import namedtuple
User=namedtuple('User',['name','sex','age'])#创建一个namedtuple对象，包含name、sex、age属性【namedtuple可命名元组】
#namedtuple对象的第一个参数是对象名，第二个参数是对象的属性，属性是列表数据，每个属性字符串之间用逗号分割
user=User(name='Runoob',sex='male',age=12)#创建一个User对象
print(user._fields)#获取所有字段名
user=User._make(['jake','female',23])#也可以通过User.__make方法创建User对象
print(user)
print(user.name)#获取对象用户属性
user=user._replace(age=13)#修改对象用户属性的值
print(user)
print(user._asdict())#将User对象转换成字典
'''

#计数器Counter,返回字典形式的元素的个数
'''
import collections
a='a112bb'
print(collections.Counter(a))
#计数器的most_common方法,将元素出现的次数按从高到低排序
#并返回前N个元素，若多个元素统计相同，按照字母顺序排列，N若未指定，返回所有元素
b=collections.Counter(a)
print(b.most_common())
#elements:返回一个迭代器，元素被重复多少次，在迭代器中就包含多少个此元素，
#所有元素按字母顺序排列，个数小于1的不罗列
print(list(b.elements()))
#update增加元素的重复次数一次
b.update('a')
print(b)
#subtract;减少元素重复次数一次
b.subtract('ab')
print(b)
'''

#有序字典ordereDict:继承了dict的所有功能，dict是无序的，ordereDict是有序的
#记录了键值对插入的顺序，是有序字典
'''
import collections
dic=collections.OrderedDict({'name':'tom','age':18,'sex':'man'})
print(dic)
#ordereDict类补充方法，clear方法
#dic.clear()
#print(dic)
#popitem有序删除,从最后一个元素开始删除
#dic.popitem()
#print(dic)
#pop:删除指定键值对
#dic.pop('age')
#print(dic)
#move_to_end：将指定键值对移到最后位置
dic.move_to_end('name')
print(dic)
#setdefault:设置默认值，默认为None,也可指定值
dic.setdefault('course')
print(dic)
#update:更新字典，有则更新，无则添加
dic.update({'course':'Chinese'})
print(dic)
#默认字典defaultdict：设置values默认类型，如list、tuple
dic=collections.defaultdict(list)
dic['course'].append('En')
dic['course'].append('Cn')
print(dic)
'''

#双向队列deque:类似于list，允许两端操作元素
#append:从队列右侧添加元素
import collections
deq=collections.deque('abcd')
deq.append('e')
print(deq)
#apendleft:从队列左侧添加元素
deq.appendleft('1')
print(deq)
#count:统计队列中指定元素的个数
print(deq.count('a'))
#extend:从队列右侧扩展
deq.extend([11,22,33])
print(deq)
#extendleft:从队列左侧扩展
deq.extendleft([0,'x'])
print(deq)
#index:取元素索引位置
print(deq.index('a'))
#insert:在队列任意位置插入值
deq.insert(3,'y')
print(deq)
#pop:从队列右侧移除值
deq.pop()
print(deq)
#popleft:从队列左侧移除值
deq.popleft()
print(deq)
#remove:移除指定值
deq.remove('y')
print(deq)
#reverse:将队列中的元素反转
deq.reverse()
print(deq)
#rotate:移动队列中的元素，若n<0，则从队列最左侧的元素依次移动到最右侧，
#若n>0,从最右侧的元素移动到最左侧
deq.rotate(2)
print(deq)
deq.rotate(-2)
print(deq)
