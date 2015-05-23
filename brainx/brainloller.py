# -*- coding: utf-8 -*-

import image
import brainfuck


class BrainLoller():
    def __init__(self, filename, printCode="", printOut=0, test=0):
        self.test = []
        self.data = self.getBrainLoller(filename)
        if printCode == "":
            if printOut == 0:
                if test == 0:
                    brainfuck.BrainFuck(self.data)
                else:
                    #print("test")
                    brainfuck.BrainFuck(self.data, b'\x00', 0, 1, 1)
                    myfile = open("debug_01.log", "a")
                    myfile.write("# RGB input\n")
                    testOut = "[\n    ["
                    y = 0
                    for y in range(0, int(len(self.test) / self.width)):
                        #print("------: " + str(y%2) + "   " + str(y))
                        if y % 2 == 0:
                            e = y * self.width + self.width
                            #print(str(y * self.width) + " e: " + str(e))
                            for i in range(y * self.width, e):
                                testOut += self.test[i]
                        else:
                            i = y * self.width + self.width - 1
                            while i >= y * self.width:
                                #print(i/self.width)
                            #for i in range(e, y * self.width):
                                testOut += self.test[i]
                                i -= 1
                        testOut += "],\n    ["
                        y = 0
                    testOut = testOut.replace(")(", "), (")
                    testOut += ']\n]\n\n'
                    testOut = testOut.replace("\n    []", "")
                    myfile.write(testOut)
                    myfile.close()
                #print(" "x.output)
            else:
                print((self.data))
        else:
            f = open(printCode, 'w')
            f.write(self.data)

    def readImage(self, filename):
        x = image.ImagePng(filename)
        self.rgb = x.rgb
        self.width = x.width

    def getBrainLoller(self, filename):
        self.readImage(filename)
        start = 0, 0
        m = 0, 1
        ret = ''
        while not self.out(start):
            o, m = self.getChars(self.rgb[start[0]][start[1]], m)
            ret += o
            start = start[0] + m[0], start[1] + m[1]
        return ret

    def out(self, p):
        lenJ = len(self.rgb)
        lenD = len(self.rgb[0])
        return p[0] == lenJ or p[1] == lenD or p[0] < 0 or p[1] < 0

    def turn(self, d, vector):
        if d == "r":
            if vector[0] == 0:
                return vector[1], vector[0]
            else:
                return vector[1], -vector[0]
        if d == "l":
            if vector[0] != 0:
                return vector[1], vector[0]
            else:
                return -vector[1], vector[0]

    def getChars(self, color, m):
        ch = ''
        if color == (255, 0, 0):
            self.test.append("(255, 0, 0)")
            ch = '>'
        elif color == (128, 0, 0):
            self.test.append("(128, 0, 0)")
            ch = '<'
        elif color == (0, 255, 0):
            self.test.append("(0, 255, 0)")
            ch = '+'
        elif color == (0, 128, 0):
            self.test.append("(0, 128, 0)")
            ch = '-'
        elif color == (0, 0, 255):
            self.test.append("(0, 0, 255)")
            ch = '.'
        elif color == (0, 0, 128):
            self.test.append("(0, 0, 128)")
            ch = ','
        elif color == (255, 255, 0):
            self.test.append("(255, 255, 0)")
            ch = '['
        elif color == (128, 128, 0):
            self.test.append("(128, 128, 0)")
            ch = ']'
        elif color == (0, 255, 255):
            self.test.append("(0, 255, 255)")
            m = self.turn("r", m)
        elif color == (0, 128, 128):
            self.test.append("(0, 128, 128)")
            m = self.turn("l", m)
        else:
            self.test.append("(0, 0, 0)")
        return ch, m

if __name__ == "__main__":
    BrainLoller("tests/sachovnice.png")
