import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton , QWidget
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import QtCore
from PyQt6.QtCore import Qt


# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()


        self.elev1 = []
        self.elev2 = []
        self.elev3 = []
        self.create_elevators()


        self.setWindowTitle("Alavator")
        self.setFixedSize(QSize(800, 600))
        self.setStyleSheet('background-color:#424242 ')
        #self.create_widgets()

    def create_widgets(self):
        btn=QPushButton("ok",self)


    def create_elevators(self):


        for i in range(15):
            font = self.font()
            font.setPointSize(16)
            self.elev1.append(QPushButton(self))
            self.elev1[i].setFont(font)
            self.elev1[i].setGeometry(270, 500 - 30 * i,60,30)
            self.elev1[i].setText(str(i+1))
            if(i%2==0):
                self.elev1[i].setStyleSheet("background-color : #7f7f7f ")
            else:
                self.elev1[i].setStyleSheet("background-color : #bcbcbc  ")

        for i in range(15):
            font = self.font()
            font.setPointSize(16)
            self.elev2.append(QPushButton(self))
            self.elev2[i].setFont(font)
            self.elev2[i].setGeometry(360, 500 - 30 * i,60,30)
            self.elev2[i].setText( str(i+1))
            if(i%2==0):
                self.elev2[i].setStyleSheet("background-color : #bcbcbc  ")
            else:
                self.elev2[i].setStyleSheet("background-color : #7f7f7f ")

        for i in range(15):
            font = self.font()
            font.setPointSize(16)
            self.elev3.append(QPushButton(self))
            self.elev3[i].setFont(font)
            self.elev3[i].setGeometry(450, 500 - 30 * i,60,30)
            self.elev3[i].setText(str(i+1))
            if(i%2==0):
                self.elev3[i].setStyleSheet("background-color : #7f7f7f ")
            else:
                self.elev3[i].setStyleSheet("background-color : #bcbcbc  ")
            


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()