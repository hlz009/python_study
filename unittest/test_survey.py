import unittest
from survey import AnonymousSurvey

'''
每完成一个单元测试 python打印一个字符
测试通过是一个句点.
测试引发错误是一个E
测试导致断言失败时一个F
因此打印句点的个数应该与测试方法的个数相等，才算测试通过
'''
class TestAnonmyousSurvey(unittest.TestCase):

    '''
    unittest.TestCase中包含setUp()方法，我们可以创建一些对象，并在每个测试方法中使用，
    python会先运行setUp()的方法
    '''
    def setUp(self):
        question = "what language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["chinese", "english", "spanish"]

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])

        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()