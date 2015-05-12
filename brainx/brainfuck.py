class BrainFuck:
	
	def __init__(self, data):
		self.data = data
		mem = b'\x00'
		self.memory = mem
		self.memoryPtr = 0
		self.output = ""
		self.bcode = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
		
		self.interpreter(self.bcode)
	
	def interpreter( self, bcode ):
		print(bcode)
		for i in range(0, len(bcode)):
			#print(bcode[i])
			self.calcMemory