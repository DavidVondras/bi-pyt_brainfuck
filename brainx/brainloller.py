# -*- coding: utf-8 -*-
import brainfuck


class BrainLoller():

    def getChars(self, color, m):
        o = ''
        if color == (255, 0, 0):
            o = '>'
        if color == (128, 0, 0):
            o = '<'
        if color == (0, 255, 0):
            o = '+'
        if color == (0, 128, 0):
            o = '-'
        if color == (0, 0, 255):
            o = '.'
        if color == (0, 0, 128):
            o = ','
        if color == (255, 255, 0):
            o = '['
        if color == (128, 128, 0):
            o = ']'
        if color == (0, 255, 255):
            m = self._turn(m, "right")
        if color == (0, 128, 128):
            m = self._turn(m, "left")
        return o, m


