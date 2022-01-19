#!/usr/bin/env python

import sys
from PyQt4 import Qt


class HelloApplication(Qt.QApplication):

    def __init__(self, args):
        # ...
        Qt.QApplication.__init__(self, args)
        # ...
        self.addWidgets()
        # ...
        self.exec_()

    def addWidgets(self):
        # ...
        self.mein_button = Qt.QPushButton("Sag 'Guten Tag!'", None)
        # ...
        self.connect(self.mein_button, Qt.SIGNAL("clicked()"), self.slotSagGutenTag)
        self.mein_button.show()

    def slotSagGutenTag(self):
        # ...
        print ("Guten Tag!")

# Wenn das Programm gestartet wird, erzeuge ein HelloApplication Instanz
if __name__ == "__main__":
    app = HelloApplication(sys.argv)
