from PyQt5.QtCore import QThread, pyqtSignal
from controllers.Tools import Tools
import time


class CountDown(QThread):
	ended = pyqtSignal()
	emitData = pyqtSignal(dict)
	stop = False

	def __init__(self, data):
		super().__init__()
		
		self.time_dict = data
		self.time_secs = data['seconds'] + (60 * data['minutes']) + ((60 * 60) * data['hours'])

	def down(self):
		time.sleep(1)

		self.time_secs -= 1

		secs_as_time = Tools.number_to_time(self.time_secs).split(':')

		self.time_dict['hours'] = secs_as_time[0]
		self.time_dict['minutes'] = secs_as_time[1]
		self.time_dict['seconds'] = secs_as_time[2]

		if self.time_secs == 0:
			return False
		else:
			return True

	def run(self):
		while self.down() and not self.stop:
			self.emitData.emit(self.time_dict)
		self.ended.emit()


