import os.path #os.path模块主要用于获取文件的属性

#print(os.path.abspath('os模块.py'))#获取文件的绝对路径
#print(os.path.exists('os模块.py'))#判断文件是否存在
#print(os.path.join('G:\\python','os模块.py'))#将目录和文件名拼接
#print(os.path.split('G:\\python\\project\\python\\os模块.py'))#将目录和文件名分离
#print(os.path.isdir('G:\\python\\project'))#判断路径是否是文件目录
#print(os.path.isabs('G:\\python\\project\\python\\os模块.py'))#判断路径是否是绝对路径
#print(os.path.isfile('os模块.py'))#判断是否是文件名
#print(os.path.splitext('os模块.py'))#分离文件名和扩展名，‘.’之前的是文件名，之后的是扩展名
#print(os.path.basename('G:\\python\\project\\python\\os模块.py'))#从文件路径中提取文件
#print(os.path.dirname('G:\\python\\project\\python\\os模块.py'))#从文件路径中提取文件目录
#print(os.path.isdir('G:\\python\\project\\python'))#判断是否为路径，不包括文件

'''
print(os.path.getatime('G:\\python\\project\\python\\os模块.py'))#返回文件路径最近访问时间
print(os.path.getctime('G:\\python\\project\\python\\os模块.py'))#返回文件路径创建时间
print(os.path.getmtime('G:\\python\\project\\python\\os模块.py'))#返回文件最近修改时间
print(os.path.getsize('G:\\python\\project\\python\\os模块.py'))#返回文件的大小
'''
