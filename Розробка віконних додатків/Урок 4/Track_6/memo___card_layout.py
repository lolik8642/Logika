''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo___app import app 

# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно 
btn_menu = QPushButton("Меню")

# кнопка прибирає вікно і повертає його після закінчення таймера
btn_sleep = QPushButton("Відпочити")
# введення кількості хвилин
box_minutes = QSpinBox()
box_minutes.setValue(30)
# кнопка відповіді "Ок" / "Наступний"
btn_OK = QPushButton("ВІдповісти")

# текст питання
lb_question = QLabel('Яблуко')
rbtn_1 = QRadioButton('')
rbth_2 = QRadioButton('')
rbth_3 = QRadioButton('')
rbth_4 = QRadioButton('')

# Опиши групу перемикачів
radioGroupBox = QGroupBox("Варіанти відповідей")
radioGroup = QButtonGroup()

radioGroup.addButton(rbtn_1)
radioGroup.addButton(rbth_2)
radioGroup.addButton(rbth_3)
radioGroup.addButton(rbth_4)

# Опиши панень з результатами

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
    ''' показати панель відповідей '''
    pass

def show_question():
    ''' показати панель запитань '''
    pass
