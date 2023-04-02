

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        return self.answer == answer
        

q1 = ('En iyi programlama dili hangisidir?'  , ['python', 'java', 'c#', 'javascript'] , 'python')
q2 = ('En popüler programlama dili hangisidir?'  , ['python', 'java', 'javascript', 'c#'] , 'python')
q3 = ('En kazandıran programlama dili hangisidir?'  , ['java','python', 'c#', 'javascript'] , 'python')
questions = [q1, q2, q3]


print(q1.checkAnswer('python'))
print(q2.checkAnswer('c#'))


# quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[quiz.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1} : {questionText}')

        for q in questions.choices:
            print('-' + q)

        answer = input('cevap:')
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer)
            self.score +=1
        self.questionIndex +=1

        self.displayQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex
            self.showScore()

        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('score:')

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion
            print('Quiz bitti!')
        else:
            print(f'Question{questionNumber} of {totalQuestion}' .center)


    
q1 = ('En iyi programlama dili hangisidir?'  , ['python', 'java', 'c#', 'javascript'] , 'python')
q2 = ('En popüler programlama dili hangisidir?'  , ['python', 'java', 'javascript', 'c#'] , 'python')
q3 = ('En kazandıran programlama dili hangisidir?'  , ['java','python', 'c#', 'javascript'] , 'python')
questions = [q1, q2, q3]

quiz = Quiz(questions)
question = quiz.questions[quiz.questionIndex]
print(question.text)



