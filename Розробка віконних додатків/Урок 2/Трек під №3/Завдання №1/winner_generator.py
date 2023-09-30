#підключення бібліотек
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

import sys
#створення елементів інтерфейсу
app = QApplication(sys.argv)

line = QVBoxLayout()
main_window = QWidget()
main_window.show()
main_window.setWindowTitle("Визначник переможця")
main_window.resize(500, 300)


main_window.setLayout(line)

#прив'язка елементів до вертикальної лінії
text = QLabel("Натисни щоб дізнатися переможця")
number = QLabel("?")
button = QPushButton("Згенерувати")
vLayout.addWidget(text, aligment=Qt.AlignCenter)

#обробка подій

#запуск додатку
app.exec_()