import sys
import functools 
from functools import partial
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton , QWidget
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
import elevator



class MainWindow(QMainWindow , QWidget):
    def __init__(self,elevator1,elevator2,elevator3):

        super().__init__()

        self.elevator1=elevator1
        self.elevator2=elevator2
        self.elevator3=elevator3
        self.elev1 = []
        self.elev2 = []
        self.elev3 = []  
        self.textbox = [] 
        self.okbtn=[] 
        self.saveInfo=[]
        self.Btn1=[]
        self.Btn2=[]
        self.create_elevators(elevator1,elevator2,elevator3)
        self.setWindowTitle("elevator")
        self.setFixedSize(QSize(800, 600))
        
       
        
    def create_elevators(self , elevator1,elevator2,elevator3):

        

        for i in range(15):
            j=1
            font = self.font()
            font.setPointSize(16)
            self.elev1.append(QPushButton(self))
            self.elev1[i].setFont(font)
            self.elev1[i].setGeometry(270, 517 - 30 * i,60,30)
            self.elev1[i].setText(str(i+1))
            self.elev1[i].setStyleSheet("color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray")
            self.elev1[i].clicked.connect(partial(self.setIntReq,i,j))
           

        for i in range(15):
            j=2
            font = self.font()
            font.setPointSize(16)
            self.elev2.append(QPushButton(self))
            self.elev2[i].setFont(font)
            self.elev2[i].setGeometry(360, 517 - 30 * i,60,30)
            self.elev2[i].setText( str(i+1))
            self.elev2[i].setStyleSheet("color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray")
            self.elev2[i].clicked.connect(partial(self.setIntReq,i,j))
                 

        for i in range(15):
            j=3
            font = self.font()
            font.setPointSize(16)
            self.elev3.append(QPushButton(self))
            self.elev3[i].setFont(font)
            self.elev3[i].setGeometry(450, 517 - 30 * i,60,30)
            self.elev3[i].setText(str(i+1))
            self.elev3[i].setStyleSheet("color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray ")
            self.elev3[i].clicked.connect(partial(self.setIntReq,i,j))
    


        for j in range(2):
            font = self.font()
            font.setPointSize(11)
            self.textbox.append(QLineEdit(self))
            if(j==0):
                self.textbox[j].setToolTip("enter current floor")
            if(j==1):
                self.textbox[j].setToolTip("enter destination floor")
                
            self.textbox[j].setGeometry(560, 270+50*j ,100,40)
            self.textbox[j].setFont(font)
            self.textbox[j].setStyleSheet("border-radius : 20;border : 2px solid black;background-color : darkgray")
            self.okbtn.append(QPushButton("OK",self))
            self.okbtn[j].setGeometry(625, 275+50*j, 32, 32)
            self.okbtn[j].setStyleSheet("color: lightgray;border-radius : 16;border : 2px solid black;background-color : black")
            self.okbtn[j].clicked.connect(lambda: self.setExtReq())

        for j in range(2):
            self.Btn1.append( QPushButton("",self))
            self.Btn1[j].setGeometry(162,269+50*j,40,40)
            self.Btn1[j].setStyleSheet("color: black;border-radius : 20;border : 2px solid black;background-color : black")
            if(j==0):
                self.Btn2.append( QPushButton("⏸",self))
            if(j==1):
                self.Btn2.append( QPushButton("⏴",self))
            font.setPointSize(18)
            self.Btn2[j].setFont(font)
            self.Btn2[j].setGeometry(168,275+50*j,28,28)
            self.Btn2[j].setStyleSheet("color: black;border-radius : 14;border : 2px solid black;background-color :darkgray")
    

    def setExtReq(self):     
        self.elevator1.add_external_req(self.textbox[0].text(),self.textbox[1].text())
        self.elevator2.add_external_req(self.textbox[0].text(),self.textbox[1].text())
        self.elevator3.add_external_req(self.textbox[0].text(),self.textbox[1].text())
        print(self.textbox[0].text(),self.textbox[1].text())

    def setIntReq(self,i,j):   
        if(j==1):
            self.elevator1.add_internal_req(i+1)
            print(i+1)
        if(j==2):
            self.elevator2.add_internal_req(i+1)
            print(i+1)
        if(j==3):
            self.elevator3.add_internal_req(i+1)
            print(i+1)

   
    def moveElevator(self, elevator1 , elevator2, elevator3):
        for i in range(15):
            self.elev1[i].setStyleSheet("color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray")
            self.elev2[i].setStyleSheet("color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray")
            self.elev3[i].setStyleSheet("color: black;background-color : lightgray ;border-radius : 50;border : 1px solid darkgray")
            if i in self.elevator1.internal_req:
                self.elev1[i-1].setStyleSheet("color: black;background-color : red ;border-radius : 50;border : 2px solid black")

            if i in self.elevator2.internal_req:
                self.elev2[i-1].setStyleSheet("color: black;background-color : red ;border-radius : 50;border : 2px solid black")
               
            if i in self.elevator3.internal_req:
                self.elev3[i-1].setStyleSheet("color: black;background-color : red ;border-radius : 50;border : 2px solid black")
            for j in range (len(elevator1.external_req)):
                
                if (self.elevator1.external_req[j][1]==i):
                    self.elev1[i-1].setStyleSheet("color: black;background-color : red ;border-radius : 50;border : 2px solid black")
            for j in range (len(elevator2.external_req)):
                if (self.elevator2.external_req[j][1]==i):
                    self.elev2[i-1].setStyleSheet("color: black;background-color : red ;border-radius : 50;border : 2px solid black")
            for j in range (len(elevator3.external_req)):
                if (self.elevator3.external_req[j][1]==i):
                    self.elev3[i-1].setStyleSheet("color: black;background-color : red ;border-radius : 50;border : 2px solid black")
    

        if(self.elevator1.is_stop):
            self.elev1[self.elevator1.current_floor].setStyleSheet("color: lightgray;background-color : green;border-radius : 50;border : 2px solid black")
        else:
            self.elev1[self.elevator1.current_floor].setStyleSheet("color: lightgray;background-color : darkorange;border-radius : 50;border : 2px solid black")

        if(elevator2.is_stop):
            self.elev2[self.elevator2.current_floor].setStyleSheet("color: lightgray;background-color : green;border-radius : 50;border : 2px solid black")
        else:
            self.elev2[self.elevator2.current_floor].setStyleSheet("color: lightgray;background-color : darkorange;border-radius : 50;border : 2px solid black")

        if(elevator3.is_stop):
            self.elev3[self.elevator3.current_floor].setStyleSheet("color: lightgray;background-color : green;border-radius : 50;border : 2px solid black")
        else:
            self.elev3[self.elevator3.current_floor].setStyleSheet("color: lightgray;background-color : darkorange;border-radius : 50;border : 2px solid black")
       
   





