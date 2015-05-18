#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import brainfuck as brfuck
import brainloller as br
import sys


def main(argv=None):
    from optparse import OptionParser
    us = 'usage: %prog [options] FILE'
    hlBrainFuck = 'use the BrainFuck interpreter [default]'
    parser = OptionParser(usage=us, version="%prog 1.0")
    parser.add_option('-b', '--brainfuck', action='store_true',
                        dest='fuck', help=hlBrainFuck)
    parser.add_option('-l', '--brainloller', action='store_true',
                        dest='loller', help='use the BrainLoller interpreter')
    parser.add_option('-c', '--copter', action='store_true', dest='copter',
                        help='use the BrainCopter interpreter')
    (options, args) = parser.parse_args()
    if len(args) < 1:
        parser.error('to few arguments')
if __name__ == "__main__":
    print("main")
    sys.exit(main())
