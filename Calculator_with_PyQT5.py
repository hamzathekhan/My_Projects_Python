from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, \
    QComboBox
from PyQt5.QtGui import QFont
from math import sqrt


# Creating Class
class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        # App Setting
        self.setWindowTitle("Calc App Practice")
        self.resize(300,200)

        # Objetcs
        self.text_box = QLineEdit()
        self.text_box.setReadOnly(True)
        self.text_box.setFont(QFont("Arial",20))
        self.text_box.setStyleSheet("QLineEdit { background-color : #b5b5b5 ;}")
        self.combo = QComboBox()
        self.combo.addItem("History")
        self.grid = QGridLayout()
        buttons = [("1/x",0,0),("x*x",0,1),("SQRT",0,2),("%",0,3),
                   ("7",1,0),("8",1,1),("9",1,2),("-",1,3),
                   ("4",2,0),("5",2,1),("6",2,2),("+",2,3),
                   ("1",3,0),("2",3,1),("3",3,2),("*",3,3),
                   ("0",4,0),(".",4,1),("=",4,2),("/",4,3)
                   ]
        for text , row , col in buttons:
            button = QPushButton(text)
            if button.text() == "=":
                button.setStyleSheet("QPushButton { background-color : #587ded ;}")
            elif button.text() in ["+","-","*","/","1/x","x*x","SQRT","%"]:
                button.setStyleSheet("QPushButton { background-color : #f58f22 ;}")
            else:
                button.setStyleSheet("QPushButton { background-color : #cccccc ;}")
            button.clicked.connect(self.CalculationFunction)
            self.grid.addWidget(button,row,col)
        self.del_ = QPushButton("Del")
        self.del_.setStyleSheet("QPushButton { background-color : #ff3636 ;}")
        self.clear = QPushButton("Clear")
        self.clear.setStyleSheet("QPushButton { background-color : #ff3636 ;}")


        # Layout
        master_layout = QVBoxLayout()
        self.r1 = QHBoxLayout()
        self.r2 = QHBoxLayout()
        self.r3 = QHBoxLayout()

        #
        self.r1.addWidget(self.text_box,alignment=Qt.AlignLeft)
        self.r1.addWidget(self.combo)
        self.r2.addLayout(self.grid)
        self.r3.addWidget(self.clear)
        self.r3.addWidget(self.del_)

        #
        master_layout.addLayout(self.r1)
        master_layout.addLayout(self.r2)
        master_layout.addLayout(self.r3)
        #
        self.setLayout(master_layout)

        # Events
        self.del_.clicked.connect(self.CalculationFunction)
        self.clear.clicked.connect(self.CalculationFunction)
        self.x = 0
    def CalculationFunction(self):
        button = app.sender()
        text = button.text()

        if text == "=":
            value = self.text_box.text()
            try:
                res = eval(value)
                self.text_box.setText(str(res))
                self.combo.addItem(f'{self.x}. Result: {value} = {res}')
                self.x += 1
            except Exception as e:
                self.text_box.setText(f'Error : {e}')
                self.combo.addItem(f'{self.x}. Result: {e}')
                self.x += 1

        elif text == "Del":
            value = self.text_box.text()
            res = value[:-1]
            self.text_box.setText(res)
        elif text == "Clear":
            self.text_box.setText("")
        elif text == "1/x":
            value = self.text_box.text()
            res = round(1/int(value),4)
            self.text_box.setText(str(res))
            self.combo.addItem(f'{self.x}. Result 1/{value} = {res}')
            self.x += 1
        elif text == "x*x":
            value = self.text_box.text()
            res = float(value)*float(value)
            self.text_box.setText(str(res))
            self.combo.addItem(f'{self.x}. Result {value}*{value} = {res}')
            self.x += 1
        elif text == "SQRT":
            value = self.text_box.text()
            res = sqrt(float(value))
            self.text_box.setText(str(res))
            self.combo.addItem(f'{self.x}. Result sqrt({value}) = {res}')
            self.x += 1
        else:
            value = self.text_box.text()
            self.text_box.setText(value+text)

# Show App
if __name__ == "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget { background-color : #737170 ;}")
    main_window.show()
    app.exec_()