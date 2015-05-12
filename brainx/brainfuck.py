import sys


class BrainFuck:

    def __init__(self, data):
        self.data = data
        mem = b'\x00'
        self.memory = bytearray(mem)
        self.memoryPtr = 0
        self.output = ""
        self.bcode = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
        self.interpreter(self.bcode)

    def interpreter(self, bcode):
        i = 0
        while i < len(bcode):
            if bcode[i] == '>':
                self.memoryPtr += 1
                if len(self.memory) == self.memoryPtr:
                    self.memory += bytearray([0])
            if bcode[i] == '<':
                if self.memoryPtr > 0:
                    self.memoryPtr -= 1
            if bcode[i] == '+':
                self.memory[self.memoryPtr] += 1
                if self.memory[self.memoryPtr] == 256:
                    self.memory[self.memoryPtr] = 0
            if bcode[i] == '-':
                self.memory[self.memoryPtr] -= 1
                if self.memory[self.memoryPtr] == -1:
                    self.memory[self.memoryPtr] = 255
            if bcode[i] == '.':
                print(chr(self.memory[self.memoryPtr]))
                self.output += chr(self.memory[self.memoryPtr])
            if bcode[i] == ',':
                self.memory[self.memoryPtr] = ord(self.getchar())
            if bcode[i] == '[':
                code = self.cycle(bcode[i:])
                while self.memory[self.memoryPtr] != 0:
                    self.interpreter(code)
                i += len(code) + 1
            i += 1

    def cycle(self, bcode):
        end = 1
        while (bcode[0:end].count('[') != bcode[0:end].count(']')):
            end += 1
        return bcode[1:end - 1]

    def getchar(self):
        if len(self.user_input) == 0:
            return sys.stdin.read(1)
        else:
            ret = self.user_input[0]
            self.user_input = self.user_input[1:]
            return ret