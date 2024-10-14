from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox
from PyQt5.QtGui import QFont
from random import choice
import string
from sys import exit

class PaaswordGen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")

        # Objects
        self.password_lenght = QLabel("Password Length:      ")
        self.password_lenght.setStyleSheet("QLabel { font-family: Impact ; color : #333333 ; }")
        self.characters_included = QLabel("Include Characters:")
        self.characters_included.setStyleSheet("QLabel { font-family: Impact ; color : #333333 ; }")
        self.symbols_included = QLabel("Include Symbols:")
        self.symbols_included.setStyleSheet("QLabel { font-family: Impact ; color : #333333 ; }")
        self.number_included = QLabel("Include Numbers:")
        self.number_included.setStyleSheet("QLabel { font-family: Impact ; color : #333333 ; }")
        self.password_text = QLabel("Generated Password:")
        self.password_text.setStyleSheet("QLabel { font-family: Impact ; color : #333333 ; }")

        self.input_of_password_lenght = QLineEdit()
        self.checkbox_of_characters_included = QCheckBox()
        self.checkbox_of_symbols_included = QCheckBox()
        self.checkbox_of_number_included = QCheckBox()
        self.input_of_password_here = QLineEdit()
        self.input_of_password_here.setReadOnly(True)
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.setStyleSheet("QPushButton { background-color : #f39c12 ;}")
        self.exit_button = QPushButton("Exit App")


        # Layout
        self.master_layout = QVBoxLayout()

        r1 = QHBoxLayout()
        r2 = QHBoxLayout()
        r3 = QHBoxLayout()
        r4 = QHBoxLayout()
        r5 = QHBoxLayout()
        r6 = QHBoxLayout()

        r1.addWidget(self.password_lenght)
        r1.addWidget(self.input_of_password_lenght)

        r2.addWidget(self.characters_included)
        r2.addWidget(self.checkbox_of_characters_included)

        r3.addWidget(self.symbols_included)
        r3.addWidget(self.checkbox_of_symbols_included)

        r4.addWidget(self.number_included)
        r4.addWidget(self.checkbox_of_number_included)

        r5.addWidget(self.password_text)
        r5.addWidget(self.input_of_password_here)

        r6.addWidget(self.generate_button)


        self.master_layout.addLayout(r1)
        self.master_layout.addLayout(r2)
        self.master_layout.addLayout(r3)
        self.master_layout.addLayout(r4)
        self.master_layout.addLayout(r5)
        self.master_layout.addLayout(r6)

        self.setLayout(self.master_layout)
        self.generate_button.clicked.connect(self.password_generator_function)





    # Events
    def password_generator_function(self):
        password_lenght_value = int(self.input_of_password_lenght.text())

        if password_lenght_value < 8:
            self.input_of_password_here.setText("Too Short Password")

        Characters = ""

        if self.checkbox_of_characters_included.isChecked():
            Characters += string.ascii_letters
        if self.checkbox_of_symbols_included.isChecked():
            Characters += string.punctuation

        if self.checkbox_of_number_included.isChecked():
            Characters += string.digits
        if not Characters:
            self.input_of_password_here.setText("Not Valid Options")
            return
        password = "".join(choice(Characters) for _ in range(password_lenght_value))

        self.input_of_password_here.setText(password)





# Run/Show App
if __name__ in "__main__":
    app = QApplication([])
    main_window = PaaswordGen()
    main_window.setStyleSheet("QWidget { background-color : #bdc3c7  ;}")
    main_window.show()
    app.exec_()
