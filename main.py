import sys

from PyQt6 import QtTest
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QApplication

import elevator
import GUI

elevator1 = elevator.Elevator(1)
elevator2 = elevator.Elevator(2)
elevator3 = elevator.Elevator(3)


def move():
    elevator1.move()
    elevator2.move()
    elevator3.move()
    elevator1.update_age()
    elevator2.update_age()
    elevator3.update_age()


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
        move()
        window.update()
    QtTest.QTest.qWait(500)
    # if window.close:
    #     break

sys.exit(app.exec())
