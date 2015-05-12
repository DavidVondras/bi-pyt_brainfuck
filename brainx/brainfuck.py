class BrainFuck
	
	def __init__(self, data):
		self.data = data
		mem = b'\x00'
		self.memory = mem
		self.memorzPtr = 0
		self.output = ""
		try:
            with open(data, mode='r') as f:
                self.bcode = f.read()
        except:
            self.bcode = data
		
		self.interpreter(self.bcode)
	
	def interpreter( self, bcode ):
		