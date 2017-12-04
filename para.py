class Params:
	__slots__ = ('max', 'w2i', 'i2w', 'c2i')
	
	def __init__(self, m, w2i, i2w, c2i):
		self.max = m
		self.w2i = w2i
		self.i2w = i2w
		self.c2i = c2i

class Data:
	__slots__ = ('txtIn', 'catIn', 'out')
	
	def __init__(self, txtIn, catIn, out):
		self.txtIn = txtIn
		self.catIn = catIn
		self.out = out
	
	def getJointInput(self):
		return [self.txtIn] + self.catIn
