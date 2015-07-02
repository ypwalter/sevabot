#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys

def main(args):
    # rage magic word
    if random.randint(1, 100) >= 90:
       print "不要像「小孩子要糖果」似的，什麼都喊要，而且越多越好。一下子得不到想要的也不要疑神疑鬼。"
       return 0

    # magic word
    if args.__len__() != 0:
       magic_word = args[random.randint(0, args.__len__() - 1)]   
    else:
       magic_word = ""

    if magic_word == "sf" or magic_word == "paris":
        print "巴黎有華貴的內飾，舊金山有海景，是一種比法；"
    elif magic_word == "tp" or magic_word == "bj":
        print "於北京辦公室比，那邊既沒有臺北辦公室現有的咖啡機，也沒有附近的美食，更沒有同樣質量的空氣，又是另一種比法。"    
    else:
        rand_list = ["公司不是盲流組織，不是mob rule。若是只有在mob rule環境下才能生存，若是認為上班就是搞民主運動，不僅政治上幼稚，工作上也幼稚。",
                     "同一家公司，不同地域，可比性不強。",
                     "誰也不會吃飽了撐的跑到信義計劃區辦「血汗工廠」。"]
        print rand_list[random.randint(0, rand_list.__len__() - 1)]

if __name__ == '__main__':
    main(sys.argv[1:])
