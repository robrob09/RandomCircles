import random
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 422)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 30, 271, 71))
        self.pushButton.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Рисовать"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Git и желтые окружности")
        self.pushButton.clicked.connect(self.paint)
        self.doRepaint = False

    def paint(self):
        self.doRepaint = True
        self.repaint()
        self.doRepaint = False

    def paintEvent(self, event):
        if self.doRepaint:
            painter = QPainter()
            painter.begin(self)
            painter.setPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            radius = random.randint(20, 120)
            painter.drawEllipse(230, 211, radius, radius)
            painter.end()


if __name__ == '__main__':
    application = QApplication(sys.argv)
    execute = MainWindow()
    execute.show()
    sys.exit(application.exec_())
