from PyQt5.QtWidgets import QLabel, QApplication, QDialog, QGridLayout, QHBoxLayout, QPushButton, QFormLayout, \
    QWidget, \
    QLineEdit
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class calculator_frame(QDialog):
    def __init__(self):
        super().__init__()
        self.shower = QLineEdit()
        self.label = QLabel()
        self.init()
        self.tmp_string_num = ""
        self.tmp_num = 0
        self.sum_num = ""
        self.num = 0

    def init(self):
        self.setWindowTitle("个人计算器")
        self.setWindowIcon(QIcon('calculator.ico'))
        self.label.setStyleSheet('font-size:20px;color:rgb(180,180,180,255);')
        self.shower.setStyleSheet('font-size:20px;color:rgb(180,180,180,255);')
        self.shower.setEnabled(False)
        hbox = QHBoxLayout()
        form_widget = QWidget()
        grid_widget = QWidget()
        form_layout = QFormLayout()
        form_layout.addRow("memory:", self.shower)
        form_layout.addRow("result=", self.label)
        form_widget.setLayout(form_layout)
        # self.setFixedSize(300,200)

        grid_layout = QGridLayout()
        one = QPushButton("1")
        two = QPushButton("2")
        three = QPushButton("3")
        four = QPushButton("4")
        five = QPushButton("5")
        six = QPushButton("6")
        seven = QPushButton("7")
        eight = QPushButton("8")
        nine = QPushButton("9")
        zero = QPushButton("0")
        point = QPushButton(".")
        equal = QPushButton("=")
        add = QPushButton("+")
        sub = QPushButton("-")
        mult = QPushButton("*")
        div = QPushButton("/")

        one.clicked.connect(self.clicker)
        two.clicked.connect(self.clicker)
        three.clicked.connect(self.clicker)
        four.clicked.connect(self.clicker)
        five.clicked.connect(self.clicker)
        six.clicked.connect(self.clicker)
        seven.clicked.connect(self.clicker)
        eight.clicked.connect(self.clicker)
        nine.clicked.connect(self.clicker)
        zero.clicked.connect(self.clicker)
        add.clicked.connect(self.clicker)
        sub.clicked.connect(self.clicker)
        mult.clicked.connect(self.clicker)
        div.clicked.connect(self.clicker)
        equal.clicked.connect(self.clicker)
        point.clicked.connect(self.clicker)
        one.setStyleSheet('font-size:32px;color:rgb(0,0,0,255);')
        two.setStyleSheet('font-size:32px;color:rgb(0,0,0,255);')
        three.setStyleSheet('font-size:32px;color:rgb(0,0,0,255);')
        four.setStyleSheet('font-size:32px;color:rgb(0,0,0,255);')
        five.setStyleSheet('font-size:32px;color:rgb(0,0,0,255);')
        six.setStyleSheet('font-size:32px;color:rgb(0,0,0,255);')
        seven.setStyleSheet('font-size:32px;color:rgb(0,0,0,255);')
        eight.setStyleSheet('font-size:32px;color:rgb(0,0,0,255);')
        nine.setStyleSheet('font-size:32px;color:rgb(0,0,0,255);')
        zero.setStyleSheet('font-size:32px;color:rgb(0,0,0,255);')
        point.setStyleSheet('font-size:32px;color:rgb(0,0,0,255);')
        equal.setStyleSheet('font-size:32px;color:rgb(0,0,0,255);')
        add.setStyleSheet('font-size:28px;color:rgb(0,0,0,255);')
        sub.setStyleSheet('font-size:28px;color:rgb(0,0,0,255);')
        mult.setStyleSheet('font-size:28px;color:rgb(0,0,0,255);')
        div.setStyleSheet('font-size:28px;color:rgb(0,0,0,255);')

        grid_layout.addWidget(add, 2, 4)
        grid_layout.addWidget(div, 1, 4)
        grid_layout.addWidget(mult, 0, 4)
        grid_layout.addWidget(sub, 3, 4)
        grid_layout.addWidget(zero, 3, 2)
        grid_layout.addWidget(point, 3, 1)
        grid_layout.addWidget(equal, 3, 3)
        grid_layout.addWidget(one, 2, 1)
        grid_layout.addWidget(two, 2, 2)
        grid_layout.addWidget(three, 2, 3)
        grid_layout.addWidget(four, 1, 1)
        grid_layout.addWidget(five, 1, 2)
        grid_layout.addWidget(six, 1, 3)
        grid_layout.addWidget(seven, 0, 1)
        grid_layout.addWidget(eight, 0, 2)
        grid_layout.addWidget(nine, 0, 3)
        grid_widget.setLayout(grid_layout)
        hbox.addWidget(form_widget, 0, Qt.AlignLeft)
        hbox.addWidget(grid_widget, 0, Qt.AlignRight)
        self.setLayout(hbox)

    def clicker(self):
        num_or_opt = self.sender().text()
        if num_or_opt.isdigit():
            self.tmp_string_num += str(num_or_opt)
            self.tmp_num = int(self.tmp_string_num)
            self.shower.setText(self.tmp_string_num)
            self.sum_num += self.tmp_string_num
            print(self.sum_num)
            self.label.setText(self.sum_num)
            self.tmp_string_num=""
            self.tmp_num = 0
        else:
            if not num_or_opt == "=":
                self.tmp_string_num += num_or_opt
                self.sum_num += num_or_opt
                self.shower.setText(self.tmp_string_num)
                self.tmp_string_num = ""
                self.tmp_num = 0
            else:
                self.label.setText(str(eval(self.sum_num)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainFrame = calculator_frame()
    mainFrame.show()
    sys.exit(app.exec_())
