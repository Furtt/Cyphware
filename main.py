import sys
from gui import xor,cesar
import signal
from PySide import QtGui

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
		
		self.initUI()
	
	def initUI(self):		
#__________________MenuBar _____________________ 
		menubar = self.menuBar()
	#______File________		
		fileMenu = menubar.addMenu('&File')
	#______Edit________
		editMenu = menubar.addMenu('&Edit')
	#______Cryptage______
		cryptageMenu = menubar.addMenu('&Cryptage')
		#________XOR____________
		xorAction = QtGui.QAction('XOR',self,shortcut = None,statusTip = None)
		xorAction.triggered.connect(self.xorDisplay)
		cryptageMenu.addAction(xorAction)
		#________Cesar__________
		cesarAction = QtGui.QAction('Cesar',self,shortcut = None, statusTip = None)
		cesarAction.triggered.connect(self.cesarDisplay)
		cryptageMenu.addAction(cesarAction)
		
#__________________Display______________________
		self.resize(500,300)
		self.setWindowTitle('Cryptool')
		self.setWindowIcon(QtGui.QIcon('icon/crypto.png'))
		self.show()
	
	def xorDisplay(self):
		self.setCentralWidget(xor.Display(self))
	def cesarDisplay(self):
		self.setCentralWidget(cesar.Display(self))
		
def main():
	app = QtGui.QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
