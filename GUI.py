import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton , QWidget
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
import elevator



class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()


        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        
        #self.setStyleSheet("background-color : gray ")
        #self.setStyleSheet("background-image: url(elev.jpg);background-repeat: no-repeat; background-position: center ; width:600 ; height:800")
        self.elev1 = []
        self.elev2 = []
        self.elev3 = []  
        self.textbox = [] 
        self.okbtn=[] 
        self.create_elevators()
        self.setWindowTitle("elevator")
        self.setFixedSize(QSize(800, 600))

        
        

 


    def create_elevators(self):


        for i in range(15):
            font = self.font()
            font.setPointSize(16)
            self.elev1.append(QPushButton(self))
            self.elev1[i].setFont(font)
            self.elev1[i].setGeometry(270, 480 - 30 * i,60,30)
            self.elev1[i].setText(str(i+1))
            self.elev1[i].setStyleSheet("color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray")

        for i in range(15):
            font = self.font()
            font.setPointSize(16)
            self.elev2.append(QPushButton(self))
            self.elev2[i].setFont(font)
            self.elev2[i].setGeometry(360, 480 - 30 * i,60,30)
            self.elev2[i].setText( str(i+1))
            self.elev2[i].setStyleSheet("color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray")
           

        for i in range(15):
            font = self.font()
            font.setPointSize(16)
            self.elev3.append(QPushButton(self))
            self.elev3[i].setFont(font)
            self.elev3[i].setGeometry(450, 480 - 30 * i,60,30)
            self.elev3[i].setText(str(i+1))
            self.elev3[i].setStyleSheet("color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray ")


        for i in range(3):
            self.textbox.append(QLineEdit(self))
            self.textbox[i].setGeometry(230+110*i, 520 ,100,40)
            self.textbox[i].setStyleSheet("border-radius : 20;border : 2px solid black;background-color : lightgreen")
            self.okbtn.append(QPushButton("OK", self))
            self.okbtn[i].setGeometry(295+110*i, 525, 32, 32)
            self.okbtn[i].setStyleSheet("color: lightgray;border-radius : 16;border : 2px solid black;background-color : darkgreen")
           

        
        
 



        



    def moveElevator(self,elevator1, elevator2, elevator3):
        for i in range(15):
            self.elev1[i].setStyleSheet("color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray")
            self.elev2[i].setStyleSheet("color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray")
            self.elev3[i].setStyleSheet("color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray")

        self.elev1[elevator1.current_floor].setStyleSheet("color: lightgray;background-color : green;border-radius : 50;border : 2px solid black")
        self.elev2[elevator2.current_floor].setStyleSheet("color: lightgray;background-color : green;border-radius : 50;border : 2px solid black")
        self.elev3[elevator3.current_floor].setStyleSheet("color: lightgray;background-color : green;border-radius : 50;border : 2px solid black")
            

elevator1 = elevator.Elevator(1)
elevator2 = elevator.Elevator(2)
elevator3 = elevator.Elevator(3)
elevator1.current_floor=5
elevator1.is_stop=False
elevator2.current_floor=10
elevator2.is_stop=True
elevator3.current_floor=5
elevator3.is_stop=False

stylesheet = """
    MainWindow {
        border-image: url("elev.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
        
    }
"""

app = QApplication(sys.argv)
app.setStyleSheet(stylesheet)



window = MainWindow()

window.moveElevator(elevator1,elevator2,elevator3)

window.show()
app.exec()