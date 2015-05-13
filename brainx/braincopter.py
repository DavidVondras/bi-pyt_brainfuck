# -*- coding: utf-8 -*-
import image
import brainfuck


class BrainCopter():
    def __init__(self, filename):
        self.data = self.getBrainLoller(filename)
        brainfuck.BrainFuck(self.data)

    def readImage(self, filename):
        self.rgb = image.ImagePng(filename).rgb

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
        return p[0] == len(self.rgb) or p[1] == len(self.rgb[0]) or p[0] < 0 or p[1] < 0

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
        
        return ch, m

if __name__ == "__main__":
    BrainCopter("../tests/HelloWorld.png")