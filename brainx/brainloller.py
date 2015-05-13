# -*- coding: utf-8 -*-

import image


class BrainLoller():
    def __init__(self, filename):
        self.data = getBrainLoller(filename)
        
    def readImage(self, filename):
        self.rgb = image.ImagePng(filename).rgb

    def getBrainLoller(self, filename):
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
    def 

if __name__ == "__main__":
    BrainLoller.readImage("../tests/HelloWord.png")
