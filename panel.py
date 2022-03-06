#!/usr/bin/python

from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication)
from PyQt6.QtCore import QTimer
import sys
from functools import partial
from control import homeassistant

class Panel(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.all_on = QPushButton('All On', self)
        self.all_on.clicked.connect(partial(self.toggleLight, self.all_on))
        self.all_on.setGeometry(50, 50, 100, 40)
        self.all_on.setStyleSheet("background-color : lightgrey;" "color : black;")

        self.all_off = QPushButton('All Off', self)
        self.all_off.clicked.connect(partial(self.toggleLight, self.all_off))
        self.all_off.setGeometry(50, 90, 100, 40)
        self.all_off.setStyleSheet("background-color : lightgrey;" "color : black;")

        self.light_1_on = QPushButton('On', self)
        self.light_1_on.setGeometry(170, 50, 100, 40)
        self.light_1_on.clicked.connect(partial(self.toggleLight, self.light_1_on))
        
        self.light_1_off = QPushButton('Off', self)
        self.light_1_off.setGeometry(170, 90, 100, 40)
        self.light_1_off.clicked.connect(partial(self.toggleLight, self.light_1_off))

        self.light_2_on = QPushButton('On', self)
        self.light_2_on.setGeometry(290, 50, 100, 40)
        self.light_2_on.clicked.connect(partial(self.toggleLight, self.light_2_on))
        
        self.light_2_off = QPushButton('Off', self)
        self.light_2_off.setGeometry(290, 90, 100, 40)
        self.light_2_off.clicked.connect(partial(self.toggleLight, self.light_2_off))

        self.light_3_on = QPushButton('On', self)
        self.light_3_on.setGeometry(410, 50, 100, 40)
        self.light_3_on.clicked.connect(partial(self.toggleLight, self.light_3_on))
        
        self.light_3_off = QPushButton('Off', self)
        self.light_3_off.setGeometry(410, 90, 100, 40)
        self.light_3_off.clicked.connect(partial(self.toggleLight, self.light_3_off))

        self.light_4_on = QPushButton('On', self)
        self.light_4_on.setGeometry(530, 50, 100, 40)
        self.light_4_on.clicked.connect(partial(self.toggleLight, self.light_4_on))
        
        self.light_4_off = QPushButton('Off', self)
        self.light_4_off.setGeometry(530, 90, 100, 40)
        self.light_4_off.clicked.connect(partial(self.toggleLight, self.light_4_off))

        self.setState()

        self.checkState = QTimer(self)
        self.checkState.timeout.connect(self.setState)
        self.checkState.start(1000)

        self.setGeometry(300, 300, 800, 480)
        self.setWindowTitle('Home Assistant')
        self.show()

    def setState(self):
        light_1_state = homeassistant.getState("light.fm_1")

        if light_1_state == 'on':
            self.light_1_on.setStyleSheet("background-color : green;" "color : white;")
            self.light_1_off.setStyleSheet("background-color : lightgrey;" "color : black;")
        else:
            self.light_1_on.setStyleSheet("background-color : lightgrey;" "color : black;")
            self.light_1_off.setStyleSheet("background-color : red;" "color : white;")

        light_2_state = homeassistant.getState("light.fm_2")

        if light_2_state == 'on':
            self.light_2_on.setStyleSheet("background-color : green;" "color : white;")
            self.light_2_off.setStyleSheet("background-color : lightgrey;" "color : black;")
        else:
            self.light_2_on.setStyleSheet("background-color : lightgrey;" "color : black;")
            self.light_2_off.setStyleSheet("background-color : red;" "color : white;")

        light_3_state = homeassistant.getState("light.fm_3")

        if light_3_state == 'on':
            self.light_3_on.setStyleSheet("background-color : green;" "color : white;")
            self.light_3_off.setStyleSheet("background-color : lightgrey;" "color : black;")
        else:
            self.light_3_on.setStyleSheet("background-color : lightgrey;" "color : black;")
            self.light_3_off.setStyleSheet("background-color : red;" "color : white;")

        light_4_state = homeassistant.getState("light.fm_4")

        if light_4_state == 'on':
            self.light_4_on.setStyleSheet("background-color : green;" "color : white;")
            self.light_4_off.setStyleSheet("background-color : lightgrey;" "color : black;")
        else:
            self.light_4_on.setStyleSheet("background-color : lightgrey;" "color : black;")
            self.light_4_off.setStyleSheet("background-color : red;" "color : white;")


    def toggleLight(self, button):

        if button == self.all_on:
            lights = ['light.fm_1', 'light.fm_2', 'light.fm_3', 'light.fm_4']
            homeassistant.lightToggle(lights, "turn_on")
            self.light_1_on.setStyleSheet("background-color : green;" "color : white;")
            self.light_1_off.setStyleSheet("background-color : lightgrey;" "color : black;")
            self.light_2_on.setStyleSheet("background-color : green;" "color : white;")
            self.light_2_off.setStyleSheet("background-color : lightgrey;" "color : black;")
            self.light_3_on.setStyleSheet("background-color : green;" "color : white;")
            self.light_3_off.setStyleSheet("background-color : lightgrey;" "color : black;")
            self.light_4_on.setStyleSheet("background-color : green;" "color : white;")
            self.light_4_off.setStyleSheet("background-color : lightgrey;" "color : black;")
        elif button == self.all_off:
            lights = ['light.fm_1', 'light.fm_2', 'light.fm_3', 'light.fm_4']
            homeassistant.lightToggle(lights, "turn_off")
            self.light_1_off.setStyleSheet("background-color : red;" "color : white;")
            self.light_1_on.setStyleSheet("background-color : lightgrey;" "color : black;")
            self.light_2_off.setStyleSheet("background-color : red;" "color : white;")
            self.light_2_on.setStyleSheet("background-color : lightgrey;" "color : black;")
            self.light_3_off.setStyleSheet("background-color : red;" "color : white;")
            self.light_3_on.setStyleSheet("background-color : lightgrey;" "color : black;")
            self.light_4_off.setStyleSheet("background-color : red;" "color : white;")
            self.light_4_on.setStyleSheet("background-color : lightgrey;" "color : black;")
        elif button == self.light_1_on:
            self.light_1_on.setStyleSheet("background-color : green;" "color : white;")
            self.light_1_off.setStyleSheet("background-color : lightgrey;" "color : black;")
            homeassistant.lightToggle("light.fm_1", "turn_on")
        elif button == self.light_1_off:
            self.light_1_off.setStyleSheet("background-color : red;" "color : white;")
            self.light_1_on.setStyleSheet("background-color : lightgrey;" "color : black;")
            homeassistant.lightToggle("light.fm_1", "turn_off")
        elif button == self.light_2_on:
            self.light_2_on.setStyleSheet("background-color : green;" "color : white;")
            self.light_2_off.setStyleSheet("background-color : lightgrey;" "color : black;")
            homeassistant.lightToggle("light.fm_2", "turn_on")
        elif button == self.light_2_off:
            self.light_2_off.setStyleSheet("background-color : red;" "color : white;")
            self.light_2_on.setStyleSheet("background-color : lightgrey;" "color : black;")
            homeassistant.lightToggle("light.fm_2", "turn_off")
        elif button == self.light_3_on:
            self.light_3_on.setStyleSheet("background-color : green;" "color : white;")
            self.light_3_off.setStyleSheet("background-color : lightgrey;" "color : black;")
            homeassistant.lightToggle("light.fm_3", "turn_on")
        elif button == self.light_3_off:
            self.light_3_off.setStyleSheet("background-color : red;" "color : white;")
            self.light_3_on.setStyleSheet("background-color : lightgrey;" "color : black;")
            homeassistant.lightToggle("light.fm_3", "turn_off")
        elif button == self.light_4_on:
            self.light_4_on.setStyleSheet("background-color : green;" "color : white;")
            self.light_4_off.setStyleSheet("background-color : lightgrey;" "color : black;")
            homeassistant.lightToggle("light.fm_4", "turn_on")
        elif button == self.light_4_off:
            self.light_4_off.setStyleSheet("background-color : red;" "color : white;")
            self.light_4_on.setStyleSheet("background-color : lightgrey;" "color : black;")
            homeassistant.lightToggle("light.fm_4", "turn_off")



def main():

    app = QApplication(sys.argv)
    ex = Panel()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()