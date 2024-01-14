from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

from random import choice, shuffle

app = QApplication([]) #сторюємо віконний додаток

from window import *

class Question():
    current = None

    def __init__(self, text, right_ans, ans2, ans3, ans4):
        self.text = text
        self.right_ans = right_ans
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        
question = [
    Question("вісім", "eiqht", "eit", "eghite", "nine"),
    Question("чотири", "four", "fore", "fruin", "fif"),
    Question("сім", "seven", "sivn", "sevine", "sevni"),
    Question("девять", "nine", "eit", "lol", "neni"),
    Question("сто", "one hundret", "eit", "sto","hundrut"),
]
radio_list = [btn1, btn2, btn3, btn4]

win = QWidget() # створємо вікно
win.resize(600, 300)
win.setWindowTitle("Memori card")
win.setLayout(main_line)

def next_question():
    Question.current = choice(question)
    question_lb.setText(Question.current.text)
    shuffle(radio_list)
    radio_list[0].setText(Question.current.right_ans)
    radio_list[1].setText(Question.current.ans2)
    radio_list[2].setText(Question.current.ans3)
    radio_list[3].setText(Question.current.ans4)


def answer_click():
    if answer_btn.text() == "Відповісти":
        group_box.hide()
        result_box.show()
        answer_btn.setText("Наступне питання")
    else:
        next_question()
        group_box.show()
        result_box.hide()
        answer_btn.setText("Відповісти")
        

answer_btn.clicked.connect(answer_click)

# в кінці
next_question()
win.show() #показує вікно
app.exec_() # запускаємо додаток