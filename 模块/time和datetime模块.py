#日期和时间模块datetime
'''
from datetime import date
#显示今天的时间
now=date.today()
print(now)
#显示今天是这个月的第几天和星期
print(now.strftime("%m-%d-%y.%d %b %Y is a %A on the %d day of %B"))
birthday=date(1964,7,31)
age=now-birthday
print(age.days)
'''
#对days,seconds,microseconds以外的任何参数进行合并操作，并标准化为以上三个结果属性
'''
from datetime import timedelta
delta=timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)
'''
'''
*import datetime
#获取最小年份数
print(datetime.MINYEAR)
#获取最大年份数
print(datetime.MAXYEAR)
'''


#datetime模块中的date(日期)
'''
from datetime import date
g=date(2013,12,21)#定义年的函数，year、month、day参数都必须有
print(g)#2013-12-21
'''
import time
from datetime import date
#date.fromordinal()返回与格列高利历序号对应的日期，其中序号为1是公元1年1月1日
print(date.fromordinal(99))
#date.fromtimestamp()返回与时间戳对应的日期
print(date.fromtimestamp(time.time()))
#date.fromisoformat()返回一个对应于以 YYYY-MM-DD 格式给出的时间字符串的date对象
print(date.fromisoformat('2002-11-12'))
#date.isoformat()返回一个与date日期对象相对应的时间字符串
print(date(2002,1,12).isoformat())
#date.min最小的日期
print(date.min)
#date.max最大的日期
print(date.max)
#date.resolution两个日期对象的最小间隔
print(date.resolution)
#date.year
print(date.year)
#date.replace修改date的时间
d=date(2005,12,31)
print(d.replace(day=26))
#date.timetuple返回一个date对象的时间元组struct_time，hours, minutes 和 seconds 值均为 0，且 DST 旗标值为 -1
print(date.timetuple(date(2009,12,13)))
#date.toordinal返回日期对应的格列高利历序号，其中公元1年1月1日的序号是1
print(date.toordinal(date(2021,9,11)))
#date.weekday返回一个整数代表星期几，0是星期一，6是星期天
print(date(2021,9,11).weekday())
#date.isoweekday返回一个整数代表星期几，1是星期一，7是星期天
print(date(2021,9,11).isoweekday())
#date.isocalendar返回一个年、一年的第几周和这周的第几天
print(date(2021,9,12).isocalendar())
#date._str_等价于date.isoformat
d=date(2016,9,19)
print(str(d))
#date.ctime()返回一个表示日期的字符串
print(date(2016,9,19).ctime())
#date.strftime返回一个自定义格式的日期字符串
print(date(2016,9,19).strftime('%Y-%m-%d'))

'''
from datetime import datetime,timezone
print(datetime(2019,5,18,15,17,8,132263).isoformat())#t为单个分割字符，会被放在日期和时间之间
print(datetime(2019,5,18,15,17,tzinfo=timezone.utc).isoformat())

#str(datetime对象)等价于datetime.isoformat(' ')
d=datetime(2019,5,18,15,17,8,132263)
print(str(d))

#datetime.ctime返回一个表示日期和时间的字符串,它等效于time.ctime(time.mktime(d.timetuple)))
print(datetime(2002,12,4,20,30,40).ctime())

#datetime.strftime返回一个自定义格式字符串所指明的代表日期和时间的字符串
print(datetime(2002,12,4,20,30,40).strftime("%a %b %d %H:%M:%S"))

#datetime.strptime返回日期和时间字符串对应的元组
print(datetime.strptime('Wed Dec 04 20:30:40','%a %b %d %H:%M:%S'))
'''



#datetime模块中的time(时间)





#datetime模块中的timedelta(两个日期或时间之间的间隔)
'''
from datetime import timedelta
delta=timedelta(days=50,seconds=27,microseconds=10,milliseconds=29000,minutes=5,hours=8,weeks=2)
print(delta)

print(delta.resolution)#两个不相等timedelta之间的最小间隔



#两个timedelta之间进行比较，总是返回布尔值（true或false）
d2=timedelta(hours=12)
print(delta!=d2)
print(delta>d2)



#当timedelta对象和其它类型的数据进行比较，会报类型错误
#print(delta>2)
#在布尔运算中，timedelta 对象当且仅当其不等于 timedelta(0) 时则会被视为真值。



#返回时间间隔包含了多少秒
print(delta.total_seconds())
'''
#timedelta算术运算
'''
from datetime import timedelta
year=timedelta(days=365)
ten_years=10*year
print(ten_years.days)
print(ten_years.days//365)
print(ten_years.days-year.days)
print((ten_years.days-year.days)//3)
'''
#




#time模块
'''
import time
#获取当前时间戳
now=time.time()
print('当前时间戳为：%s'%now)

#获取当前时间，只需要将当前时间戳传递给time的localtime函数
localtime=time.localtime(time.time())
print(localtime)
#time.struct_time(tm_year=2021, tm_mon=9, tm_mday=3, tm_hour=21, tm_min=59, tm_sec=43, tm_wday=4, tm_yday=246, tm_isdst=0)
#struct_time是处理时间的元组，tm_year是四位数年,tm_mon是月,tm_mday是日,tm_hour是小时,tm_min是分钟,tm_sec是秒,tm_wday是一周的第几日,tm_yday是一年的第几日,tm_isdst是夏令时

#最简单获取可读的时间模式的函数asctime()
time2=time.asctime(time.localtime(time.time()))
print('本地时间为：',time2)

#格式化日期strftime
#格式化成2016-03-20 11：45：39形式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

#格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))
#将格式字符串转换为时间戳
a="Sat Mar 28 22:24:24 2016"
#mktime是localtime的反函数，返回一个浮点数
#strptime将时间字符串转换为时间元组
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))#将a这个时间字符串转换为时间元组，然后将这个时间元组转换为时间戳
'''
#Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历
#time.clock()方法用以浮点数计算的秒数返回当前的CPU时间
'''
import time
def procedure():
    time.sleep(2.5)
t0=time.clock()
procedure()
print(time.clock() - t0,"seconds process time")
t0=time.time()
procedure()
print(time.time() - t0,"seconds wall time")
'''
#time.ctime()方法,把一个时间戳转化为time.asctime()的形式，如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于 asctime(localtime(secs))
#import time
#print("time.ctime() : %s"%time.ctime())
#time.gmtime()接收时间戳并返回格林威治天文时间下的时间元组
'''
import time
#print('time.gmtime() : %s' % time.gmtime())
print(time.gmtime())
'''
#time.localtime()接收时间戳并返回本地的时间元组
'''
import time
print(time.localtime(time.time()))
'''
#time.mktime()接收时间元组返回时间戳
'''
import time
print(time.mktime(time.localtime(time.time())))
'''
#time.sleep()推迟调用线程的运行,表示进程挂起的时间
'''
import time
print('start: %s'%time.time())
time.sleep(5)
print('end: %s'%time.time())
'''
#time.tzset()根据环境变量tz重新初始化时间相关设置（windows环境下time模块没有tzset函数）
'''
import time
import os
os.environ['TZ']='EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))
os.environ['TZ']='AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))
'''




