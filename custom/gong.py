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
        print "巴 黎 有 華 貴 的 內 飾 ， 舊 金 山 有 海 景 ， 是 一 種 比 法；"
    elif magic_word == "tp" or magic_word == "bj":
        print "於 北 京 辦 公 室 比 ， 那 邊 既 沒 有 臺 北 辦 公 室 現 有 的 咖 啡 機 ， 也 沒 有 附 近 的 美 食 ， 更 沒 有 同 樣 質 量 的 空 氣 ， 又 是 另 一 種 比 法。"    
    else:
        rand_list = ["公司不是盲流組織，不是mob rule。若是只有在mob rule環境下才能生存，若是認為上班就是搞民主運動，不僅政治上幼稚，工作上也幼稚。",
                     "同一家公司，不同地域，可比性不強。",
                     "誰也不會吃飽了撐的跑到信義計劃區辦「血汗工廠」。"]
        print rand_list[random.randint(0, rand_list.__len__() - 1)]

if __name__ == '__main__':
    main(sys.argv[1:])
