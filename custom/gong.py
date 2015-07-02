#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys

def main(args):
    # rage magic word
    if random.randint(1, 100) == 100:
       print "不要像「小孩子要糖果」似的，什麼都喊要，而且越多越好。一下子得不到想要的也不要疑神疑鬼。"
       return 0

    if args.__len__() == 0:
       return 0

    # magic word
    magic_word = args[random.randint(0, args.__len__() - 1)]   
    if magic_word == "sf":
        print "巴黎有華貴的內飾，舊金山有海景，是一種比法；"
    elif magic_word == "paris":
        print "巴黎有華貴的內飾，舊金山有海景，是一種比法；"
    else:
        print "同一家公司，不同地域，可比性不強。"

if __name__ == '__main__':
    main(sys.argv[1:])
