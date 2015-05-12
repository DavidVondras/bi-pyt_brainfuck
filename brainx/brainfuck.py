class BrainFuck:
	
	def __init__(self, data):
		self.data = data
		mem = b'\x00'
		self.memory = mem
		self.memoryPtr = 0
		self.output = ""
		self.bcode = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
		
		self.interpreter(self.bcode)
	
	def calcMemory( self, bChar ):
		 if bChar == '+':
            if self.memory[self.memoryPtr] != 255:
				self.memory[self.memoryPtr] += 1
            else:
				self.memory[self.memoryPtr] = 0

        elif bChar == '-':
            if self.memory[self.Ptr] != 0:
				self.memory[self.Ptr] -= 1
            else:
				self.memory[self.Ptr] = 255
		elif bChar == '>':
			self.memoryPtr += 1
			if len(self.memory) == self.memoryPtr:
				self.memory += bytearray([0])		
		
		elif bChar == '>':
			self.memory_pointer += 1
            if len(self.memory) == self.memoryPtr:
				self.memory += bytearray([0])

		elif bChar == '<':
			if self.memoryPtr > 0:
				self.memoryPtr -= 1

		elif bChar == ',':
			self.memory[self.memoryPtr] = ord(self._readchar())
		
		elif c[c_i] == '.':
			print(chr(self.memory[self.memoryPtr]), end=r'')
			self.output += chr(self.memory[self.memoryPtr])
		
	def interpreter( self, bcode ):
		print(bcode)
		for i in range(0, len(bcode)):
			self.calcMemory(bcode[i])