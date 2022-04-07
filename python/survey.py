
class AnonymousSurvey:
    def __init__(self,question):
        self.question=question
        self.responses=[]
    def show_question(self):
        print(self.question)
    def store_response(self,new_response):
        self.responses.append(new_response)
    def show_results(self):
        print('Survey Results:')
        for response in self.responses:
            print(f'- {response}')

class Employee:
    def __init__(self,first,last,money):
        self.first=first
        self.last=last
        self.money=money
    def give_raise(self,sais=5000):
        self.money+=sais


