#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zlib


class PNGWrongHeaderError(Exception):
    pass


class PNGNotImplementedError(Exception):
    pass


class ImagePng():
    def getBytes(self, bytes):
        n = 0
        for b in bytes:
            n = n * 256 + b
        return n

    def get(self, left, up, ul):
        res = tuple()
        for i in range(0, 3):
            p = (left[i] + up[i] - ul[i])
            pl = abs(p - left[i])
            pu = abs(p - up[i])
            pul = abs(p - ul[i])

            if (pl <= pu and pl <= pul):
                res += (left[i],)
            elif (pu <= pul):
                res += (up[i],)
            else:
                res += (ul[i],)
        return res

    def pixelTG(self, a, res):

        x = (a[0] + res[0]) % 256
        z = (a[1] + res[1]) % 256
        y = (a[2] + res[2]) % 256
        return (x, z, y)

    def __init__(self, filename):
        fileImage = open(filename, mode='rb')
        self.imageValues = fileImage.read()
        if (self.imageValues[:8] != b'\x89PNG\r\n\x1a\n'):
            raise PNGWrongHeaderError()
        self.imageValues = self.imageValues[8:]
        self.data = []
        p = 0
        while p < len(self.imageValues):
            l = self.getBytes(self.imageValues[p:p + 4])
            p += 4
            self.data += [{'head':self.imageValues[p:p + 4], 'data':self.imageValues[p + 4:p + l + 4]}]
            p += (l + 8)
        for c in self.data:
            if (c['head'] == b'IHDR'):
                ihdr = c['data']
                break
        self.width = self.getBytes(ihdr[0:4])
        self.height = self.getBytes(ihdr[4:8])
        if self.getBytes(ihdr[8:9]) != 8 \
        or self.getBytes(ihdr[9:10]) != 2 \
        or self.getBytes(ihdr[10:11]) != 0 \
        or self.getBytes(ihdr[11:12]) != 0 \
        or self.getBytes(ihdr[12:13]) != 0:
            raise PNGNotImplementedError()
        idat = b''
        for c in self.data:
            if (c['head'] == b'IDAT'):
                idat += c['data']

        idat = zlib.decompress(idat)
        self.rgb = []
        p = 0
        for row in range(0, self.height):
            pngF = idat[p]
            p += 1
            line = []
            left = (0, 0, 0)
            upleft = (0, 0, 0)
            for c in range(0, self.width):
                pi = (idat[p], idat[p + 1], idat[p + 2])
                p += 3
                if (pngF == 0):
                    left = pi
                    line += [pi]
                elif (pngF == 1):
                    left = self.pixelTG(left, pi)
                    line += [left]
                elif (pngF == 2):
                    left = self.pixelTG(pi, self.rgb[len(self.rgb) - 1][c])
                    line += [left]

                elif (pngF == 4):
                    up = self.rgb[len(self.rgb) - 1][c]
                    current = self.pixelTG(pi, self.get(left, up, upleft))
                    line += [current]
                    left = current
                    upleft = up
            self.rgb += [line]