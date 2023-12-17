from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([]) #сторюємо віконний додаток

from window import main_line

win = QWidget() # створємо вікно
win.resize(600, 300)
win.setWindowTitle("Memori card")
win.setLayout(main_line)

# в кінці
win.show() #показує вікно
app.exec_() # запускаємо додаток