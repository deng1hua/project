#检测文件的权限模式
'''
import os,sys
ret=os.access('/e.txt',os.F_OK)
print('F_OK-返回值%s'%ret)
ret=os.access('/e.txt',os.R_OK)
print('R_OK-返回值%s'%ret)
ret=os.access('/e.txt',os.W_OK)
print('W_OK-返回值%s'%ret)
ret=os.access('/e.txt',os.X_OK)
print('X_OK-返回值%s'%ret)
'''
#改变当前工作目录到指定的路径
'''
import os, sys
# 查看当前工作目录
retval = os.getcwd()
print ("当前工作目录为 %s" % retval)
# 修改当前工作目录
os.chdir('G:/users')
# 查看修改后的工作目录
retval = os.getcwd()
print ("目录修改成功 %s" % retval)
'''
#设置路径的标记为数字标记,只在unix中有效
'''
import os,stat
path = "/tmp/foo.txt"
flags = stat.SF_NOUNLINK
retval = os.chflags( path, flags )
print ("返回值: %s" % retval)
'''
#更改文件或目录的权限
'''
import os,sys,stat
os.chmod('/e.txt',stat.S_IXGRP)
os.chmod('/e.txt',stat.S_IWOTH)
print('修改成功')
'''
#用于更改文件所有者，如果不修改可以设置为 -1, 你需要超级用户权限来执行权限修改操作(只支持在Unix下使用)
'''
import os,sys
os.chown('/e.txt',100,-1)
print('修改权限成功')
'''
#更改当前进程的根目录为指定的目录，使用该函数需要管理员权限。在 unix 中有效。
'''
import os,sys
os.chroot('/temp')
print('修改根目录成功')
'''
#关闭指定的文件描述符fd
'''
import os,sys
fd=os.open('e.txt',os.O_RDWR|os.O_CREAT)
str='this is test'
str=str.encode()
os.write(fd,str)
os.close(fd)
print('关闭文件成功')
'''
#关闭所有文件描述符 fd，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略。
'''
import os,sys
fd=os.open('e.txt',os.O_RDWR|os.O_CREAT)
str='this is test'
str=str.encode()
os.write(fd,str)
os.closerange(fd,fd)
print('关闭文件成功')
'''
#于复制文件描述符 fd。
'''
import os,sys
fd=os.open('/e.txt',os.O_RDWR|os.O_CREAT)
d_fd=os.dup(fd)
os.write(d_fd,'this is test'.encode())
os.closerange(fd,d_fd)
print('关闭所有文件成功')
'''
#将一个文件描述符 fd 复制到另一个 fd2.Unix, Windows 上可用
'''
import os
f=open('e.txt','a')
os.dup2(f.fileno(),1)
f.close()
print('runoob')
print('google')
'''
#通过文件描述符改变当前工作目录。Unix 上可用。
'''
import os, sys
# 首先到目录 "/var/www/html"
os.chdir("/var/www/html" )
# 输出当前目录
print ("当前工作目录为 : %s" % os.getcwd())
# 打开新目录 "/tmp"
fd = os.open( "/tmp", os.O_RDONLY )
# 使用 os.fchdir() 方法修改到新目录
os.fchdir(fd)
# 输出当前目录
print ("当前工作目录为 : %s" % os.getcwd())
# 关闭打开的目录
os.close( fd )
'''
#改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。Unix上可用。
'''
import os, sys, stat
# 打开文件 "/tmp/foo.txt"
fd = os.open( "/tmp", os.O_RDONLY )
# 设置文件可通过组执行
os.fchmod( fd, stat.S_IXGRP)
# 设置文件可被其他用户写入
os.fchmod(fd, stat.S_IWOTH)
print ("修改权限成功!!")
# 关闭文件
os.close( fd )
'''
#修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。Unix上可用。
'''
import os, sys, stat
# 打开文件 "/tmp/foo.txt"
fd = os.open("/tmp", os.O_RDONLY)
# 设置文件的用户 id 为 100
os.fchown(fd, 100, -1)
# 设置文件的用户组 id 为 50
os.fchown(fd, -1, 50)
print("修改权限成功!!")
# 关闭文件
os.close(fd)
'''
#强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。如果你需要刷新缓冲区可以使用该方法。
# Unix上可用。
'''
import os, sys
# 打开文件 "/tmp/foo.txt"
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
# 写入字符串
os.write(fd, "This is test".encode())
# 使用 fdatasync() 方法
os.fdatasync(fd)
# 读取文件
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print ("读取的字符是 : ", str)
# 关闭文件
os.close( fd )
print ("关闭文件成功!!")
'''
#通过文件描述符 fd 创建一个文件对象，并返回这个文件对象。
#该方法是内置函数 open() 的别名，可以接收一样的参数，唯一的区别是 fdopen() 的第一个参数必须是整型。
'''
import os,sys
fd=os.open('e.txt',os.O_RDWR|os.O_CREAT)#打开文件
fo=os.fdopen(fd,'w+')#获取以上文件的对象
print('current I/O pointer position:%d'%fo.tell())#获取当前位置
fo.write('python is a great language.\nyeah its great!\n')#写入字符串
#读取内容
os.lseek(fd,0,0)
str=os.read(fd,100)
print('read string is:',str)
#获取当前位置
print('current I/O pointer positon:%d'%fo.tell())
#关闭文件
os.close(fd)
print('关闭文件成功')
'''
#返回一个打开的文件的系统配置信息。Unix上可用。
'''
import os, sys
# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
print ("%s" % os.pathconf_names)
# 获取最大文件连接数
no = os.fpathconf(fd, 'PC_LINK_MAX')
print ("文件最大连接数为 :%d" % no)
# 获取文件名最大长度
no = os.fpathconf(fd, 'PC_NAME_MAX')
print ("文件名最大长度为 :%d" % no)
# 关闭文件
os.close( fd )
print ("关闭文件成功!!")
'''
#返回文件描述符fd的状态，类似 stat()。Unix，Windows上可用。
'''
import os,sys
#打开文件
fd=os.open('e.txt',os.O_RDWR|os.O_CREAT)
#获取元组
info=os.fstat(fd)
print('文件信息:',info)
#获取文件uid
print('文件uid为:%d'%info.st_uid)
#获取文件gid
print('文件gid为:%d'%info.st_gid)
#关闭文件
os.close(fd)
'''
#