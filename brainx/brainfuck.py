class BrainFuck:
	
	def __init__(self, data):
		self.data = data
		mem = b'\x00'
		self.memory = bytearray(mem)
		self.memoryPtr = 0
		self.output = ""
		self.bcode = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
		
		self.interpreter()
	
	def calcMemory( self, bChar ):
		print(self.memory[self.memoryPtr])
		if bChar == '+':
			if self.memory[self.memoryPtr] != 255:
				print(self.memory[self.memoryPtr])	
				self.memory[self.memoryPtr] += 1			
			else:
				self.memory[self.memoryPtr] = 0
		elif bChar == '-':    
			if self.memory[self.memoryPtr] != 0:
				self.memory[self.memoryPtr] -= 1
            
			else:
				self.memory[self.memoryPtr] = 255
		
		elif bChar == '>':
			self.memoryPtr += 1
			if len(self.memory) == self.memoryPtr:
				self.memory += bytearray([0])		
		
		elif bChar == '<':
			if self.memoryPtr > 0:
				self.memoryPtr -= 1

		elif bChar == ',':
			self.memory[self.memoryPtr] = ord(self._readchar())
		
		elif bChar == '.':
			print("+" + chr(self.memory[self.memoryPtr]), end=r'')
			self.output += chr(self.memory[self.memoryPtr])
		
		
	def interpreter( self ):
		print(self.bcode)
		for i in range(0, len(self.bcode)):
			self.calcMemory(self.bcode[i])