#1.用户输入月份，判断这个月是哪个季节
#思路：1、2、3春季，4、5、6夏季，7、8、9秋季，10、11、12冬季，
# 可以通过判断一个变量是否在指定的列表中，来判断是哪个季节
'''
month=int(input('请输入月份：'))
spring=[1,2,3]
summer=[4,5,6]
autmn=[7,8,9]
winner=[10,11,12]
if month in spring:
    print('春季')
elif month in summer:
    print('夏季')
elif month in autmn:
    print('秋季')
elif month in winner:
    print('冬季')
else:
    print('请输入正确的月份：')
'''
#2.假定有下面的列表:
    #names = ['fentiao','fendai','fensi','apple']
    #输出结果为:'I have fentiao, fendai, fensi and apple.'
#names = ['fentiao','fendai','fensi','apple']
#print('I have '+','.join(names[:3])+' and '+(names[3]))
#3.设计一个程序，用来实现帮助小学生进行百以内的算术练习，它具有以下功能：
#提供10道加、减、乘或除四种基本算术运算的题目；
#练习者根据显示的题目输入自己的答案，程序自动判断输入的答案是否正确并显示出相应的信息。
'''
import random
#定义用来记录总的答题数目和正确的数目
count=0
right=0
#提供十道题目
while count < 10:
    op = ['+', '-', '*', '/']  # 创建列表，用来记录加减乘除四大运算
    s = random.choice(op)  # 随机生成op列表中的字符
    a = random.randint(0, 100)  # 随机生成0-100以内的数字
    b = random.randint(1, 100)  # 除数不能为零
    print('%d %s %d = ' % (a, s, b))
    question = input('请输入你的答案：（q退出）')  # 默认输入的为字符串类型
    # 判断随机生成的运算符，并计算正确结果
    if s == '+':
        result = a + b
    elif s == '-':
        result = a - b
    elif s == '*':
        result = a * b
    else:
        result = a / b
    # 判断用户输入的结果是否正确，str强制转换为字符串类型
    if question == str(result):
        print('回答正确')
        right += 1
        count += 1
    elif question == 'q':
        break
    else:
        print('回答错误')
        count += 1
#计算准确率
if count==0:
    percent=0
else:
    percent=right/count
print('测试结束，共回答%d道题，回答正确个数为%d,正确率为%.2f' %(count,right,percent*100))
'''
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
'''
#定义列表，用来记录用户名和密码
users=['root','westos']
passwds=['123','456']
#定义尝试登录的次数
trycount=0
#判断尝试登录次数是否超过3次
while trycount<3:
    #接收用户输入的用户名和密码
    inuser=input('用户名：')
    inpasswd=input('密码：')
    trycount+=1
    #判断用户是否存在
    if inuser in users:
        #先找出用户对应的索引值
        index=users.index(inuser)
        #找出密码列表中对应的索引值的密码
        passwd=passwds[index]
        #判断输入的密码是否正确
        if inpasswd==passwd:
            print('%s登录成功'%(inuser))
            break
        else:
            print('%s登录失败：密码错误！'%(inuser))
    else:
        print('用户%s不存在'%(inuser))
else:
    print('已经超过三次机会！')
'''
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
#无限循环
while True:
        # 输出操作选项信息
        print(info)
        choice = input('请输入选择：')
        if choice == '1':
            print('入栈'.center(50, '*'))  # 将字符串移到中间，center的第一个参数是返回字符串的长度，第二个参数是填补两侧缺失空间的字符
            # 接收入栈元素
            item = input('入栈元素：')
            # append：添加元素到列表中，将输入的item值添加到stack列表的末尾，入栈-》list.append
            stack.append(item)
            print('元素%s入栈成功' % item)
        # 要进行出栈操作，首先要判断列表的长度是否为0，为0就无法进行出栈
        elif choice == '2':
            if len(stack) == 0:
                print('栈为空，无法出栈')
            else:
                print('出栈'.center(50, '*'))
                # pop:删除列表中的最后一个元素  出栈-》list.pop
                item = stack.pop()
                print('%s元素出栈成功' % item)
        # 要输出栈顶元素，当列表的长度为0时，自然什么元素都没有，栈顶元素是列表的最后一个元素，
        elif choice == '3':
            # len:列表长度
            if len(stack) == 0:
                print('栈为空，无栈顶元素')
            else:
                print('栈顶元素为%s' % stack[-1])  # 栈顶元素->stack索引为-1的元素
        elif choice == '4':
            print('栈的长度为%s' % len(stack))  # 栈的长度就是列表的长度
        # 判断栈是否为空，也就是判断stack列表的长度是否为0
        elif choice == '5':
            if len(stack) == 0:
                print('栈为空')
            else:
                print('栈不为空')
        elif choice == 'q':
            break
        else:
            print('请输入正确的选择')  # 当choice输入的值不是1、2、3、4、5、q时，提示再次输入
'''
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
'''
print('管理员登录界面'.center(50,'*'))
#初始会员信息
users=['westos','linux']
passwds=['123','456']
#接收输入的用户名和密码
inuser=input('用户名：')
inpasswd=input('密码：')
if inuser=='admin':
    if inpasswd=='admin':
        print('管理员%s登录成功'%(inuser))
    while True:
        print("""
        **操作目录**
        1.添加会员信息
        2.删除会员信息
        3.查看会员信息
        4.退出
        """)
        option=input('请输入你想执行的操作：')
        if option=='1':
            print('添加会员信息')
            adduser=input('用户名：')
            addpasswd=input('密码：')
            if adduser in users:
                print('添加会员信息失败，该会员已存在')
            else:
                users.append(adduser)
                passwds.append(addpasswd)
                print('添加会员信息成功！')
        elif option=='2':
            print('删除会员信息')
            popuser=input('请输入要删除的会员用户名：')
            if popuser in users:
                index=users.index(popuser)
                users.pop(index)
                print('%s会员删除成功'%(popuser))
            else:
                print('该会议不存在，无法删除！')
        elif option=='3':
            print('查看会员信息')
            cuser=input('用户名：')
            if cuser in users:
                index = users.index(cuser)
                print(users[index])
                print(passwds[index])
            else:
                print('没有该会员信息')
        elif option=='4':
            break
        else:
            print('请输入正确的选择：')
    else:
        print('登录失败，密码错误')
else:
    print('用户不存在')
'''







