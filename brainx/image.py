#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zlib


class PNGWrongHeaderError(Exception):
    pass


class PNGNotImplementedError(Exception):
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
        for c in self.data:
            if (c['head'] == b'IHDR'):
                ihdr = c['data']
                break
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