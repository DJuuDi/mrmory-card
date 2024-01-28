from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

meny_win = QWidget() # створємо вікно
meny_win.resize(600, 300)
meny_win.setWindowTitle("Memory Card Menu")

title_lb = QLabel("Статистика")
count_lb = QLabel("Разів відповідали: ")
right_lb = QLabel("Правильних відповідей: ")
succes_lb = QLabel("Успішність: ")

back_btn  = QPushButton("Назад")
v_line = QVBoxLayout()
v_line.addWidget(title_lb)
v_line.addWidget(count_lb)
v_line.addWidget(right_lb)
v_line.addWidget(succes_lb)
v_line.addWidget(back_btn)

meny_win.setLayout(v_line)