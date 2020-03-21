import os, colorsys
from PIL import Image

class ColorOption:

    imageTagFmt = '<img src="{0}">'
    imageTagFmtClass = '<img class="{classes}" src="{image}">'    
    ColorName = None

    def __init__(self, filePath):
        self.FilePath = filePath
        self.FileName = os.path.split(filePath)[1]
        self.Hue = imageToHue(filePath)

    def __str__(self):
        return self.getColorName() + ' (' + self.FileName + ')'

    def __repr__(self):
        return self.getColorName() + ' (' + str(self.Hue) + ')'

    def __eq__(self, other):
        return self.ColorName == other.ColorName

    def __ne__(self, other):
        return not (self == other)

    def getColorName(self):
        if self.ColorName == None:            
            name_part = self.FileName.split('.')[0]
            self.ColorName = toTitleCase(name_part.split('_'))
            
        return self.ColorName

    def formatToImageTag(self, className=None):
        if (className != None):
            return self.imageTagFmtClass.format(classes=className, image=self.FileName)
        else:
            return self.imageTagFmt.format(self.FileName)
    
    
def imageToHue(filePath: str) -> float:
    img = Image.open(filePath)
    pixels = img.load()
    rgb_val = pixels[1,1]
    hsv_val = colorsys.rgb_to_hsv(rgb_val[0],rgb_val[1],rgb_val[2])
    return hsv_val[0]

def toTitleCase(words: list) -> str:
    out = ''
    if len(words) == 0:
        return out
    
    for word in words:
        firstLetter = word[0]
        remainder = word[1:]
        out = out + ' ' + firstLetter.upper() + remainder
    return out[1:]