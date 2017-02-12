# -*- coding:utf-8 -*-
# 图片拼接练习
import PIL.Image as Image
import os, sys

mw =51
ms = 50

msize = mw * ms


fpre = "x"
#toImage = Image.new('RGBA', (msize, msize))
toImage = Image.new('RGBA', (2550, 1580))

for y in range(1, 32):
    for x in range(1, 51):
        fname = "x_%s.jpg" % (ms*(y-1)+x)
        
        fromImage = Image.open(fname)
        fromImage =fromImage.resize((50, 50), Image.ANTIALIAS)
        toImage.paste(fromImage, ((x-1) * mw, (y-1) * mw))

toImage.save('/Users/apple/Desktop/wximages/toImage_s10100.jpg')