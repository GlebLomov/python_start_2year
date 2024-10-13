from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox,QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox,\
                            QApplication
from PyQt5.QtCore import Qt
 
# Вікно додатку
window = QWidget()

btn_menu = QPushButton("Меню")
btn_rest = QPushButton("Відпочити")
btn_next= QPushButton("Відповісти")


rb_ans1 = QRadioButton("1")
rb_ans2 = QRadioButton("2")
rb_ans3 = QRadioButton("3")
rb_ans4 = QRadioButton("4")


RadioGroup = QButtonGroup()
RadioGroup.addButton(rb_ans1)
RadioGroup.addButton(rb_ans2)
RadioGroup.addButton(rb_ans3)
RadioGroup.addButton(rb_ans4)


lb_question = QLabel("Запитаня")
lb_rest = QLabel("хвилин")
lb_result = QLabel("Правильно")
lb_right_answer = QLabel("відповідь")

sp_rest = QSpinBox()

qb_question = QGroupBox("варіанти відповідей")

rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()


rb_h1 = QHBoxLayout()

rb_v1.addWidget(rb_ans1)
rb_v1.addWidget(rb_ans2)



rb_v2.addWidget(rb_ans3)
rb_v2.addWidget(rb_ans4)


rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)

qb_question.setLayout(rb_h1)

qb_answer = QGroupBox()

v1 = QVBoxLayout()

v1.addWidget(lb_result)
v1.addWidget(lb_right_answer)

qb_answer.setLayout(v1)


h1_main = QHBoxLayout()
h2_main = QHBoxLayout()
h3_main = QHBoxLayout()
h4_main = QHBoxLayout()
V1_main = QHBoxLayout()

h1_main.addWidget(btn_menu)

h1_main.addStretch(1)

h1_main.addWidget(btn_rest)

h1_main.addWidget(sp_rest)

h1_main.addWidget(lb_rest)


h2_main.addWidget(lb_question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

h3_main.addWidget(qb_answer)

h3_main.addWidget(qb_question)


qb_answer.hide()

h4_main.addStretch(1)

h4_main.addWidget(btn_next,stretch=2)

h4_main.addStretch(1)

V1_main.addLayout(h1_main,stretch=1)
V1_main.addLayout(h2_main,stretch=2)
V1_main.addLayout(h3_main,stretch=8)

V1_main.addLayout(h4_main)

V1_main.setSpacing(5)

window.setLayout(V1_main)

window.resize(550,450)

window.setWindowTitle("Memory Card")