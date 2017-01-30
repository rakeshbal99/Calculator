#Rakesh Bal
#Roll No-16CS10043
#Hall- LBS Hall
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from math import *
#importing GUI from KossCalci.py file
import KossCalci

class MainWindow(QMainWindow,KossCalci.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #sending signals to lineEdit after a certain pushbutton is pressed
        self.connect(self.pClear, SIGNAL("clicked()"), lambda: self.lineEdit.clear())
        self.connect(self.pClear2, SIGNAL("clicked()"), lambda: self.lineEdit.clear())
        self.connect(self.pBackspace, SIGNAL("clicked()"), lambda: self.lineEdit.backspace())
        self.connect(self.pBackspace2, SIGNAL("clicked()"), lambda: self.lineEdit.clear())
        self.connect(self.p0, SIGNAL("clicked()"), lambda : self.lineEdit.insert('0'))
        self.connect(self.p1, SIGNAL("clicked()"), lambda : self.lineEdit.insert('1'))
        self.connect(self.p2, SIGNAL("clicked()"), lambda: self.lineEdit.insert('2'))
        self.connect(self.p3, SIGNAL("clicked()"), lambda: self.lineEdit.insert('3'))
        self.connect(self.p4, SIGNAL("clicked()"), lambda: self.lineEdit.insert('4'))
        self.connect(self.p5, SIGNAL("clicked()"), lambda: self.lineEdit.insert('5'))
        self.connect(self.p6, SIGNAL("clicked()"), lambda: self.lineEdit.insert('6'))
        self.connect(self.p7, SIGNAL("clicked()"), lambda: self.lineEdit.insert('7'))
        self.connect(self.p8, SIGNAL("clicked()"), lambda: self.lineEdit.insert('8'))
        self.connect(self.p9, SIGNAL("clicked()"), lambda: self.lineEdit.insert('9'))
        self.connect(self.pDot, SIGNAL("clicked()"), lambda: self.lineEdit.insert('.'))
        self.connect(self.pDivision, SIGNAL("clicked()"), lambda: self.lineEdit.insert('/'))
        self.connect(self.pMultiply, SIGNAL("clicked()"), lambda: self.lineEdit.insert('*'))
        self.connect(self.pSubstract, SIGNAL("clicked()"), lambda: self.lineEdit.insert('-'))
        self.connect(self.pAdd, SIGNAL("clicked()"), lambda: self.lineEdit.insert('+'))
        # evaluateExp is the function for displaying output
        self.connect(self.pEqualTo, SIGNAL("clicked()"), lambda: self.evaluateExp())
        self.connect(self.pEqualTo2, SIGNAL("clicked()"), lambda: self.evaluateExp())
        self.connect(self.pSin, SIGNAL("clicked()"), lambda: self.lineEdit.insert('sin('))
        self.connect(self.pCos, SIGNAL("clicked()"), lambda: self.lineEdit.insert('cos('))
        self.connect(self.pTan, SIGNAL("clicked()"), lambda: self.lineEdit.insert('tan('))
        self.connect(self.pASin, SIGNAL("clicked()"), lambda: self.lineEdit.insert('asin('))
        self.connect(self.pACos, SIGNAL("clicked()"), lambda: self.lineEdit.insert('acos('))
        self.connect(self.pATan, SIGNAL("clicked()"), lambda: self.lineEdit.insert('atan('))
        self.connect(self.pSinh, SIGNAL("clicked()"), lambda: self.lineEdit.insert('sinh('))
        self.connect(self.pCosh, SIGNAL("clicked()"), lambda: self.lineEdit.insert('cosh('))
        self.connect(self.pTanh, SIGNAL("clicked()"), lambda: self.lineEdit.insert('tanh('))
        self.connect(self.pNaturalLog, SIGNAL("clicked()"), lambda: self.lineEdit.insert('log('))
        self.connect(self.pLog, SIGNAL("clicked()"), lambda: self.lineEdit.insert('log10('))
        self.connect(self.pSqrt, SIGNAL("clicked()"), lambda: self.lineEdit.insert('sqrt('))
        self.connect(self.pOpenParenthesis, SIGNAL("clicked()"), lambda: self.lineEdit.insert('('))
        self.connect(self.pCloseParenthesis, SIGNAL("clicked()"), lambda: self.lineEdit.insert(')'))
        self.connect(self.pOpenParenthesis2, SIGNAL("clicked()"), lambda: self.lineEdit.insert('('))
        self.connect(self.pCloseParenthesis2, SIGNAL("clicked()"), lambda: self.lineEdit.insert(')'))
        self.connect(self.pFloor, SIGNAL("clicked()"), lambda: self.lineEdit.insert('floor('))
        self.connect(self.pCeil, SIGNAL("clicked()"), lambda: self.lineEdit.insert('ceil('))
        self.connect(self.pExponential, SIGNAL("clicked()"), lambda: self.lineEdit.insert('e'))
        self.connect(self.pPI, SIGNAL("clicked()"), lambda: self.lineEdit.insert('pi'))
        self.connect(self.pExponent, SIGNAL("clicked()"), lambda: self.lineEdit.insert('**'))
        self.connect(self.pFact, SIGNAL("clicked()"), lambda: self.lineEdit.insert('factorial('))
        self.connect(self.pRem, SIGNAL("clicked()"), lambda: self.lineEdit.insert(','))
        self.connect(self.pAbs, SIGNAL("clicked()"), lambda: self.lineEdit.insert('fabs('))
        self.connect(self.pMod, SIGNAL("clicked()"), lambda: self.lineEdit.insert('fmod('))
        #the following will enavle the user to directly enter input directly from keyboard.
        self.connect(self.lineEdit, SIGNAL("returnPressed()"), lambda :self.evaluateExp())



    def evaluateExp(self):
         try:
             exp = self.lineEdit.text()
             self.result = eval(exp)
             #the result to be displayed in lcd.
             self.lcdNumber.display(self.result)
         except:
             #error handling to be printed in lineEdit
             self.lineEdit.setText("%s is INVALID" % exp)

#instance of QApplication to execute the code.
app=QApplication(sys.argv)
form=MainWindow()
form.show()
app.exec_()