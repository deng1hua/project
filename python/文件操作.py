#文件打开模式
'''
'w'只写模式，只能向文件写入内容；
'r'只读模式，只能读取文件；
'a'追加模式，向文件追加写入内容，如果文件中有内容，会在它之后添加写入的内容
'rb'以二进制的格式读取内容，一般用于非文本文件
'wb'以二进制的格式写入内容，一般用于非文本文件
'''
#向文件写入内容
'''
f=open('a.txt','w',encoding='utf-8') #open()函数打开一个文件，第一个参数指定文件名，第二个参数指定打开方式，第三个参数指定编码格式
#f.write('这是一个测试文件')#.write()向文件写入内容
print(f.writable())#判断文件是否可写
s='python'
f.writelines(s)#将一个字符串序列写入文件
f.close() #关闭文件
'''
#读取文件的内容
'''
f=open('a.txt','r',encoding='utf-8')
#print(f.read())#读取文件所有内容
#print(f.readline(2))#读取文件一行内容,加了一个非负数参数2，则读取一行的前2个字节的内容
#print(f.readlines())#读取文件所有内容，转换为一个每行作为一个元素的列表【包含换行符】
#print(f.readable())#判断文件是否可读
f.close()
'''
#向文件追加内容
'''
f=open('a.txt','a',encoding='utf-8')
f.write('\n这是一个测试文件')#在已有内容的下一行写入内容
f.close()
'''
'''
f=open('a.txt','r',encoding='utf-8')
print(f.tell())#获取文件当前所在位置
f.seek(2)#将文件指针定位到2
print(f.tell())
print(f.seekable())#判断文件在python中是否可搜索
print(f.fileno())#返回一个整型的文件描述符
f.flush()#刷新文件缓冲区
print(f.isatty())#检测文件是否连接到一个终端设备
f.truncate()#截断文件，如果指定了size则表示截断siaze个字节符
print(f.read())
f.close()
'''
#上下文管理器,使用with打开文件，不需要再主动关闭文件，自动释放内存
'''
with open('a.txt','r',encoding='utf-8') as f:
    print(f.read())
'''
#复制文件
'''
f=open('a.txt','r',encoding='utf-8')
f1=open('a1.txt','w',encoding='utf-8')
f1.write(f.read())
f.close()
f1.close()
'''
#使用上下文管理器复制文件
'''
with open('a.txt','r',encoding='utf-8') as f:
    with open('a2.txt','w',encoding='utf-8') as f1:
        f1.write(f.read())
'''
#使用json模块保存数据到文件
'''
import json
name=input('name: ')
with open('a.txt','w') as f:
    json.dump(name,f) #将name变量的值写入f文件对象,json.dump()第一个参数是要保存到文件中的对象，第二个参数是文件对象
'''
#使用json模块读取文件内容
'''
import json
with open('a.txt') as f:
    print(json.load(f)) #json.load()读取文件内容，有一个参数是文件对象
'''

#获取用户名，如果文件存在，就读取文件内容并打印；如果不存在，就提示输入用户名，并把用户名写入文件
'''
import json
def get_stored_username(filename):
    "如果存储了用户名，就获取它"
    try: #将读取文件的代码放在try内
        with open(filename) as f:
            username=json.load(f)
    except FileNotFoundError: #读取的文件不存在，就捕获这个错误，并返回None
        return None
    else: #文件存在，就返回读取的内容
        return username
def get_new_username(filename):
    "没有用户，提示输入用户名"
    username=input('What is your name? ')
    with open(filename,'w') as f: #将输入的用户名写入文件
        json.dump(username,f)
    return username
def greet_user(filename):
    "获取用户，并指出其名字"
    username=get_stored_username(filename) #调用第一个函数，读取文件内容
    if username: #如果文件存在，输出指定的操作
        print(f'welcome back,{username}')
    else: #否则，调用第二个函数提示输入用户名并把用户名写入文件，再打印指定的内容
        username=get_new_username(filename)
        print(f"we'll remember you when you come back,{username}")

greet_user('cv.txt')
'''

