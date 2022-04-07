'''
s='str|abc|red'
print(s.index('r'))#获取单个字符在整个字符串中的索引位置，没有会报错
print(s.rindex('r'))#查找子串最后出现的位置
print(s.find('r'))#查找子串第一次出现的位置，如果没有这个子串返回-1
print(s.rfind('r'))#查找子串最后出现的位置
print(s.count('r'))#单个字符在整个字符串中出现的次数
t=s.split(sep='|',maxsplit=1)##参数sep指定分隔符，参数maxsplit最大劈分次数，在经过最大劈分后，剩余的子串会单独作为一部分
print(t)
t1=s.rsplit(sep='|',maxsplit=1)#从字符串右边开始劈分，劈分一次
print(t1)
'''

'''
q=' abc '
q1=q.strip()#将字符串两端的空白删除
print(q1)
q2=q.rstrip()#将字符串右端的空白删除
print(q2)
q3=q.lstrip()#将字符串左边的空白删除
print(q3)
'''

'''
st='AbcD str'
print(st.upper())#将字符串的所有字母转换成大写
print(st.lower())#将字符串的所有字母转换成小写
print(st.title())#将每个单词的首字母转换成大写，其余小写
print(st.capitalize())#将字符串的第一个字母转成大写，其余小写
print(st.swapcase())#将字符串的大写字符转成小写，小写字符转成大写
'''

'''
w='python'
print(w.isdigit())#判断字符串是否只包含数字
print(w.isalpha())#判断字符串是否只包含字母
print(w.isalnum())#判断字符串所有字符都是字母或数字
print(w.isspace())#判断字符串是否只包含空格
print(w.isascii())#判断字符串为空或所有字母都是ASCII  ASCII码包括大小写英文字母、标点符号、阿拉伯数字、数学符号、控制字符等共128个字符，一个ASCII码占一个字节，用7位二进制数编码组成 
print(w.isdecimal())#判断字符串是否只包含十进制数字
print(w.isnumeric())#判断字符串是否全部由数字组成
print(w.isidentifier())#判断字符串是否是合法的标识符(字母、数字和下划线)
print(w.islower())#判断字符串的所有字母是否全部是小写
print(w.isupper())#判断字符串的所有字母是否全部是大写
print(w.isprintable())#判断字符串是否可打印或者为空，不可打印的字符串是回车、换行符(\n)、制表符(\t)
print(w.istitle())#判断字符串的每个单词的首字母是否大写
'''

'''
a=['google','facebook','amazon','twitter']
print('|'.join(a))#将列表中的每个元素使用|分割，合并成一个字符串
print(' '.join(a))
print('*'.join('python'))#将字符串的每个字母拆分，并使用*连接
'''

'''
a='python,java'
b=a.replace('java','php')#字符串替换，第一个参数是要替换的字符串，第二个参数是新的字符串
print(b)
'''

'''
s='python'
print(s.endswith('on',4,6))#判断字符串是否含有指定的后缀,4和6分别是字符串的开始位置和结束位置【索引4到6的位置是否含有字符串on的后缀】
print(s.startswith('py',0,2))#判断字符串是否含有指定的前缀
'''

'''
#字符串的对齐方式
s='python'
print(s.ljust(10,'!'))#字符串左对齐，第一个参数指定宽度，第二个参数指定填充符
print(s.rjust(10,'!'))#字符串左对齐
print(s.center(10,'!'))#字符串居中对齐
print(s.zfill(10))#右对齐，左边使用0进行填充
'''

'''
#字符串编解码
s='天涯共此时'
s1=s.encode(encoding='gbk')#encode编码
s2=s.encode(encoding='utf-8')
print(s1)
print(s2)
s3=s1.decode(encoding='gbk')#decode解码
s4=s2.decode(encoding='utf-8')
print(s3)
print(s4)
'''

'''
#expandtabs将字符串中的\t符号替换为空格
s='python\tjava'
print(s.expandtabs())
print(s.expandtabs(6))#里面的参数指定转换字符串中的 tab 符号 \t 转为空格的字符数【转换为多少个空格】。
'''

'''
s='python'
print(len(s))#计算字符串长度
print(max(s))#字符串中的最大字母
print(min(s))#字符串中的最小字母
'''

'''
a="aeiou"
b="12345"
tt=str.maketrans(a,b)#将字符串中的字母转换成对应的数字，两个参数的长度要相同
str="this is eample...wow"
print(str.translate(tt))#根据maketrans给出的转换关系，转换对应的字母为数字
'''

'''
#格式化字符串
name='jake'
age=12
jz='my name is {},now is {}'.format(name,age)#第一种方法，添加字符串的format方法，引入要格式化的字符串
print(jz)
j1=f'my name is {name},now is {age}'#第二种方法，在字符串前加一个f，字符串中的花括号内添加要格式化的字符串
print(j1)
j2='my name is %s,now is %d'%(name,age)#第三种方法，使用格式化字符串、格式化整数符号
print(j2)
#使用字典对象格式化字符串
people={'name':'jake','age':'12'}
j3='my name is {name},now is {age}'.format_map(people)#format_map的参数【mapping】是一个字典对象，且在格式化时要在大括号内加入相应的键
print(j3)
'''


'''
print('%10s'%('python'))#格式化字符串，调整字符串的宽度为10,右对齐
print('%-10s'%('python'))#左对齐，调整宽度为10
print('%.2s'%('python'))#取字符串前两位
print('%10.2s'%('python'))#取字符串前两位，右对齐，设置宽度为10
print('%-10.2s'%('python'))#取字符串前两位，左对齐，设置宽度为10
print('%10d'%99)#格式化整数，调整整数的宽度为10 => print('{0:10d}'.format(99))
print('%.2f'%3.1415926)#保留浮点数两位 => print('{0:.2f}'.format(3.1415926))
print('%10.2f'%3.1415926)#同时设置宽度为10，保留小数点后两位 => print('{0:10.2f}'.format(3.1415926))
print('%e'%3.1415926)#默认小数点后六位用科学计数法
print('%.2e'%3.1415926)#保留小数点后两位用科学计数法
print('%g'%3.1415926)#默认取六位数字，包括小数点前面的整数部分
print('%.7g'%3.1415926)#取七位数字
print('%.2g'%1113.14151926)#取两位数字，自动转换为科学计数法
'''

'''
s='MobileF'
print(s.casefold())#将字符串所有字符转为小写
'''

'''
txt='i could eat bananas all day'
print(txt.partition('bananas'))#搜索指定的字符串，并将该字符串拆分为包含三个元素的元组，bananas前面的所有字符串为一个元素，它之后的也为一个元素
print(txt.partition('apples'))#如果没有指定的字符串，将整个字符串内容作为一个元组的元素，第二个、第三个都为空字符串元素
print(txt.rpartition('bananas'))#和字符串的partition方法输出相同
print(txt.rpartition('apples'))#如果没有指定的字符串，第一个、第二个元素都为空字符串，最后一个元素是整个字符串
'''

'''
str1 = 'ab c\n\nde fg\rkl\r\n'
print(str1.splitlines())#返回一个每行作为元素的列表
print(str1.splitlines(True))#为True时，返回一个保留\n、\r的列表
'''

'''
#字符串的驻留机制，对于相同的字符串只保留一份拷贝，后续再创建相同的字符串，不再开辟新的内存空间，而是把字符串的地址直接赋值给新的变量
a='python'
b='python'
print(id(a))
print(id(b))
#字符串驻留的几种情况
#字符串的长度为0或1
a1=''
b1=''
print(a1 is b1)
a11='a'
b11='a'
print(a11 is b11)
#合法的标识符的字符串
a2='\n'
b2='\n'
print(a2 is b2)
#只在编译时驻留，而非运行时
a3='abc'
b3='ab'+'c'
print(a3 is b3)#编译时驻留
b4=''.join(['ab','c'])
print(a3 is b4)#运行时没驻留
#-5到256之间的数字
a4=-4
b4=-4
print(a4 is b4)
#强制驻留，使用sys模块的intern方法
import sys
a5='abc'
b5=''.join(['ab','c'])
b5=sys.intern(a5)
print(a5 is b5)
'''

'''
#字符串比较[比较它们的字符串长度]
print('apple'>'app')
print(ord('a'))#获取指定字母的原始值
print(chr(97))#获取原始值对应的字母
'''

'''
#字符串切片
a='python'
print(a[2])#获取索引值在字符串中对应的字符
print(a[-2])#字符串的最后一个字母为-1，倒数第二个为-2，依次类推
print(a[1:5:2])#索引值1对应的字母为y，索引值5对应的字母为n,切片的范围是左闭右开，因此切片的范围是从y到n,不包括n,2为步长
print(a[3::-2])#获取索引值3到最开始的字符，步长为-2
'''

#字符串反转,输出‘python hello’
#s='hello python'
#print(' '.join(s.split(sep=' ')[::-1]))

'''
a='hello'
b='python'
#字符串连接
print(a+b)
#字符串重复
print(a*2)
#字符串索引
print(a[2])
#字符串切片
print(a[1:4])
#字符串成员判断
print('e' in a)
print('f' not in a)
#转义字符
print(r'\n')
'''


















