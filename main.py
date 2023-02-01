import sys
from time import sleep

from PyQt6 import QtTest
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

import elevator
import GUI




elevator1 = elevator.Elevator(1)
elevator2 = elevator.Elevator(2)
elevator3 = elevator.Elevator(3)


stylesheet = """
    MainWindow {
        border-image: url("elev1.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
        
    }
"""

app = QApplication(sys.argv)
app.setStyleSheet(stylesheet)
window = GUI.MainWindow(elevator1, elevator2, elevator3)
window.show()
while True:
    if not window.pause:
        elevator1.move()
        elevator2.move()
        elevator3.move()
        window.update()
    QtTest.QTest.qWait(500)
    # if window.close:
    #     break

sys.exit(app.exec())
