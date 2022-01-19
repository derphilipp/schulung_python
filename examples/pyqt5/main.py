#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget


class HelloWorld(QWidget):
    # Kontruktor
    def __init__(self):
        super().__init__()
        self.init_ui()

    # Initialisierungsfunktion
    def init_ui(self):
        self.my_button = QPushButton("Hello World", self)
        self.my_button.clicked.connect(self.slot_hello_world)
        self.quit_button = QPushButton("Quit", self)
        self.quit_button.clicked.connect(QApplication.instance().quit)
        self.quit_button.resize(self.quit_button.sizeHint())
        self.quit_button.move(50, 50)

        self.setGeometry(200, 200, 200, 200)
        self.setWindowIcon(QIcon('web.png'))
        self.setWindowTitle('Icon')
        self.show()

    # Beliebige Funktion
    def slot_hello_world(self):
        print("Hello World")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = HelloWorld()
    sys.exit(app.exec_())
