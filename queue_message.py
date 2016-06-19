class Message(object):
	'''
	Rotary encoder message DTO for the queue
	'''

	CCW = "counterclockwise"
	CW = "clockwise"
	BTN = "button"

	def __init__(self, id, msg, timestamp=0):
		self.id = id
		self.msg = msg
		self.timestamp = timestamp
