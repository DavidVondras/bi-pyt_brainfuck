class BrainFuck:
	
	def __init__(self, data):
		self.data = data
		mem = b'\x00'
		self.memory = mem
		self.memoryPtr = 0
		self.output = ""
		self.bcode = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
		
		self.interpreter(self.bcode)
	
	def calcMemory( bChar ):
		 if bChar == '+':
            if self.memory[self.memoryPtr] != 255:
				self.memory[self.memoryPtr] += 1
            else:
				self.memory[self.memoryPtr] = 0

        elif c[c_i] == '-':
            if self.memory[self.Ptr] != 0:
				self.memory[self.Ptr] -= 1
            else:
				self.memory[self.Ptr] = 255
	
	def interpreter( self, bcode ):
		print(bcode)
		for i in range(0, len(bcode)):
			self.calcMemory(bcode[i])