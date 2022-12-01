# подключаем модуль с направляющими линиями
from PyQt5.Qt import Qt
# подключаем необходимые виджеты
from PyQt5.QtWidgets import (
    QApplication, QWidget, QRadioButton,
    QVBoxLayout, QPushButton, QLabel,
    QButtonGroup
)
# создаём объект приложения
app = QApplication([])
# создаём объект главного окна
window = QWidget()
# создаём название главного окна
window.setWindowTitle('app')
# задаём точку появления окна на экране компьютера
window.move(900, 70)
# задаём размер окна
window.resize(400, 200)
# даём команду окну показаться
window.show()

# создаём объекты радиокнопок
radio_button1 = QRadioButton('1')
radio_button2 = QRadioButton('2')
radio_button3 = QRadioButton('3')
# устанавливаем, какая радиокнопка будет выбрана при запуске программы
radio_button1.setChecked(True)
# создаём направляющую вертикальную линию
line_v = QVBoxLayout()

# размещаем радиокнопки на вертикальной направляющей
line_v.addWidget(radio_button1)
line_v.addWidget(radio_button2)
line_v.addWidget(radio_button3)
# создаём объект кнопки и задаём надпись на ней
button = QPushButton('Проверить')
# помещаем кнопку на направляющую линию по центру
line_v.addWidget(button, alignment=Qt.AlignCenter)
# создаём поле, где далее будет отображаться текст про выбранную кнопку
title = QLabel()
line_v.addWidget(title, alignment=Qt.AlignCenter)
# добавляем получившуюся линию на окно приложения
window.setLayout(line_v)
# создаём группу радиокнопок и добавляем туда созданные нами ранее объекты радиокнопок
button_group = QButtonGroup()
button_group.addButton(radio_button1, id=1)
button_group.addButton(radio_button2, id=2)
button_group.addButton(radio_button3, id=3)
# функция, которая изменяет информацию (текст) о новой кнопке
def radio_button_check():
    title.setText('Выбрана кнопка ' + str(button_group.checkedId()))
# связываем нажатие на кнопку и вызов функции
button.clicked.connect(radio_button_check)
# Оставляет приложение открытым, пока не будет нажата кнопка выхода
app.exec_()



