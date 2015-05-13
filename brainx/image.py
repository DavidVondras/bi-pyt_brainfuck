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
        