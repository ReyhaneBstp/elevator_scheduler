import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton , QWidget
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
import elevator


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()


        self.elev1 = []
        self.elev2 = []
        self.elev3 = []  
        self.create_elevators()
        self.setWindowTitle("elevator")
        self.setFixedSize(QSize(800, 600))
        self.setStyleSheet('background-color:#424242 ')

  


    def create_elevators(self):


        for i in range(15):
            font = self.font()
            font.setPointSize(16)
            self.elev1.append(QPushButton(self))
            self.elev1[i].setFont(font)
            self.elev1[i].setGeometry(270, 500 - 30 * i,60,30)
            self.elev1[i].setText(str(i+1))
            self.elev1[i].setStyleSheet("background-color : #bcbcbc  ")

        for i in range(15):
            font = self.font()
            font.setPointSize(16)
            self.elev2.append(QPushButton(self))
            self.elev2[i].setFont(font)
            self.elev2[i].setGeometry(360, 500 - 30 * i,60,30)
            self.elev2[i].setText( str(i+1))
            self.elev2[i].setStyleSheet("background-color : #bcbcbc  ")
           

        for i in range(15):
            font = self.font()
            font.setPointSize(16)
            self.elev3.append(QPushButton(self))
            self.elev3[i].setFont(font)
            self.elev3[i].setGeometry(450, 500 - 30 * i,60,30)
            self.elev3[i].setText(str(i+1))
            self.elev3[i].setStyleSheet("background-color : #bcbcbc  ")

        



    def moveElevator(self,elevator1, elevator2, elevator3):
        for i in range(15):
            self.elev1[i].setStyleSheet("background-color : #bcbcbc ")
            self.elev2[i].setStyleSheet("background-color : #bcbcbc ")
            self.elev3[i].setStyleSheet("background-color : #bcbcbc ")

        self.elev1[elevator1.current_floor].setStyleSheet("background-color : #02c712")
        self.elev2[elevator2.current_floor].setStyleSheet("background-color : #02c712")
        self.elev3[elevator3.current_floor].setStyleSheet("background-color : #02c712")
            

elevator1 = elevator.Elevator(1)
elevator2 = elevator.Elevator(2)
elevator3 = elevator.Elevator(3)
elevator1.current_floor=5
elevator1.is_stop=False
elevator2.current_floor=10
elevator2.is_stop=True
elevator3.current_floor=5
elevator3.is_stop=False
app = QApplication(sys.argv)
window = MainWindow()

window.moveElevator(elevator1,elevator2,elevator3)

window.show()
app.exec()