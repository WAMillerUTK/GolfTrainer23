from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Python ")
  
        # setting geometry
        self.setGeometry(100, 100, 500, 400)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
  
    # method for components
    def UiComponents(self):
  
  
        # creating a command link button
        cl_button = QCommandLinkButton("GeeksforGeeks", self)
  
        # setting geometry
        cl_button.setGeometry(200, 100, 200, 50)
  
        # setting animate click property
        cl_button.animateClick(200)
  
          
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())