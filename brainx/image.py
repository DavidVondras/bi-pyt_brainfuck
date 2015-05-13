#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class PNGWrongHeaderError(Exception):
    pass


class ImagePng():

    def __init__(self, filename):
        fileImage = open(filename, mode='rb')
        self.imageValues = fileImage.read()
        if (self.binary[:8] != b'\x89PNG\r\n\x1a\n'):
            raise PNGWrongHeaderError()
        self.imageValues = self.imageValues[8:]
        self.data = []
        p = 0
        while p < len(self.imageValues):
            l = self.getBytes(self.imageValues[p:p + 4])
            p += 4
            self.data += [{'head':self.imageValues[p:p + 4], 'data':self.imageValues[p + 4:p + l + 4]}]
            p += (l + 8)
