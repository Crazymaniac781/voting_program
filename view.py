from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 479)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 238, 230);\n"
"QCheckBox::indicator { width: 100px; height: 100px;} ;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_main = QtWidgets.QLabel(self.centralwidget)
        self.label_main.setGeometry(QtCore.QRect(0, 0, 861, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_main.setFont(font)
        self.label_main.setTextFormat(QtCore.Qt.PlainText)
        self.label_main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main.setObjectName("label_main")
        self.label_candidate1 = QtWidgets.QLabel(self.centralwidget)
        self.label_candidate1.setGeometry(QtCore.QRect(20, 100, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_candidate1.setFont(font)
        self.label_candidate1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_candidate1.setObjectName("label_candidate1")
        self.label_candidate2 = QtWidgets.QLabel(self.centralwidget)
        self.label_candidate2.setGeometry(QtCore.QRect(620, 100, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_candidate2.setFont(font)
        self.label_candidate2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_candidate2.setObjectName("label_candidate2")
        self.button_candidate1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_candidate1.setGeometry(QtCore.QRect(30, 160, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_candidate1.setFont(font)
        self.button_candidate1.setStyleSheet("background-color: rgb(255, 34, 5);")
        self.button_candidate1.setObjectName("button_candidate1")
        self.button_candidate2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_candidate2.setGeometry(QtCore.QRect(630, 160, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_candidate2.setFont(font)
        self.button_candidate2.setStyleSheet("background-color: rgb(66, 66, 255);")
        self.button_candidate2.setObjectName("button_candidate2")
        self.label_votechoice = QtWidgets.QLabel(self.centralwidget)
        self.label_votechoice.setGeometry(QtCore.QRect(280, 140, 311, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_votechoice.setFont(font)
        self.label_votechoice.setAlignment(QtCore.Qt.AlignCenter)
        self.label_votechoice.setWordWrap(True)
        self.label_votechoice.setObjectName("label_votechoice")
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setGeometry(QtCore.QRect(280, 360, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_submit.setFont(font)
        self.button_submit.setStyleSheet("background-color: rgb(255, 216, 74);")
        self.button_submit.setObjectName("button_submit")
        self.label_candidate1vote = QtWidgets.QLabel(self.centralwidget)
        self.label_candidate1vote.setGeometry(QtCore.QRect(80, 250, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_candidate1vote.setFont(font)
        self.label_candidate1vote.setAlignment(QtCore.Qt.AlignCenter)
        self.label_candidate1vote.setObjectName("label_candidate1vote")
        self.label_candidate2vote = QtWidgets.QLabel(self.centralwidget)
        self.label_candidate2vote.setGeometry(QtCore.QRect(690, 240, 111, 111))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_candidate2vote.setFont(font)
        self.label_candidate2vote.setAlignment(QtCore.Qt.AlignCenter)
        self.label_candidate2vote.setObjectName("label_candidate2vote")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 290, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_main.setText(_translate("MainWindow", "Online Voter"))
        self.label_candidate1.setText(_translate("MainWindow", "Henry Thompson"))
        self.label_candidate2.setText(_translate("MainWindow", "Michelle Russell"))
        self.button_candidate1.setText(_translate("MainWindow", "Vote For Henry"))
        self.button_candidate2.setText(_translate("MainWindow", "Vote For Michelle"))
        self.label_votechoice.setText(_translate("MainWindow", "Please Select a Candidate"))
        self.button_submit.setText(_translate("MainWindow", "Submit"))
        self.label_candidate1vote.setText(_translate("MainWindow", "0"))
        self.label_candidate2vote.setText(_translate("MainWindow", "0"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Enter Your Name Here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
