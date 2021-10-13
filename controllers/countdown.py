from PyQt5.QtCore import QThread, pyqtSignal
import time

class CountDown(QThread):
	ended = pyqtSignal()
	emitData = pyqtSignal(dict)
	stop = False

	def __init__(self, timeData):
		super().__init__()
		
		self.data = timeData

	def down(self):
		time.sleep(1)

		if self.data['seconds'] > 0:
			self.data['seconds'] -= 1
		elif self.data['minutes'] > 0: 
			self.data['seconds'] = 59
			self.data['minutes'] -= 1
		elif self.data['hours'] > 0:
			self.data['seconds'] = 59
			self.data['minutes'] = 59
			self.data['hours'] -= 1

		if all(t == 0 for t in self.data.values()):
			return False
		else:
			return True

	

	def run(self):
		while self.down() and not self.stop:
			self.emitData.emit(self.data)
		self.ended.emit()


