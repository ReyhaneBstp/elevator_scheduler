from functools import partial

from PyQt6.QtCore import QSize
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget

import elevator


class MainWindow(QMainWindow, QWidget):
    def __init__(self, elevator1, elevator2, elevator3):
        super().__init__()
        self.elevator1 = elevator1
        self.elevator2 = elevator2
        self.elevator3 = elevator3
        self.elev1 = []
        self.elev2 = []
        self.elev3 = []
        self.dir = []
        self.textbox = []
        self.okbtn = []
        self.saveInfo = []
        self.Btn1 = []
        self.Btn2 = []
        self.create_elevators()
        self.setWindowTitle("elevator")
        self.setFixedSize(QSize(800, 600))
        self.pause = False

    def create_elevators(self):
        
        for i in range(16):
            j = 1
            font = self.font()
            font.setPointSize(16)
            self.elev1.append(QPushButton(self))
            self.elev1[i].setFont(font)
            self.elev1[i].setGeometry(270, 520 - (30) * i, 60, 30)
            self.elev1[i].setText(str(i))
            self.elev1[i].setStyleSheet(
                "color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray"
            )
            self.elev1[i].clicked.connect(partial(self.setIntReq, i, j))

        for i in range(16):
            j = 2
            font = self.font()
            font.setPointSize(16)
            self.elev2.append(QPushButton(self))
            self.elev2[i].setFont(font)
            self.elev2[i].setGeometry(360, 520 - 30 * i, 60, 30)
            self.elev2[i].setText(str(i))
            self.elev2[i].setStyleSheet(
                "color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray"
            )
            self.elev2[i].clicked.connect(partial(self.setIntReq, i, j))

        for i in range(16):
            j = 3
            font = self.font()
            font.setPointSize(16)
            self.elev3.append(QPushButton(self))
            self.elev3[i].setFont(font)
            self.elev3[i].setGeometry(450, 520 - 30 * i, 60, 30)
            self.elev3[i].setText(str(i))
            self.elev3[i].setStyleSheet(
                "color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray "
            )
            self.elev3[i].clicked.connect(partial(self.setIntReq, i, j))
        self.rect=QLineEdit(self)
        self.rect.setGeometry(580, 270, 60, 100)
        self.rect.setFont(font)
        self.rect.setStyleSheet(
                "border : 2px solid black;background-color : darkgray;border-radius : 20"
            )
        for j in range(2):
            font = self.font()
            font.setPointSize(11)
            self.textbox.append(QLineEdit(self))
            if j == 0:
                self.textbox[j].setToolTip("enter current floor")
            if j == 1:
                self.textbox[j].setToolTip("enter destination floor")

            self.textbox[j].setGeometry(597, 280 + 26 * j, 26, 26)
            self.textbox[j].setFont(font)
            self.textbox[j].setStyleSheet(
                "border-radius : 15;border : 1px solid lightgray;background-color : darkgray"
            )
        self.okbtn.append(QPushButton("OK", self))
        self.okbtn[0].setGeometry(595, 335 , 32, 32)
        self.okbtn[0].setStyleSheet(
            "color: black;border-radius : 16;border : 2px solid lightgray;background-color :gray"
        )
        self.okbtn[0].clicked.connect(self.setExtReq)    
        self.textbox.append(QLineEdit(self))
        self.textbox[2].setGeometry(255, 27, 270, 40)
        self.textbox[2].setFont(font)
        self.textbox[2].setStyleSheet(
                "border : 2px solid darkgray;background-color : black"
            )

        self.textbox.append(QLineEdit(self))
        self.textbox[3].setGeometry(150, 270, 60, 100)
        self.textbox[3].setFont(font)
        self.textbox[3].setStyleSheet(
                "border : 2px solid black;background-color : darkgray;border-radius : 20"
            )
        
        self.Btn2.append(QPushButton("⏯", self))
        font.setPointSize(18)
        self.Btn2[0].setFont(font)
        self.Btn2[0].setGeometry(167, 305 , 32, 32)
        self.Btn2[0].setStyleSheet(
            "color: black;border-radius : 16;border : 2px solid lightgray;background-color :gray"
        )
        
        for i in range(3):
            font.setPointSize(21)
            self.dir.append(QPushButton("⇈", self))
            font.bold()
            self.dir[i].setFont(font)
            self.dir[i].setGeometry(280+90*i, 32, 32, 32)
            self.dir[i].setStyleSheet(
                "color: darkgreen;border-radius : 16;border : 2px solid black;background-color : balck")
        self.Btn2[0].clicked.connect(self.pause_elevator)
        #self.Btn2[0].clicked.connect(self.resume_elevator)
       

    def pause_elevator(self):
        self.pause = not self.pause

    #def resume_elevator(self):
        #self.pause = False

    def setExtReq(self):
        elv = elevator.Elevator.nearest_elevator(
            self.elevator1, self.elevator2, self.elevator3, int(self.textbox[0].text())
        )
        elv.add_external_req(int(self.textbox[0].text()), int(self.textbox[1].text()))

    def setIntReq(self, i, j):
        if j == 1:
            self.elevator1.add_internal_req(i)
        if j == 2:
            self.elevator2.add_internal_req(i)
        if j == 3:
            self.elevator3.add_internal_req(i)

    def update(self):
        
        for i in range(16):

         

            self.elev1[i].setStyleSheet(
                "color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray"
            )
            self.elev2[i].setStyleSheet(
                "color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray"
            )
            self.elev3[i].setStyleSheet(
                "color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray"
            )
            if i in self.elevator1.internal_req_list():
                self.elev1[i].setStyleSheet(
                    "color: black;background-color : darkgray ;border-radius : 50;border : 2px solid black"
                )

            if i in self.elevator2.internal_req_list():
                self.elev2[i].setStyleSheet(
                    "color: black;background-color : darkgray ;border-radius : 50;border : 2px solid black"
                )

            if i in self.elevator3.internal_req_list():
                self.elev3[i].setStyleSheet(
                    "color: black;background-color : darkgray ;border-radius : 50;border : 2px solid black"
                )
            for j in range(len(self.elevator1.external_req_list())):
                if self.elevator1.external_req_list()[j][0] == i:
                    self.elev1[i].setStyleSheet(
                        "color: black;background-color : darkgray ;border-radius : 50;border : 2px solid black"
                    )
            for j in range(len(self.elevator2.external_req_list())):
                if self.elevator2.external_req_list()[j][0] == i:
                    self.elev2[i].setStyleSheet(
                        "color: black;background-color : darkgray ;border-radius : 50;border : 2px solid black"
                    )
            for j in range(len(self.elevator3.external_req_list())):
                if self.elevator3.external_req_list()[j][0] == i:
                    self.elev3[i].setStyleSheet(
                        "color: black;background-color : darkgray ;border-radius : 50;border : 2px solid black"
                    )

        if self.elevator1.is_stop:
            self.elev1[self.elevator1.current_floor].setStyleSheet(
                "color: lightgray;background-color : green;border-radius : 50;border : 2px solid black"
            )
        else:
            self.elev1[self.elevator1.current_floor].setStyleSheet(
                "color: lightgray;background-color : darkorange;border-radius : 50;border : 2px solid gray"
            )

        if self.elevator2.is_stop:
            self.elev2[self.elevator2.current_floor].setStyleSheet(
                "color: lightgray;background-color : green;border-radius : 50;border : 2px solid black"
            )
        else:
            self.elev2[self.elevator2.current_floor].setStyleSheet(
                "color: lightgray;background-color : darkorange;border-radius : 50;border : 2px solid gray"
            )

        if self.elevator3.is_stop:
            self.elev3[self.elevator3.current_floor].setStyleSheet(
                "color: lightgray;background-color : green;border-radius : 50;border : 2px solid black"
            )
        else:
            self.elev3[self.elevator3.current_floor].setStyleSheet(
                "color: lightgray;background-color : darkorange;border-radius : 50;border : 2px solid gray"
            )
        if(self.elevator1.direction == "DOWN"):
            self.dir[0].setText("⇊",)
            self.dir[0].setStyleSheet(
                "color: darkorange;border-radius : 16;border : 2px solid black;background-color : black ")
        if(self.elevator2.direction == "DOWN"):
            self.dir[1].setText("⇊")
            self.dir[1].setStyleSheet(
                "color: darkorange;border-radius : 16;border : 2px solid black;background-color : balck")
        if(self.elevator3.direction == "DOWN"):
            self.dir[2].setText("⇊")
            self.dir[2].setStyleSheet(
                "color: darkorange;border-radius : 16;border : 2px solid black;background-color : balck")

           
        if(self.elevator1.direction == "UP"):
            self.dir[0].setText("⇈")
            self.dir[0].setStyleSheet(
                "color: darkgreen;border-radius : 16;border : 2px solid black;background-color : balck")

        if(self.elevator2.direction == "UP"):
            self.dir[1].setText("⇈")
            self.dir[1].setStyleSheet(
                "color: darkgreen;border-radius : 16;border : 2px solid black;background-color : balck")

        if(self.elevator3.direction == "UP"):
            self.dir[2].setText("⇈")
            self.dir[2].setStyleSheet(
                "color: darkgreen;border-radius : 16;border : 2px solid black;background-color : balck ")
