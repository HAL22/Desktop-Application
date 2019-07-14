#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a bit
more complicated window layout using
the QGridLayout manager.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')



        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        la = QHBoxLayout(self)
        la.addWidget(titleEdit)



        grid = QGridLayout()
        grid.setSpacing(10)


        extrawid = QWidget(self)
        extrawid.setGeometry(5, 5, 5, 5)
        extrawid.show()


        la.addLayout(grid)
       





        self.setLayout(la)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        extrawid.show()
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())