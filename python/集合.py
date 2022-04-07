'''
s={9,10,20}#创建集合，使用大括号，元素之间用逗号隔开
print(s)
print(type(s))
s1=set({1,2,3})#使用set关键字创建集合
print(type(s1))
print(len(s))#获取集合元素个数
print(max(s))#集合的最大值
print(min(s))#集合的最小值
s.pop()#删除集合元素，从最开始的位置删除
print(s)
s.add(1)#添加集合元素
print(s)
s.update(s1)#将另一个集合添加到该集合中，如果有重复的元素会去重，只保留一个
print(s)
s.discard(3)#删除集合元素，即使集合中没有该元素，也不会报错
print(s)
#s.remove(4)#删除集合元素，如果集合中没有该元素，则会报错
#print(s)
q=s.copy()#复制集合
print(q)
s.clear()#清空集合
print(s)
#del s#删除集合对象，再输出集合就会报错
#print(s)
print(q|s1)#并集，将两个集合对象放在一个集合中
print(q&s1)#交集，输出两个集合都有的元素
print(q-s1)#差集，q有s1没有的元素
print(q^s1)#q和s1出了相同元素以外的所有元素
print(q.intersection(s1))#q和s1的交集
#q.intersection_update(s1)#只保留两个集合相同的元素，不同的删除，该方法会改变原来的集合对象
#print(q)
print(q.difference(s1))#q集合中有、s1内没有的元素
#q.difference_update(s1)#只保留q集合中有、s1内没有的元素，该方法会改变原来的集合对象
#print(q)
print(q.symmetric_difference(s1))#返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
#q.symmetric_difference_update(s1)#删除q集合中和s1集合相同的元素，并将s1集合不同的元素添加到q集合中，该方法会改变原来的集合对象
#print(q)
print(q.isdisjoint(s1))#判断两个集合是否有交集，有返回false,没有返回true
q1={1,2}
print(q1.issubset(q))#q1是否包含在指定的集合q中
print(q.issuperset(q1))#q是否包含q1集合
w={'a','b'}
t=q.union(w)#合并集合，将创建一个新的集合
print(t)
'''
#集合推导式
tu={i for i in range(1,100)}
print(tu)
#在集合中没有重复的元素，元素只出现一次
t={1,2,1,3}
print(t)#{1, 2, 3},t中重复的1在输出集合时，只有一个1了
#s.update( {"字符串"} ) 将字符串添加到集合中，有重复的会忽略。
#s.update( "字符串" ) 将字符串拆分单个字符后，然后再一个个添加到集合中，有重复的会忽略。
thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({"thisset"})
print(thisset)
thisset.update("str")
print(thisset)
#创建含有一个元素的集合
myset=set(('apple',))
print(myset)
#创建含有多个元素的集合
m=set(('banana','orange'))
print(m)
#集合对列表和元组具有排序的功能
t1=set([3,5,1,2,9,7])
print(t1)
s1=set((10,9,22,5,4))
print(s1)
#当集合是由列表和元组组成时、set.pop() 是从左边删除元素
t1.pop()
print(t1)
s1.pop()
print(s1)
#按集合中的字符长度进行排序
te=['a','b','cc','d']
te.sort(key=len)
print(te)














