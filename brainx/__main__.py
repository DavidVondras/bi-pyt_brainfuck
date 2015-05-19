#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import brainfuck
import brainloller
import braincopter
from binascii import unhexlify
#import sys
from struct import *


def main(argv=None):
    from optparse import OptionParser
    us = 'usage: %prog [options] FILE'
    hlBrainFuck = 'use the BrainFuck interpreter [default]'
    hlMemory = 'use the BrainFuck interpreter with memory input'
    hlPointer = 'use the BrainFuck interpreter with pointer input'
    pointH = '--memory-pointer'
    parser = OptionParser(usage=us, version="%prog 1.0")
    parser.add_option('-f', '--brainfuck', action='store_true',
                        dest='fuck', help=hlBrainFuck)
    parser.add_option('-l', '--brainloller', action='store_true',
                        dest='loller', help='use the BrainLoller interpreter')
    parser.add_option('-c', '--copter', action='store_true', dest='copter',
                        help='use the BrainCopter interpreter')
    parser.add_option('-m', '--memory', action='store_true', dest='mem',
                        help=hlMemory)
    parser.add_option('-p', pointH, action='store_true', dest='pointer',
                        help=hlPointer)
    parser.add_option('-t', '--test', action='store_true', dest='test',
                        help=hlPointer)
    (options, args) = parser.parse_args()
    opt = 'options --brainfuck, --brainloller'
    opt += 'and --braincopter are mutually exclusive'
    opt2 = 'options --brainloller and --braincopter are mutually exclusive'
    opt3 = 'options --brainfuck and --brainloller are mutually exclusive'
    opt4 = 'options --brainfuck and --braincopter are mutually exclusive'
    if len(args) < 1:
        #parser.error('to few arguments')
        inputCode = input("Enter BrainFuck code: ")
        print(inputCode)
        brainfuck.BrainFuck(inputCode)
    else:
        if options.fuck and options.copter and options.loller:
            parser.error(opt)
        if options.loller and options.copter:
            parser.error(opt2)
        if options.fuck and options.loller:
            parser.error(opt3)
        if options.fuck and options.copter:
            parser.error(opt4)
        if options.loller or ".png" in args[0]:
            brainloller.BrainLoller(args[0])
        elif options.copter:
            braincopter.BrainCopter(args[0])
        elif options.mem and options.pointer:
            #print(type(args[1]))
            #print(type(bytearray(args[1], "utf8")))
            #print("---" + args[1] + " " + args[2])
            brainfuck.BrainFuck(args[0], bytes(args[1], "utf8"), args[2])
        elif options.mem:
            bb = args[1]
            print(bb)
            bb = bb.replace("b'", "")
            bb = bb.replace("'", "")
            bb = bb.replace("\\x", "")
            q = unhexlify(bb)
            brainfuck.BrainFuck(args[0], q)
        elif options.test:
            brainfuck.BrainFuck(args[0], b'\x00', 0, 1)
        else:
            print("bez memory")
            brainfuck.BrainFuck(args[0])

if __name__ == "__main__":
    #print("main")
    main()
