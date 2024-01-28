from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

from random import choice, shuffle
from time import sleep

app = QApplication([]) #сторюємо віконний додаток

from window import *
from menu import *

class Question():
    current = None
    count_ans = 0
    count_right_ans = 0

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

def check_answer():
    Question.count_ans += 1
    if radio_list[0].isChecked():
        Question.count_right_ans += 1
        result_text.setText("Правильно, молодець")
    else:
        result_text.setText("Неправильно, нічо")

    radio_group.setExclusive(False)
    for btn in radio_list:
        btn.setChecked(False)
    radio_group.setExclusive(True)

def answer_click():
    if answer_btn.text() == "Відповісти":
        check_answer()
        group_box.hide()
        result_box.show()
        answer_btn.setText("Наступне питання")
    else:
        next_question()
        group_box.show()
        result_box.hide()
        answer_btn.setText("Відповісти")
        
def show_menu():
    count_lb.setText("Разів відповідали: " + str(Question.count_ans))
    right_lb.setText("Правильних відповідей: " + str(Question.count_right_ans))
    try: 
        success = round(Question.count_right_ans / Question.count_ans * 100, 2)
    except:
        success = 0
    succes_lb.setText("Успішність: " + str(success))
    win.hide()
    meny_win.show()

def hide_menu():
    win.show()
    meny_win.hide()

answer_btn.clicked.connect(answer_click)
menu_btn.clicked.connect(show_menu)
back_btn.clicked.connect(hide_menu)

# в кінці
next_question()
win.show() #показує вікно
app.exec_() # запускаємо додаток