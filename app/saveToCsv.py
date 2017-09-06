# coding=utf-8
import csv
import config
from PIL import Image, ImageDraw, ImageFont
import random
from saveTxtToImage import *

# 保存单词信息到csv文件类
class saveToCsv:

    def saveImageInfoToCsv(self,path,letterArr): # 参数为csv的路径/字母数组

        csvFile = open(path,"w")
        writer = csv.writer(csvFile)
        writer.writerow(config.fileHeader)
        saveTxtToImageObject = saveTxtToImage()

        for index,value in enumerate(letterArr):
            randomFont = config.fontPath[random.randint(0,1)]
            image = saveTxtToImageObject.drawText(value,ImageFont.truetype(randomFont, config.fontSize),(0,0),config.fg ,config.randomColor)
            rgb_im = image.convert('RGB')
            imageFileName = value +'.jpg'
            rgb_im.save(config.imagePath(imageFileName),quality=95)
            dataWriteIntoImage = [config.imagePath(imageFileName), imageFileName]
            writer.writerow(dataWriteIntoImage)      # 写入数据

        csvFile.close()
