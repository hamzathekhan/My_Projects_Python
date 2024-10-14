from random import choice, randint

from PyQt5.QtCore import Qt , QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton, QComboBox, QHBoxLayout
from PyQt5.QtGui import QLinearGradient, QBrush, QRadialGradient, QFont, QFontDatabase


class Daily_Quote_Generator(QWidget):
    def __init__(self):
        super().__init__()
        # App Setting
        self.setWindowTitle("Daily Quote Generator")
        self.resize(300,200)

        # Gradient Setting
        gradient = QRadialGradient(QPoint(self.width() // 2, self.height() // 2), self.width() // 2)
        gradient.setColorAt(0.5, Qt.blue)
        gradient.setColorAt(1.0, Qt.darkBlue)

        # Objects Part
        self.title = QLabel("Daily Quote Generator")
        self.title.setFont(QFont("Arial",16))
        self.Author_names = QComboBox()
        self.Author_names.addItem("Albert Einstein")
        self.Author_names.addItem("Nelson Mandela")
        self.Author_names.addItem("Quaid-e-Azam")
        self.quote = QLabel()
        self.button = QPushButton("Get Today's Quote")

        # Layouts
        master_layout = QVBoxLayout()
        self.r1 = QHBoxLayout()
        self.r2 = QHBoxLayout()
        self.r3 = QHBoxLayout()
        self.r4 = QHBoxLayout()

        #
        self.r1.addWidget(self.title , alignment=Qt.AlignCenter)
        self.r2.addWidget(self.Author_names)
        self.r3.addWidget(self.quote,alignment=Qt.AlignCenter)
        self.r4.addWidget(self.button)


        # Master Layout Setting
        master_layout.addLayout(self.r1)
        master_layout.addLayout(self.r2)
        master_layout.addLayout(self.r3)
        master_layout.addLayout(self.r4)

        self.setLayout(master_layout)

        # Events
        self.quoteDictionary = {
            "Albert Einstein" : ["Life is like riding a bicycle.\nTo keep your balance, you must keep moving.",
                                 "Imagination is more important than knowledge.\nFor knowledge is limited,\nwhereas imagination embraces the entire world.",
                                 "Try not to become a man of success,\nbut rather try to become a man of value."],
            "Nelson Mandela" : ["Education is the most powerful weapon\nwhich you can use to change the world.",
                                "No one is born hating another person.\nThis hatred is taught,\nand it can be unlearned.",
                                "I learned that courage was not the absence of fear,\nbut the triumph over it.\nThe brave man is not he who does not feel afraid,\nbut he who conquers that fear."],
            "Quaid-e-Azam" : ["Remember, democracy is a government of the people,\nfor the people, and by the people.",
                              "Unity is strength and strength is necessary\nfor the survival of a nation.",
                              "I am a Muslim, but I am also a Pakistani.\nAnd I am proud of both."],
        }


        self.button.clicked.connect(self.quoteGeneratorFunction)


        # Set the Gradient background Brush
        palette = self.palette()
        palette.setBrush(self.backgroundRole(), QBrush(gradient))
        self.setPalette(palette)


    def quoteGeneratorFunction(self):
        self.quoteNo = randint(0, 2)
        self.name = self.Author_names.currentText()
        todayQuote = (self.quoteDictionary.get(self.name))[self.quoteNo]
        self.quote.setText(todayQuote)


# Run the App
if __name__ in "__main__":
    app = QApplication([])
    main_window = Daily_Quote_Generator()
    main_window.show()
    app.exec_()