import sys
#from __future__ import print_function

class BrainFuck:

    def __init__(self, data, memory=b'\x00', pointer=0, test=0, end=0):
        self.data = data
        self.memory = bytearray(memory)
        self.memoryPtr = pointer
        try:
            with open(data, mode='r') as f:
                self.code = f.read()
        except:
            self.code = data
        self.output = ""
        self.debugIter = 1
        self.user_input = self.findExp()
        self.interpreter(self.code)
        if test == 1:
            self.getTest()
        x = self.output
        if x == '':
            sys.stdout.write(x)
            #print(x, end='')
        if end == 0:
            sys.exit(0)

    def clearCode(self):
        chars = ['.', ',', '[', ']', '<', '>', '+', '-', '#', '!']
        clearCodeData = self.code
        ret = ''
        for i in range(0, len(clearCodeData)):
            if clearCodeData[i] in chars:
                ret += clearCodeData[i]
        return ret

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
                sys.stdout.write(chr(self.memory[self.memoryPtr]))
                self.output += chr(self.memory[self.memoryPtr])
            if bcode[i] == ',':
                self.memory[self.memoryPtr] = ord(self.getchar())
            if bcode[i] == '[':
                code = self.cycle(bcode[i:])
                while self.memory[self.memoryPtr] != 0:
                    self.interpreter(code)
                i += len(code) + 1
            if bcode[i] == '#':
                debugStr = ""
                if self.debugIter < 10:
                    debugStr = "0" + str(self.debugIter)
                else:
                    debugStr = str(self.debugIter)
                memStr = str(self.memory)
                memStr = memStr.replace('bytearray(', '')
                memStr = memStr.replace(')', '')
                f = open('debug_' + debugStr + ".log", 'w')
                deb = "# program data\n"
                deb += self.clearCode() + "\n\n"
                deb += "# memory\n"
                deb += memStr + "\n\n"
                deb += "# memory pointer\n"
                deb += str(self.memoryPtr) + "\n\n"
                deb += "# output\n"
                #f.write(deb)
                #deb = self.output.encode()
                #f.write(deb, end="")                
                deb += str(self.output.encode())
                #f.write(deb, end="")                   
                f.write(deb + "\n\n")
                f.close
                self.debugIter += 1
            i += 1

    def findExp(self):
        """finfing the stupid !"""
        i = 0
        while i < len(self.code) and self.code[i] != '!':
            i += 1

        if i + 1 < len(self.code):
            ret = self.code[i + 1:]
            self.code = self.code[:i]
            return ret

        return ''

    def cycle(self, bcode):
        end = 1
        while (bcode[0:end].count('[') != bcode[0:end].count(']')):
            end += 1
        return bcode[1:end - 1]

    def getTest(self):
        debugStr = ""
        if self.debugIter < 10:
            debugStr = "0" + str(self.debugIter)
        else:
            debugStr = str(self.debugIter)
        self.clearCode()
        memStr = str(self.memory)
        memStr = memStr.replace('bytearray(', '')
        memStr = memStr.replace(')', '')
        f = open('debug_' + debugStr + ".log", 'w')
        deb = "# program data\n"
        deb += self.clearCode() + "\n\n"
        deb += "# memory\n"
        deb += memStr + "\n\n"
        deb += "# memory pointer\n"
        deb += str(self.memoryPtr) + "\n\n"
        deb += "# output\n"
        #f.write(deb)
        deb += str(self.output.encode())
        #f.write(deb, end="")                
        f.write(deb + "\n\n")
        #f.write(deb)
        f.close

    def getchar(self):
        if len(self.user_input) == 0:
            return sys.stdin.read(1)
        else:
            ret = self.user_input[0]
            self.user_input = self.user_input[1:]
            return ret

if __name__ == "__main__":
    data = "../tests/hello1.b"
    sys.exit(BrainFuck(data))
