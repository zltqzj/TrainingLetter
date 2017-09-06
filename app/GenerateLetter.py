# coding=utf-8
import os
import string
import random

from PIL import Image, ImageDraw, ImageFont
import config

# 生成一组单词类
class generateLetter:

    def randomUpperLetter(self):
        letter = chr(random.randint(65,90))
        return letter

    def randomLowerLetter(self):
        letter = chr(random.randint(97,122))
        return letter

    def randomNumber(self):
        number  = config.random.randint(2,7)
        return number

    def generateLettersArray(self):
        # 随机生成一批单词
        letterArr = []
        for i in range(config.wordNumber):
            # 构造单词
            letter = self.randomUpperLetter()
            letterNumber = self.randomNumber()
            for i in range(0,letterNumber):
                letter += self.randomUpperLetter() if letterNumber%2 == 0 else self.randomLowerLetter()
            #print letter
            letterArr.append(letter)
        return letterArr
