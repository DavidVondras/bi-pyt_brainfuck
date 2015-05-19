#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import brainfuck
import brainloller
import braincopter
#import sys


def main(argv=None):
    from optparse import OptionParser
    us = 'usage: %prog [options] FILE'
    hlBrainFuck = 'use the BrainFuck interpreter [default]'
    hlMemory = 'use the BrainFuck interpreter with memory input'
    hlPointer = 'use the BrainFuck interpreter with pointer input'
    parser = OptionParser(usage=us, version="%prog 1.0")
    parser.add_option('-b', '--brainfuck', action='store_true',
                        dest='fuck', help=hlBrainFuck)
    parser.add_option('-l', '--brainloller', action='store_true',
                        dest='loller', help='use the BrainLoller interpreter')
    parser.add_option('-c', '--copter', action='store_true', dest='copter',
                        help='use the BrainCopter interpreter')
    parser.add_option('-m', '--memory', action='store_true', dest='mem',
                        help=hlMemory)
    parser.add_option('-p', '--pointer', action='store_true', dest='pointer',
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
        if options.loller:
            brainloller.BrainLoller(args[0])
        elif options.copter:
            braincopter.BrainCopter(args[0])
        elif options.mem and options.pointer:
            print("---" + args[1] + " " + args[2])
            brainfuck.BrainFuck(args[0])
        else:
            print("bez memory")
            brainfuck.BrainFuck(args[0])

if __name__ == "__main__":
    #print("main")
    main()
