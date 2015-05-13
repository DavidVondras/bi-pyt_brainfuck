# -*- coding: utf-8 -*-

import image


class BrainLoller():
    def __init__(self, filename):
        self.data = self.getBrainLoller(filename)

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

    def getChars(self, color, m):
        ch = ''
        if color == (255, 0, 0):
            ch = '>'
        if color == (128, 0, 0):
            ch = '<'
        if color == (0, 255, 0):
            ch = '+'
        if color == (0, 128, 0):
            ch = '-'
        if color == (0, 0, 255):
            ch = '.'
        if color == (0, 0, 128):
            ch = ','
        if color == (255, 255, 0):
            ch = '['
        if color == (128, 128, 0):
            ch = ']'
        if color == (0, 255, 255):
            m = self._turn(m, "right")
        if color == (0, 128, 128):
            m = self._turn(m, "left")
        return ch, m

if __name__ == "__main__":
    BrainLoller("../tests/HelloWord.png")
