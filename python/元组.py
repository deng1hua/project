'''
s=(1,'a',2,3,'a')#创建元组,元组是不可变数据类型
print(type(s))
s1=tuple((1,4,5))#创建元组的第二种方式，使用tuple方法
print(type(s1))
s2=('b',)#创建只有一个元素的元组，需要在元素后面添加一个逗号
print(type(s2))
print(s[0])#元组索引
print(s[1:3])#元组切片
print(len(s))#获取元组的长度
print(max(s1))#获取元组的最大值
print(min(s1))#获取元组的最小值
print(s.count('a'))#统计元组的该元素在元组中的出现次数
print(s.index('a'))#元素在元组中的索引位置，如果出现重复元素，输出元素最开始出现的索引位置
#元组是不可变类型数据，但它的元素若是可变数据类型，则可以对元素进行修改
t=(1,2,['str','kill'])
print(t[2][0])
t[2][0]=3
t[2][1]=4
print(t)
#元组遍历
for i in s:
    print(i,end='\t')
#元组连接
s4=s+s2
print(s4)
#通过间接方法修改元组
ls=list(s)
ls.pop()
print(ls)
s=tuple(ls)
print(s)
#使用del删除整个元组
del s
print(s)
'''






