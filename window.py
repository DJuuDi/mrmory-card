from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QRadioButton, QButtonGroup, QGroupBox, QWidget, QSpinBox, QHBoxLayout, QPushButton, QLabel, QVBoxLayout

menu_btn = QPushButton("Меню")
rest_btn = QPushButton("Відпочити")

time_spin = QSpinBox()
time_spin.setValue(3)
time_lb = QLabel("хвилини")

row1 = QHBoxLayout()
row1.addWidget(menu_btn)
row1.addWidget(rest_btn)
row1.addWidget(time_spin)
row1.addWidget(time_lb)

question_lb = QLabel("Питання")

btn1 = QRadioButton("варіант1")
btn2 = QRadioButton("варіант2")
btn3 = QRadioButton("варіант3")
btn4 = QRadioButton("варіант4")

row2 = QHBoxLayout()
radio_group = QButtonGroup
radio_group.addButton(btn1)
radio_group.addButton(btn2)
radio_group.addButton(btn3)
radio_group.addButton(btn4)



main_line = QVBoxLayout()
main_line.addLayout(row1)