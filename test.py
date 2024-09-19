import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('我的窗口')
        self.setGeometry(50, 50, 200, 150)
        self.gridlayout = QGridLayout()
        self.setLayout(self.gridlayout)
        self.mylabel = QLabel('0', self)
        self.mylabel.setFont(QFont('Arial', 24))
        self.gridlayout.addWidget(self.mylabel, 0, 0, 1, 2)
        self.mybutton1 = QPushButton('开始', self)
        self.mybutton1.clicked.connect(self.startTimer)
        self.gridlayout.addWidget(self.mybutton1, 1, 0)
        self.mybutton2 = QPushButton('停止', self)
        self.mybutton2.clicked.connect(self.stopTimer)
        self.mybutton2.setDisabled(True)
        self.gridlayout.addWidget(self.mybutton2, 1, 1)
        self.mytimer = QTimer(self)
        self.mytimer.timeout.connect(self.onTimer)

    def startTimer(self):
        self.counter = 0
        self.mylabel.setText('开始计时...')
        self.mybutton1.setDisabled(True)
        self.mybutton2.setDisabled(False)
        self.mytimer.start(1000)

    def stopTimer(self):
        self.mylabel.setText('停止计时')
        self.mybutton1.setDisabled(False)
        self.mybutton2.setDisabled(True)
        self.mytimer.stop()

    def onTimer(self):
        self.counter += 1
        self.mylabel.setText(str(self.counter))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
