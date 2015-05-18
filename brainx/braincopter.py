# -*- coding: utf-8 -*-
import image
import brainfuck


class BrainCopter():
    def __init__(self, filename):
        rgb = image.ImagePng(filename).rgb
        ptr = (0, 0)
        w = 0
        self.data = ''

        cislo = 0
        while True:
            x = ptr[0]
            y = ptr[1]
            print(str(x) + ">=" + str(len(rgb)) + " or " + str(x) +"<0 or " + str(y) + ">=" + str(len(rgb[0])))
            if x >= len(rgb) or x < 0 or y >= len(rgb[0]) or y < 0:
                break
            px = rgb[ptr[0]][ptr[1]]
            c = (-2 * px[0] + 3 * px[1] + px[2]) % 11
            cislo += 1
            if c == 0:
                self.data += '>'
            elif c == 1:
                self.data += '<'
            elif c == 2:
                self.data += '+'
            elif c == 3:
                self.data += '-'
            elif c == 4:
                self.data += '.'
            elif c == 5:
                self.data += ','
            elif c == 6:
                self.data += '['
            elif c == 7:
                self.data += ']'
            elif c == 8:
                w += 1
                w %= 4
            elif c == 9:
                w -= 1
                w %= 4
            if w == 0:
                ptr = ptr[0], ptr[1] + 1
            elif w == 1:
                ptr = ptr[0] + 1, ptr[1]
            elif w == 2:
                ptr = ptr[0], ptr[1] - 1
            else:
                ptr = ptr[0] - 1, ptr[1]
        brainfuck.BrainFuck(self.data)
if __name__ == "__main__":
    BrainCopter("../tests/lk.png")