
# coding=utf-8

import os
from time import sleep
import string
import random
import re

# 前景色
fg  = (0, 0, 0)

# 随机背景色
white  = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# 路径
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

# 本地字体文件路径
fontPath = PATH('../font/Afromatic.ttf')
# 字体大小
fontSize = 14

# 生成图片后的路径
imagePath = lambda imageName : PATH('../image/' + imageName)

# 本地csv路径
csvPath = '../letterCsv/letter.csv'

#文件头
fileHeader =  ["path","content"]

# 随机颜色数值
randomColorNumber = random.randint(0,255)

# 随机颜色
randomColor = (randomColorNumber,randomColorNumber,randomColorNumber)

# 生成x个单词
wordNumber = 10
