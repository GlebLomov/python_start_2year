from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox,QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox,\
                            QApplication
from PyQt5.QtCore import Qt
 
# Вікно додатку
window = QWidget()
 
#  Всі кнопки
btn_menu = QPushButton('Меню')
btn_rest = QPushButton('Відпочити')
btn_next = QPushButton('Відповісти')
 
# Варіанти відповідей
rb_ans1 = QRadioButton("1")
rb_ans2 = QRadioButton("2")
rb_ans3 = QRadioButton("3")
rb_ans4 = QRadioButton("4")
 
# Групуємо варіанти відповідей
RadioGroup = QButtonGroup()
RadioGroup.addButton(rb_ans1)
RadioGroup.addButton(rb_ans2)
RadioGroup.addButton(rb_ans3)
RadioGroup.addButton(rb_ans4)
 
# Тексти
lb_question = QLabel('Запитання')
lb_rest = QLabel('хвилин')
lb_result = QLabel('Правильно')
lb_right_answer = QLabel('відповідь')
 
# віджет-лічильник - Скільки часу відпочити
sp_rest = QSpinBox()
 
# Група радіо кнопок = щоб згрупувати всі кнопки в один об'єкт
gb_question = QGroupBox('Варіанти відповідей')
 
# Задаємо 2 вертикальні лінії
rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()
 
# Задаємо горизонтальну лінію
rb_h1 = QHBoxLayout()
 
# Поміщаємо до першої вертикальні лінії ДВІ радіо-кнопки
rb_v1.addWidget(rb_ans1)
rb_v1.addWidget(rb_ans2)
 
# Поміщаємо до ДРУГОЇ вертикальні лінії ДВІ  радіо-кнопки
rb_v2.addWidget(rb_ans3)
rb_v2.addWidget(rb_ans4)
 
# Поміщаємо 2 вертикальні лінії до горизонтальної лінії
rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)
 
# До Групи (QGroupBox) радіо-кнопок додаємо горизонтальну лінію
#  в якій знаходятся дві вертикальні лінії
#  в в кожній з яких знаходятся по 2 радіо кнопки
gb_question.setLayout(rb_h1)
 
# Нова група для відображення правильної відповідді
gb_answer = QGroupBox()
# Створюємо вертикальну лінію
v1 = QVBoxLayout()
# Додаємо тексти "Правильно" і "відповідь"
v1.addWidget(lb_result)
v1.addWidget(lb_right_answer)
# Додаємо до групи вертикальну лінію в якій знаходиться 2 тексти
gb_answer.setLayout(v1)
 
# Створюємо основні лінії для всього застосунку
#  Чотири горизонтальні лінії (рядки)
#  та одна вертикальна лінія (стовпчик)
h1_main = QHBoxLayout()
h2_main = QHBoxLayout()
h3_main = QHBoxLayout()
h4_main = QHBoxLayout()
v1_main = QVBoxLayout()
 
# До першох горизонтальної лінії додаємо кнопку "Меню"
h1_main.addWidget(btn_menu)
# addStretch додає еластичний простір після кнопки btn_menu, 
# що допомагає вирівняти її зліва, а простір справа залишиться вільним
h1_main.addStretch(1)
# кнопка "Відпочити""
h1_main.addWidget(btn_rest)
# віджет-лічильник
h1_main.addWidget(sp_rest)
# текст "хвилин"
h1_main.addWidget(lb_rest)
 
# До другої горизонтальної лінії додаємо текст "Запитання"
#  та вирівнюємо його по центру горизонталі та вертикалі одночасно
h2_main.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
 
# До третьої горизонтальної лінії додаємо ГРУПУ
#  для відображення правильної відповідді
h3_main.addWidget(gb_answer)
# Група радіо-кнопок"Варіанти відповідей"
h3_main.addWidget(gb_question)
# приховуємо ГРУПУ
#  для відображення правильної відповідді
# оскільки спочатку треба показати лише питання, ЛИШЕ після відповідді
# показати правильний варіант
gb_answer.hide()
 
# До четвертої горизонтальної лінії додаємо розтягування
h4_main.addStretch(1)
# Додаємо кнопку "Відповісти"
# Параметр stretch тут означає, що ця кнопка отримає пріоритет розтягування в 2 рази
#  більший, ніж інші елементи з меншими або однаковими значеннями розтягування.
h4_main.addWidget(btn_next, stretch=2)
# додається еластичний простір з коефіцієнтом 1, але вже праворуч від кнопки.
# Це допомагає розподілити вільний простір рівномірно з обох сторін кнопки.
h4_main.addStretch(1)
 
 
# вертикальна лінія (стовпчик). Додаємо горизонтальні лінії
# чим більше stretch тим більше місця по вертикалі займає елемент
 
# Додаємо перший горизонтальний layout h1_main з пріоритетом розтягування 1
v1_main.addLayout(h1_main, stretch=1)
# Додаємо другий горизонтальний layout h2_main з пріоритетом розтягування 2
v1_main.addLayout(h2_main, stretch=2)
# Додаємо третій горизонтальний layout h3_main з пріоритетом розтягування 8
v1_main.addLayout(h3_main, stretch=8)
# різні пріоритети розтягування допомагають грамотно організувати інтерфейс, 
# щоб важливіші частини отримували більше простору, а допоміжні займали мінімум місця.
 
 # Додаємо четвертий горизонтальний layout h4_main без пріоритету розтягування
v1_main.addLayout(h4_main)
# Встановлюємо відстань між елементами layout на 5 пікселів
v1_main.setSpacing(5)
 
# Встановлюємо головний вертикальний layout v1_main як основний для вікна
window.setLayout(v1_main)
# Задаємо розміри вікна: ширина 550 пікселів, висота 450 пікселів
window.resize(550, 450)
 
window.setWindowTitle('Memory Card')
