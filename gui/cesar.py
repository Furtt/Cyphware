import sys
from PySide import QtGui, QtCore
from Function import cesar

class Display(QtGui.QWidget):
	def __init__(self,parent):
		super(Display,self).__init__(parent)
		
		self.grid = QtGui.QGridLayout()
		self.grid.setSpacing(10)
		
		self.editUp=QtGui.QTextEdit()
		self.editDown=QtGui.QTextEdit()
		self.decryptButton = QtGui.QPushButton(QtGui.QIcon('icon/Arrow-Up-icon.png'),"Decrypt")
		self.cryptButton = QtGui.QPushButton(QtGui.QIcon('icon/Arrow-Down-icon.png'),"Crypt")
		
		self.combo = QtGui.QComboBox(self)
		shift=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
		for i in shift:
			self.combo.addItem(i)

		self.grid.addWidget(self.editUp,1,0,1,3)
		self.grid.addWidget(self.cryptButton,2,0)
		self.grid.addWidget(self.decryptButton,2,1)
		self.grid.addWidget(self.combo,2,2)
		self.grid.addWidget(self.editDown,3,0,3,3)
		
		self.setLayout(self.grid)
		
		self.cryptButton.clicked[bool].connect(self.cryptAction)
		self.decryptButton.clicked[bool].connect(self.decryptAction)
		
	def cryptAction(self):
		text = self.editUp.toPlainText()
		key = self.combo.currentIndex()
		message = cesar.encrypt(text,key)
		self.editDown.setPlainText(message)

			
	def decryptAction(self):
		text = self.editDown.toPlainText()
		key = self.combo.currentIndex()
		message = cesar.decrypt(text,key)
		self.editUp.setPlainText(message)

