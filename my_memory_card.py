from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import randint, shuffle 

class Question():
    '''contains a question, a correct answer and three incorrect ones'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3, wrong4):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.wrong4 = wrong4

questions_list = [] 
questions_list.append(
        Question('Official language of Romania', 'Hungarian', 'English', 'Moldovan', 'French', 'Romanian'))
questions_list.append(
        Question('How many colors are in the rainbow?', '3', '6', '7', '8', '12'))
questions_list.append(
        Question('What is the biggest city in the world?', 'Botoșani', 'Budapest', 'London', 'Tokyo', 'New York'))
questions_list.append(
        Question('What is the most spoken language in the world?', 'English', 'Mandarin' , 'French', 'Cantoneese', 'Japanese'))
questions_list.append(
        Question('What country has the most pyramids', 'Egypt', 'Sudan', 'England', 'Saudi Arabia', 'Israel'))
questions_list.append(
        Question('In what year did the Soviet Union collapse?', '1991', '2020', '1990', '1987', '1978'))



app = QApplication([])

btn_OK = QPushButton('Reply')
lb_Question = QLabel('The most difficult question in the world!') 

RadioGroupBox = QGroupBox("Answer options")  

rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')
rbtn_5 = QRadioButton('Option 5')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
RadioGroup.addButton(rbtn_5)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans4 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)  
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans4.addWidget(rbtn_5)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)  
layout_ans1.addLayout(layout_ans4)
RadioGroupBox.setLayout(layout_ans1) 


AnsGroupBox = QGroupBox("Test results")
lb_Result = QLabel('are you right or not?') 
lb_Correct = QLabel('answer will be here!') 

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 

layout_line3.addStretch(1)


layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spaces between the content elements
def show_result():
    ''' show answer panel '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next')



def show_question():
    ''' show question panel '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Reply')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    rbtn_5.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4, rbtn_5]

def ask(q: Question):
    ''' the function writes the values of the question and answers to the corresponding widgets, 
    at the same time the answer options are distributed randomly'''
    shuffle(answers) 
    answers[0].setText(q.right_answer) 
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    answers[4].setText(q.wrong4)
    lb_Question.setText(q.question) 
    lb_Correct.setText(q.right_answer) 
    show_question() 

def show_correct(res):
    ''' show the result - set the text passed to the "result" inscription and show the panel we need '''
    lb_Result.setText(res)
    show_result()

def check_answer():
    ''' if any answer option is chosen, we need to check and show the answer panel'''
    if answers[0].isChecked():
        
        show_correct('Right!')
        window.score += 1
        print('Statistics\n-Total questions: ', window.total, '\n-Right answers: ', window.score)
        print('Rating: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # wrong answer!
            show_correct('Wrong answer!')
            print('Rating: ', (window.score/window.total*100), '%')
    

def next_question():
    ''' asks a random question from the list '''
    window.total += 1
    print('Statistics\n-Total questions: ', window.total, '\n-Right answers: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)  
                                                       
    q = questions_list[cur_question] 
    ask(q) 

def click_OK():
    ''' determines whether to show another question or check the answer to this one '''
    if btn_OK.text() == 'Answer':
        check_answer() 
    else:
        next_question() 

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

btn_OK.clicked.connect(click_OK) 

window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()
