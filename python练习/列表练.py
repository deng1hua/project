#1.用户输入月份，判断这个月是哪个季节
#思路：1、2、3春季，4、5、6夏季，7、8、9秋季，10、11、12冬季，
# 可以通过判断一个变量是否在指定的列表中，来判断是哪个季节



#2.假定有下面的列表:
    #names = ['fentiao','fendai','fensi','apple']
    #输出结果为:'I have fentiao, fendai, fensi and apple.'
names = ['fentiao','fendai','fensi','apple']


#3.设计一个程序，用来实现帮助小学生进行百以内的算术练习，它具有以下功能：
#提供10道加、减、乘或除四种基本算术运算的题目；
#练习者根据显示的题目输入自己的答案，程序自动判断输入的答案是否正确并显示出相应的信息。
#思路：1.导入随机模块 -》2.定义正确的答题数和总答题数变量的初始值为0
# 3.创建一个while循环，提数小于10
#4.定义一个包含‘加 减 乘 除’字符串列表，再定义一个随机生成这个列表中的字符的变量
#5.定义随机生成的第一个数的范围
#6.定义第二个随机生成的数的范围
#7.打印一个字符串格式化
#8.提示用户输入答案
#9.添加条件语句判断随机生成的字符，生成结果
#10.判断答案是否和计算后的结果相等
#11.计算正确率







#4.1.系统里面有多个用户，用户的信息目前保存在列表里面
    #users = ['root','westos']
    #passwd = ['123','456']
   #2.用户登陆(判断用户登陆是否成功）
    #1).判断用户是否存在
    #2).如果存在
     #   1).判断用户密码是否正确
      #  如果正确，登陆成功，推出循环
       # 如果密码不正确，重新登陆，总共有三次机会登陆
     #3).如果用户不存在重新登陆，总共有三次机会
users = ['root','westos']
passwds = ['123','456']



#5模拟栈的工作原理
'''
#定义一个空列表，用来表示栈
stack=[]
#定义操作选项的变量
info="""
 栈操作
1.入栈
2.出栈
3.栈顶元素
4.栈的长度
5.栈是否为空
q.退出
"""
'''
stack=[]
info="""
 栈操作
1.入栈
2.出栈
3.栈顶元素
4.栈的长度
5.栈是否为空
q.退出
"""


#6.后台管理员管理前台会员信息系统:
'''
1. 后台管理员只有一个用户: admin, 密码: admin
2. 当管理员登陆成功后， 可以管理前台会员信息.
3. 会员信息管理包含:
      添加会员信息
      删除会员信息
      查看会员信息
      退出

- 添加用户:
    1). 判断用户是否存在?
    2).  如果存在， 报错；
    3).  如果不存在，添加用户名和密码分别到列表中;

- 删除用户
    1). 判断用户名是否存在
    2). 如果存在，删除；
    3). 如果不存在， 报错；
'''
print('管理员登陆界面'.center(20,'-'))
users=['westos','linux']
passwds=['123','456']
inuser=input('请输入用户名：')
inpasswd=input('请输入密码：')

