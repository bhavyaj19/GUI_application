import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from functions import frame1, frame2, frame3, frame4, grid

# COLORS FFECEF FFCACA 372948 251B37  (Source: https://colorhunt.co/palette/251b37372948ffcacaffecef)
# dark-#251B37, light-#fb6667,
app = QApplication(sys.argv)  # initialising application
window = QWidget()
window.setWindowTitle("Welcome to this App")
window.move(600, 200)
window.setFixedWidth(1000) #to set fixed width
window.setFixedHeight(500) #to set fixed width
window.setStyleSheet("background: #251B37;")


frame1()

window.setLayout(grid)

window.show()  # to display app
sys.exit(app.exec())  # to hold the app screen, i guess?