class Message(object):
	'''
	Rotary encoder message DTO for the queue
	'''

	CCW = "counterclockwise"
	CW = "clockwise"
	BTN = "button"

	def __init__(self, id, msg):
		self.id = id
		self.msg = msg
