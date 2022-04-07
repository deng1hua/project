'''
#算术运算符
a=10
b=20
print(a+b)#加法运算符
print(a-b)#减法运算符
print(a*b)#乘法运算符
print(a**b)#幂运算符
print(a/b)#除法运算符
print(5//2)#整除运算符，取整除部分
print(5%2)#取余运算符，取余数部分
print(a+b-b*2**2/2//5%5)#算术运算符优先级【幂运算-乘、除、整除、取余运算-加减】
'''

'''
#比较运算符,结果为true或false
print(10==20)#等于
print(10!=20)#不等于
print(10>20)#大于
print(10<20)#小于
print(10>=20)#大于等于
print(10<=20)#小于等于
'''

'''
#赋值运算符
a=10
b=20
c=a+b#将a+b的结果赋值给c
print(c)
c+=a#加法赋值运算符，c=c+a
print(c)
c-=a#减法赋值运算符，c=c-a
print(c)
c*=a#乘法赋值运算符，c=c*a
print(c)
c/=a#除法赋值运算符，c=c/a
print(c)
c**=a#幂赋值运算符，c=c**a
print(c)
c//=a#整除赋值运算符，c=c//a
print(c)
c%=a#取余赋值运算符，c=c%a
print(c)
'''

'''
#位运算符
a=60
b=13
print(bin(a))
print(bin(b))
print(a&b)#按位与运算符，参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
print(bin(a&b))
print(a|b)#按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1
print(bin(a|b))
print(a^b)#按位异或运算符：当两对应的二进位相异时，结果为1
print(bin(a^b))
print(~a)#按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1
print(bin(~a))
print(a<<2)#左移运算符,运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0
print(a>>2)#右移运算符,把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数
'''

'''
#逻辑运算符
a=10
b=20
print(a and b)#x and y,如果x是false,返回x,否则返回y
print(a or b)# x or b,如果x是true，返回x,否则返回y
print(not (a and b))#布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True
'''

'''
#成员运算符
a=2
b=9
lst=[1,2,3,4]
print(a in lst)#判断a变量的值是否在列表内，有返回true,没有返回false
print(b not in lst)#判断b变量的值是否不在列表内，没有在返回true,在返回false
'''

'''
#身份运算符
a=10
b=10
print(a is b)#判断两个变量是否引用自同一个内存地址，是返回true,否则返回false
print(id(a))
print(id(b))
print(a is not b)#判断两个变量是否引用不同的内存地址，是返回true,否则返回false
'''

#运算符优先级【幂-》按位翻转，一元加号和减号 (最后两个的方法名为 +@ 和 -@)[~ + -]-》乘除、求余数、求整除-》加减-》右移、左移运算符-》按位与-》按位或、异或运算符-》大于、大于等于、小于、小于等于运算符
# -》等于、不等于运算符-》赋值运算符-》身份运算符-》成员运算符-》逻辑运算符】
'''
print(17%2==0 or 'cake'*3)#or左边的为false,因此输出右边正确的
print(not 5>3)#先进行比较运算，在进行身份运算
print(not not 10**2>=100 and '1')#幂运算-》比较运算-》身份运算-》逻辑运算
'''



