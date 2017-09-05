# coding=utf-8
import os
from generateLetter  import  *
from saveToCsv import *
import config

class operation:
    def operateImage(self):
        lettersObject = generateLetter()
        lettersArray = lettersObject.generateLettersArray()
        #print(lettersArray )
        saveToCsvObject = saveToCsv()
        saveToCsvObject.saveImageInfoToCsv(config.csvPath,lettersArray)
         

operateObject = operation()
operateObject.operateImage()
