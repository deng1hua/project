'''
d={'a':1,'b':2}#创建字典
print(d)
print(type(d))
d1=dict({'name':'zhangsan','age':13})#使用dict关键字创建字典
print(d1)
print(d.get('a'))#获取字典键所对应的值
print(d['a'])#获取字典键所对应的值
print(d.items())#以列表返回可遍历的(键, 值) 元组数组
print(d.keys())#获取字典所有的键
print(d.values())#获取字典所有的值
d.setdefault('c')#添加字典的键，若未指定键所对应的值，它的值就默认为None
print(d)
d.update({'c':3})#更新字典键所对应的值
print(d)
d.pop('b')#删除字典指定键和它的值
print(d)
d.popitem()#删除字典的最后一个键值对
print(d)
d.clear()#清空字典
print(d)
'''
#不允许同一个键出现两次，如果出现，后一个值会被记住
'''
d1={'Name':'Runoob','Age':19,'Class':'first','Name':'小菜鸟'}
print(d1)
'''
#键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
'''
d={['a']:1,'b':2}
print(d)
'''
'''
dict={'a':1,'b':2,'c':3}
print(len(dict))#计算字典元素个数
print(str(dict))#以可打印的字符串表示
print(tuple(dict))#返回字典的键组成的元组
l=dict.copy()#字典的浅复制
print(l)
d=dict.fromkeys(('a','b','c'),10)#将一个元组中的元素作为字典的键,并设置字典的值都为10
print(d)
print('a' in d)#判断字符串是否在字典内
'''
#将字典的值修改为键，键修改为值,原始值必须是不可变类型
'''
dic={'a':1,'b':2,'c':3}
revers={v:k for k,v in dic.items()}
print(revers)
'''
'''
#获取字典最大值及其键
prices={'a':123,'b':450.1,'c':12,'d':44}
max_prices=max(zip(prices.values(),prices.keys()))
print(max_prices)
#通过values取到key
print(list(prices.keys()) [list(prices.values()).index(12)])
'''
#可以在列表中嵌套字典
'''
a={'x':1,'y':2}
b={'w':10,'s':20}
lst=[a,b]
print(lst)
'''
#字典推导式
'''
name = ["张三", "李四", "王五", "李六"]  # 保存名字列表
sign = ["白羊座", "双鱼座", "狮子座", "处女座"]  #保存星座列表
di={i:j for i,j in zip(name,sign)}
print(di)
'''

