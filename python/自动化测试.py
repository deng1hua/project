#自动化测试模块unittest
'''
import unittest
from name import get_formatted_name
class TestNameCase(unittest.TestCase): #创建一个测试类，用于对get_formatted_name函数进行单元测试，该类继承unittest.TestCase类
    def testformattedname(self): #创建测试这个函数的方法
        formatted_name=get_formatted_name('deng','hua') #调用函数传入两个参数，并复制给变量formatted_name
        self.assertEqual(formatted_name,'Deng Hua') #调用测试类的assertEqual方法，判断这个变量的值是否和预期的输出值相等
    def testmiddlename(self):
        formatted_middle_name=get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_middle_name,'Wolfgang Amadeus Mozart')

if __name__=='__main__': #检查特殊变量__name__，如果这个文件作为主程序运行，变量__name__被设置为'__main__';如果这个文件被测试框架导入，变量__name__的值就不会是'__main__'，因此不会调用unittest.main()
    unittest.main() #调用unittest模块的main()运行测试用例
'''
#运行结果
'''
. #一个'.'表示测试通过了
----------------------------------------------------------------------
Ran 1 test in 0.000s #表示运行了一个测试，消耗时间0.000s

OK #该测试用例中的所有单元测试都通过了
'''
#测试包含城市、国家的函数fun
'''
import unittest
from city import fun
class TestFunCase(unittest.TestCase):
    def testfull_name(self): #测试没添加population参数的函数
        fullname=fun('santiago','chile')
        self.assertEqual(fullname,'Santiago,Chile')
    def testpopulation(self): #测试添加了population参数的函数
        fullname=fun('santiago','chile',5000000)
        self.assertEqual(fullname,'Santiago,Chile - Population 5000000')

if __name__=='__main__':
    unittest.main()
'''
#测试AnonymousSurvey类
'''
import unittest
from survey import AnonymousSurvey
class TestSurveyCase(unittest.TestCase):
    def test_survey(self):
        question='What language did you when you learn to speak?'
        my_survey=AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)
    def test_three_survey(self):
        question = 'What language did you when you learn to speak?'
        my_survey = AnonymousSurvey(question)
        responses=['English','Japanese','France']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)
if __name__=='__main__':
    unittest.main()
'''
#包含setUp()方法测试类
'''
import unittest
from survey import AnonymousSurvey
class TestSurveyCase(unittest.TestCase):
    def setUp(self):
        question = 'What language did you when you learn to speak?'
        self.my_survey=AnonymousSurvey(question)
        self.responses=['English','Japanese','France']
    def test_survey(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.responses)
    def test_three_survey(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.responses)
if __name__=='__main__':
    unittest.main()
'''
#测试Employee类
'''
import unittest
from survey import Employee
class TestEmployeeCase(unittest.TestCase):
    def setUp(self):
        self.employee=Employee('deng','hua',3000)
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.money,8000)
    def test_give_custom_raise(self):
        self.employee.give_raise(2000)
        self.assertEqual(self.employee.money,5000)

if __name__=='__main__':
    unittest.main()
'''

