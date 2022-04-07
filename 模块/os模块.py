'''
import os
print(dir(os))#查看os模块有哪些类型
print(help(os))#查看os模块的帮助信息
'''
#os模块系统操作
'''
import os
print(os.getcwd())#输出当前工作路径
print(os.sep)#输出当前系统的分隔符
print(os.name)#指示你正在使用的工作平台
print(os.getenv('path'))#输出环境变量
print(os.system('mkdir today'))#执行系统命令
'''
#os模块目录增删改查
'''
import os
#os.mkdir('mulu')#创建目录
#os.makedirs('war/dr')#创建多级目录
#os.chdir('G:\BaiduNetdiskDownload\ex3')#修改当前工作目录
#print(os.getcwd())#获取当前工作目录
#os.rmdir('mulu')#删除目录
#os.removedirs('war/dr')#删除多级目录
#print(os.listdir('python'))#获取指定目录下的所有文件和目录
#os.rename('a.txt','bc.txt')#重命名文件名，第一个参数是指定要修改的文件或目录，第二个参数是修改后的文件名称
#os.renames('a','b')#跟rename()用法一致
os.remove('foo.txt')#删除文件
'''

#用os模块对文件进行操作
'''
import os
fd=os.open('fo1.txt',os.O_RDWR|os.O_CREAT)#os.O_RDWR|os.O_CREAT[读写模式|创建一个新的文件]
#s='this is test'
#s=s.encode(encoding='utf-8')
#os.write(fd,s)#第一个参数是文件对象，第二个参数是写入的内容【需要对内容进行编码转换】
#print(os.read(fd,12))#从文件fd中读取12个字节的内容
os.close(fd)
'''

#获取当前目录下的所有py文件
'''
import os
path=os.getcwd()
file=os.listdir(path)
for filename in file:
    if filename.endswith('.py'):
        print(filename)
'''

#获取当前目录下的所有文件和目录以及子目录
'''
import os
path=os.getcwd()
lst_file=os.walk(path) #os.walk()通过在目录树中游走输出在目录中的文件名，向上或者向下
for dirpath,dirname,filename in lst_file:
    for dir in dirname:
        print(os.path.join(dirpath,dir))
    for file in filename:
        print(os.path.join(dirpath,file))
'''

#获取py文件
'''
import os #导入文件处理模块os和os.path
import os.path
l=[]#用于存储后缀名.py的文件
def get_py(path,l):#获取指定目录下的py文件函数,在函数中引入path、l两个变量
    filelist=os.listdir(path)#获取输入文件路径下的所有文件和目录
    for filename in filelist:#遍历这些文件和目录
        pathTmp=os.path.join(path,filename)#定义一个变量，获取path与filename组合后的路径
        if os.path.isdir(pathTmp):#如果是目录
            get_py(pathTmp,l)#则递归查找，调用自定义的文件函数
        elif filename[-3:].upper()=='.PY':#不是目录，则比较后缀名
            l.append(pathTmp)#在列表末尾添加组合的路径变量
path=input('请输入路径：').strip()#定义一个获取文件目录的输入变量，并去除字符串两边的空白
get_py(path,l)#执行文件函数
print('在%s目录下及其子目录下找到%d个py文件\n分别为：\n'%(path,len(l)))#获取文件路径变量下的py文件，以及统计存储的.py文件列表的长度len(定义的列表)
for filepath in l:#遍历这个列表，每个.py文件换行单独输出
    print(filepath+'\n')
'''
#显示所有视频格式文件，mp4，avi，rmvb
'''
import os#导入文件模块os
def search_file(start_dir,target):#定义获取指定格式的文件的函数，引入定义的输入路径变量(start_dir)和存储后缀名为‘.mp4','.avi','.rmvb'格式的文件列表
    os.chdir(start_dir)#修改定义的输入路径变量
    for each_file in os.listdir(os.curdir):#遍历返回当前目录(os.curdir)下的所有文件和目录
        ext=os.path.splitext(each_file)[1]#分离each_file的文件名和扩展名，取这个元组的扩展名
        if ext in target:#如果扩展名在指定格式的文件列表中
            vedio_list.append(os.getcwd()+os.sep+each_file+os.linesep)#再创建一个列表，在它的列表末尾添加(获取当前工作目录+文件分隔符os.sep+遍历的文件变量+文件末尾分隔符os.linesep)
        if os.path.isdir(each_file):#如果遍历的文件变量是目录(os.path.isdir)
            search_file(each_file,target)#递归调用
            os.chdir(os.pardir)#递归调用后切记返回上一层目录【os.pardir返回当前目录的父目录】
start_dir=input('请输入待查找的初始目录：')#创建获取输入路径的变量
program_dir=os.getcwd()#定义一个变量来获取当前工作目录
target=['.mp4','.avi','.rmvb']#创建一个后缀名为'.mp4','.avi','.rmvb'的列表
vedio_list=[]#创建一个空列表，来添加指定格式的文件
search_file(start_dir,target)#执行获取指定格式的文件函数
f=open(program_dir+os.sep+'vediolist.txt','w',encoding='utf-8')#创建一个文件变量f(获取当前工作目录的变量+文件分隔符+文件名，文件读取方式[只读]，字符编码encoding='utf-8')
f.writelines(vedio_list)#向文件变量f中写入保存的指定格式文件列表(file.writelines)
f.close()#关闭文件
'''
#把混乱的文件名改成有序的文件名
'''
import os#导入文件模块
path=input('请输入文件路径(结尾加上/)：')#定义一个变量获取文件路径
filelist=os.listdir(path)#获取该目录下的所有文件，存入filelst中
n=0#定义一个对文件进行排序的初始值变量n=0
for i in filelist:#遍历filelst
    oldname=path+os.sep+filelist[n]#设置旧文件名(os.sep添加系统分隔符)文件路径+文件分隔符+filelst[n]
    newname=path+os.sep+'a'+str(n+1)+'.JPG'#设置新文件名 文件路径+文件分隔符+字符串'a'+字符串格式的n+1(str(n+1))+文件后缀名’.jpg‘
    os.rename(oldname,newname)#用os模块中的rename方法对文件改名,将oldname改为newname
    print(oldname,'====>',newname)#输出oldname到newname
    n+=1#排序变量n递增
'''
#os.replace(old,new)给文件重命名
'''
import os
#将1.txt文件名改为2.txt,并将最后一个2.txt文件删除
os.replace('1.txt','2.txt')#执行后，只剩2.txt
'''


