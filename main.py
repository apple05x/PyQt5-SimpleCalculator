from PyQt5 import QtWidgets
from PyQt5 import uic
import sys

ad = "calc.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(ad)

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.resultlabel.setText('')  
        self.current_input = ''
        self.result = 0

        self.buttons()

    def buttons(self):
        self.ui.persentbutton.clicked.connect(lambda: self.button_click('%'))
        self.ui.cbutton.clicked.connect(self.clear)
        self.ui.backspacebutton.clicked.connect(self.backspace)
        self.ui.dividebutton.clicked.connect(lambda: self.button_click('/'))
        self.ui.sevenbutton.clicked.connect(lambda: self.button_click('7'))
        self.ui.eightbutton.clicked.connect(lambda: self.button_click('8'))
        self.ui.ninebutton.clicked.connect(lambda: self.button_click('9'))
        self.ui.multiplybutton.clicked.connect(lambda: self.button_click('*'))
        self.ui.fourbutton.clicked.connect(lambda: self.button_click('4'))
        self.ui.fivebutton.clicked.connect(lambda: self.button_click('5'))
        self.ui.sixbutton.clicked.connect(lambda: self.button_click('6'))
        self.ui.minusbutton.clicked.connect(lambda: self.button_click('-'))
        self.ui.onebutton.clicked.connect(lambda: self.button_click('1'))
        self.ui.twobutton.clicked.connect(lambda: self.button_click('2'))
        self.ui.threebutton.clicked.connect(lambda: self.button_click('3'))
        self.ui.plusbutton.clicked.connect(lambda: self.button_click('+'))
        self.ui.plusminusbutton.clicked.connect(self.plus_minus)
        self.ui.zerobutton.clicked.connect(lambda: self.button_click('0'))
        self.ui.pointbutton.clicked.connect(lambda: self.button_click('.'))
        self.ui.resultbutton.clicked.connect(self.calculate_result)

    def button_click(self, char):
        self.current_input += char
        self.ui.resultlabel.setText(self.current_input)

    def clear(self):
        self.current_input = ''
        self.ui.resultlabel.setText('')

    def backspace(self):
        self.current_input = self.current_input[:-1]
        self.ui.resultlabel.setText(self.current_input)

    def plus_minus(self):
        if self.current_input:
            if self.current_input[0] == '-':
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
        self.ui.resultlabel.setText(self.current_input)

    def calculate_result(self):
        try:
            self.result = str(eval(self.current_input.replace('x', '*')))
            self.ui.resultlabel.setText(self.result)
            self.current_input = self.result
        except Exception as e:
            self.ui.resultlabel.setText('Error')
            self.current_input = ''

app = QtWidgets.QApplication([])
application = Calculator()
application.show()
sys.exit(app.exec())