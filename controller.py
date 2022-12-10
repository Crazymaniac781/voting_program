from PyQt5.QtWidgets import *
from view import *

class Controller(QMainWindow, Ui_MainWindow):
    candidate1 = 0
    candidate2 = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_candidate1.clicked.connect(lambda: self.vote_1())
        self.button_candidate2.clicked.connect(lambda: self.vote_2())
        self.button_submit.clicked.connect(lambda: self.checkname())
        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_submit.clicked.connect(lambda: self.name())

    def vote_1(self):
        self.vote = 1
        self.label_votechoice.setText(f'You Have Voted For Henry')

    def vote_2(self):
        self.vote = 2
        self.label_votechoice.setText(f'You Have Voted For Michelle')

    def submit(self):
        name_check = self.textEdit.toPlainText()

        if name_check == '':
            if self.vote == 1 or self.vote == 2:
                self.label_votechoice.setText('Please Enter Your Name')
            else:
                self.label_votechoice.setText('Click the Button to Select Candidate')

        elif self.vote == 1:
            self.candidate1 += 1
            self.label_candidate1vote.setText(str(self.candidate1))
            self.label_votechoice.setText('Please Select a Candidate')
            self.vote = 0

        elif self.vote == 2:
            self.candidate2 += 1
            self.label_candidate2vote.setText(str(self.candidate2))
            self.label_votechoice.setText('Please Select a Candidate')
            self.vote = 0

        elif self.vote == 3:
            self.label_votechoice.setText('You Have Voted Already')



    def name(self):
        myname = self.textEdit.toPlainText()
        with open('names.csv', 'a') as f:
            if myname != '':
                f.write('\n' + myname)

        self.textEdit.setText('')

    def checkname(self):
        name = self.textEdit.toPlainText()
        with open('names.csv', 'r') as fp:
            s = fp.read()

        if name in s:
            self.vote = 3