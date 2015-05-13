#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ImagePng():

    def __init__(self, filename):
        fileImage = open(filename, mode='rb')
        self.imageValues = fileImage.read()
        
        