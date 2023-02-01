from time import sleep
import elevator
import GUI
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




def get_input(elv):
    inp = input("Enter floor and destination: ")
    if inp == '' :
        return
    inp = inp.split()
    if len(inp) == 1:
         elv.add_internal_req(int(inp[0]))
    elif len(inp) == 2:
        elv.add_external_req(int(inp[0]), int(inp[1]))

def nearest_elevator(elv1,elv2,elv3, floor):
    return min([elv1,elv2,elv3], key=lambda x: x.arrival_time(floor))

elevator1 = elevator.Elevator(1)
elevator2 = elevator.Elevator(2)
elevator3 = elevator.Elevator(3)
elevator1.current_floor=5
elevator1.add_internal_req(2)
elevator2.add_external_req(3,5)
elevator2.add_external_req(4,5)
elevator2.add_external_req(3,8)
elevator3.add_internal_req(3)

elevator1.is_stop=False
elevator2.current_floor=10
elevator2.is_stop=True
elevator3.current_floor=5
elevator3.is_stop=False


print(elevator2.external_req)
for j in range (len(elevator2.external_req)):
    print(elevator2.external_req[j][1])
#print (elevator2.external_req[0].index(5))
stylesheet = """
    MainWindow {
        border-image: url("elev1.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
        
    }
"""

app=QApplication(sys.argv)
app.setStyleSheet(stylesheet)
window= GUI.MainWindow(elevator1,elevator2,elevator3)
window.moveElevator(elevator1,elevator2,elevator3)
window.show()
#app.exec()

#while True:
    #get_input(elevator1)
    #elevator1.do()
    #get_input(elevator2)
    #elevator2.do()
    #get_input(elevator3)
    #elevator3.do()
    #if(len(elevator1.internal_req)!=0 | len(elevator2.internal_req)!=0 | len(elevator3.internal_req)!=0  ):
        #print(elevator1.internal_req)
        #print(elevator2.internal_req)
        #print(elevator3.internal_req)
    #sleep(1)
window.moveElevator(elevator1,elevator2,elevator3)
#while(len(elevator1.internal_req)!=0 or len(elevator2.internal_req)!=0 or len(elevator3.internal_req)!=0 or\
   # len(elevator1.external_req)!=0 or len(elevator2.external_req)!=0 or len(elevator3.external_req)!=0):
   # window.moveElevator(elevator1,elevator2,elevator3)
   # elevator1.internal_req.clear()
   # elevator3.external_req.clear()
    
    







sys.exit(app.exec())