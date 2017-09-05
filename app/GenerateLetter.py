# coding=utf-8
import os
from time import sleep
import string
import random
import re
import csv
from PIL import Image, ImageDraw, ImageFont

fg  = (0, 0, 0)
white  = (255, 255, 255)
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

fontPath = PATH('../font/aescrawl.ttf') # 本地字体文件
fontSize = 12

upperLetterRandom  = chr(random.randint(65,90))
lowerLetterRandom = chr(random.randint(97,122))

def generateLettersArray():
    # 随机生成一批单词
    letterArr = []
    for i in range(10):
        # 构造单词
        letter = chr(random.randint(65,90))
        letterNumber = random.randint(2,7)
        for i in range(0,letterNumber):
            letter += chr(random.randint(65,90)) if letterNumber%2 == 0 else chr(random.randint(97,122))
        print letter
        letterArr.append(letter)
    return letterArr

# 单词保存到一张图片中
def drawText(txt, font, pos=(0, 0), fill=fg, bg=white):
    """
    绘制txt文本
    :param txt:
    :param pos:
    :param fill:
    :param bg: 背景色
    :return:
    """
    txt_size = font.getsize(txt)
    image = Image.new('RGBA', (txt_size[0] + pos[0] + random.randint(0, 30),
                               txt_size[1] + pos[1] + random.randint(0, 20)),
                           bg)
    draw = ImageDraw.Draw(image)
    draw.text(pos, txt, font=font, fill=fill)
    rotate = image.rotate(random.randint(-3, 3), expand=1)
    image.paste(rotate, (0, 0), rotate)
    image = image.point(lambda i: add_noise(i))
    del draw
    return image

def add_noise(i):
    i = i + random.randint(-10, 10)
    if i < 0:
        i = 0
    elif i > 255:
        i = 255
    return i

def saveToCsv(letterArr):

    if not os.path.exists('../letterCsv'):
        os.mkdir("../letterCsv")
    if not os.path.exists('../image'):
        os.mkdir("../image")
    csvFile = open('../letterCsv/letter.csv',"w")
    #文件头
    fileHeader = ["path","content"]

    writer = csv.writer(csvFile)
    writer.writerow(fileHeader)
    for index,value in enumerate(letterArr):
        image = drawText(value,ImageFont.truetype(fontPath, fontSize),(0,0),fg ,white )
        imageFileName =  value+'.png'
        image.save(PATH('../image/' + imageFileName))
        d1 = [PATH('../image/' + imageFileName), imageFileName]
        writer.writerow(d1)      # 写入数据
    csvFile.close()


def operation():
    letterArr = generateLettersArray()
    saveToCsv(letterArr)

 
operation()
