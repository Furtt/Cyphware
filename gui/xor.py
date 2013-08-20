import sys
from PySide import QtGui
from Function import xor


class Display(QtGui.QWidget):
	def __init__(self,parent):
		super(Display,self).__init__(parent)
		
		self.grid = QtGui.QGridLayout()
		self.grid.setSpacing(10)
		self.cryptButton = QtGui.QPushButton(QtGui.QIcon('icon/Arrow-Down-icon.png'),"Crypt")
		self.combo = QtGui.QComboBox(self)
		shift=["ASCII","BIN"]
		for i in shift:
			self.combo.addItem(i)
		self.key = QtGui.QLabel('key')
		self.keyEdit = QtGui.QLineEdit()
		self.editUp=QtGui.QTextEdit()
		self.editDown=QtGui.QTextEdit()

		self.grid.addWidget(self.editUp,1,0,1,4)
		self.grid.addWidget(self.cryptButton,2,0)
		self.grid.addWidget(self.combo,2,1)
		self.grid.addWidget(self.key,2,2)
		self.grid.addWidget(self.keyEdit,2,3)
		self.grid.addWidget(self.editDown,3,0,3,4)

		self.setLayout(self.grid)
		
		self.cryptButton.clicked[bool].connect(self.cryptAction)
		
	def cryptAction(self):
		text = self.editUp.toPlainText()
		key = self.keyEdit.text()
		outputType = self.combo.currentIndex()
		message = xor.xorCipher(text,key,outputType)
		self.editDown.setPlainText(message)
