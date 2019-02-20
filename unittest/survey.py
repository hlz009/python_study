'''
匿名调查类
'''

class AnonymousSurvey():
    ''' 收集匿名调查问卷的答案 '''

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_result(self):
        print("Surey result")
        for response in self.responses:
            print("- " + response)
