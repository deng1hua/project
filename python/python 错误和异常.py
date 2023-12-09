#print(10/0)#0不能作为除数触发异常
#print(4+spam)#spam未定义触发异常
#print('2'+20)#字符串不能和整型相加
#try->except异常捕捉，当输入的数据错误时，except会捕捉指定的异常
'''
while True:
    try:
        x=int(input('请输入一个数字：'))
        break
    except ValueError:
        print('你输入的不是数字，请重新输入：')
'''
#一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组

#except (RuntimeError, TypeError, NameError):
 #   pass
'''
def model_exception(x,y):
    try:
        a=x/y
    except (ZeroDivisionError,ValueError,TypeError):
        print('one of ZeroDivisionError,ValueError,TypeError happend')
model_exception(1,0)
'''
#捕获所有异常
'''
try:
    ...
except Exception as e: #当不知道具体的异常的类型时，可以直接捕获Exception，输出当前程序运行产生的异常
    print(e)
'''
'''
#最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
import sys
try:
    f=open('e.txt')
    s=f.readline()
    i=int(s.strip())
except OSError as err:
    print('OS error:{0}'.format(err))
except ValueError:
    print('Could not convert data to an integer')
except:
    print('Unexcepted error:',sys.exc_info()[0])#exc_info()方法会将当前的异常信息以元组的形式返回，元组包含异常类型的名称、捕获到的异常实例和一个traceback对象
    raise
'''
#在 try 语句中判断文件是否可以打开，如果打开文件时正常的没有发生异常则执行 else 部分的语句
'''

try:
     f=open('e.txt','r')
except IOError:
    print('cannot open',arg)
else:
     print('has',len(f.readlines()),'lines')
     f.close()
'''
#异常处理并不仅仅处理那些直接发生在 try 子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。
'''
def number():
    x=1/0
try:
    number()
except Exception as e:
    print(e)
'''
#finally无论是否发生异常都会执行
'''
try:
    x=1/0
except Exception as e:
    print(e)
else:
    print(x)
finally:
    print('whenever do')
'''
#使用raise语句抛出一个指定的异常
'''
x=10
if x>5:
    raise Exception('x 不能大于5.x的值为：{}'.format(x))
'''
#如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出
'''
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by')
    raise
'''
#可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承
'''
class Myerror(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)
try:
    raise Myerror(2*2)
except Myerror as e:
    print('My exception occured,vlaue:',e.value)
raise Myerror('oops!')
'''
#有异常时，执行try->except->finally语句；没有异常时，执行try->else->finally语句
'''
def divide():
    x=int(input('请输入一个数：'))
    y=int(input('请输入另一个数：'))
    try:
        result=x/y
    except ZeroDivisionError:
        print('divison by zero')
    else:
        print('result is',result)
    finally:
        print('executing finally clause')
divide()
'''
#使用关键词with语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
'''
with open('e.txt') as f:
    for line in f:
        print(line,end='')
'''
#assert用于判断一个表达式在为false时触发异常(断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况)
#assert True#条件为true时正常执行
#assert False#条件为false时触发异常
#assert 1==1
#assert 1==2,'1不等于2'
#在 python3 中，处理带有参数的异常
'''
def f(var):
    try:
        return int(var)
    except (ValueError) as ae:
        print('参数无法转换为数字类型\n',ae)#ae返回错误的具体信息
print(f(1))
print(f('1'))
print(f('var'))
'''
#使用traceback模块查看异常信息
'''
import traceback
try:
    1/0
except Exception as e:
    traceback.print_exc(file=open('e.txt','w+',encoding='utf-8'))
    #print_exc打印具体的异常信息，并将异常信息写入到e.txt文件
'''
#raise主动触发异常
'''
def not_zero(num):
    try:
        if num==0:
            raise ValueError('参数错误')
        return num
    except Exception as e:
        print(e)
not_zero(0)
'''
#format_exc()打印异常信息，返回一个字符串类型的错误信息
'''
import traceback
try:
    import c
except:
    i=traceback.format_exc()
    print(i)
'''
#自定义上下文管理器
'''
class Test:
    def __enter__(self):
        print('enter')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self,exc_type,exc_val,exc_tb)
        import traceback
        print(traceback.extract_tb(exc_tb))#提取追踪信息
        print('exit')
        return True #加该语句就会把异常信息传递给exit方法，不会再次抛出异常
with Test() as e: #e是enter方法的返回值
    #print('body',e)
    1/0
'''
#contextlib模块
'''
import contextlib
@contextlib.contextmanager
def test():
    print(1) #相当于上下文管理器中的enter方法
    yield 'xxx'
    print(2) #相当于上下文管理器的exit方法
with test() as x: #x是上下文管理器中的enter方法的返回值
    print(3,x)
'''
#处理多个相同的异常
'''
import contextlib
@contextlib.contextmanager
def text():
    try:
        yield
    except ZeroDivisionError as e:
        print('error:',e)
x=1
y=0
with text(): #调用上下文管理器text()函数，try相当于enter函数，except相当于exit函数
    x/y #y为0会报错，执行except中的内容
a=2
b=0
with text():
    a/b
'''
#contextlib.closing方法，让一个拥有close方法的对象改变为上下文管理器对象
'''
class te:
    def t(self):
        print('tttt')
    def close(self):
        print('资源释放')
import contextlib
with contextlib.closing(te()) as t_obj:
    t_obj.t()
'''
#打开一个文件向另一个文件写入内容，可以两个open函数写在同一行，使用 ，分割
'''
with open('e.txt','r',encoding='utf-8') as f,open('e1.txt','w',encoding='utf-8') as t:
    f1=f.read()
    t1=t.write(f1)
'''
#手动抛出异常
'''
def f(i):
    if i<0:
        raise ValueError('值错误')
    else:
        print(i)
#通过try...except捕获异常
try:
    f(-1)
except ValueError as e:
    print('error',e)
'''




