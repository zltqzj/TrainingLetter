# coding=utf-8
import csv
import config
from PIL import Image, ImageDraw, ImageFont
import random

# 把文字变为图片类
class saveTxtToImage:

    def add_noise(self,i):
        i = i + random.randint(-10, 10)
        if i < 0:
            i = 0
        elif i > 255:
            i = 255
        return i

    def drawText(self,txt, font, pos=(0, 0), fill=config.fg, bg=config.white):
        txt_size = font.getsize(txt)

        maxWidth = maxHeight = 100
        minWidth = minHeight = 10

        randomColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
         
        image = Image.new('RGBA', (txt_size[0] + pos[0] + random.randint(0, maxWidth) + maxWidth,
                                   txt_size[1] + pos[1] + random.randint(0, maxHeight) +maxHeight + txt_size[0]),
                               (randomColor))
        draw = ImageDraw.Draw(image)
        draw.text((random.randint(minHeight, maxWidth),random.randint(minHeight, maxHeight)), txt, font=font, fill=fill)
        rotate = image.rotate(random.randint(-10, 10), expand=1)
        image.paste(rotate, (0, 0), rotate)
        image = image.point(lambda i: self.add_noise(i))
        del draw
        return image
