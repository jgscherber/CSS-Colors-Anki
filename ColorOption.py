import os, colorsys
from PIL import Image

class ColorOption:

    imageTagFmt = '<img src="{0}">'
    imageTagFmtClass = '<img class="{classes}" src="{image}">'    
    ColorName = None

    # Color Values
    Hue = 0
    Red = 0
    Green = 0
    Blue = 0

    def __init__(self, filePath):
        self.FilePath = filePath
        self.FileName = os.path.split(filePath)[1]
        self.__setColors__()
        self.__setColorName__()

    def __str__(self):
        return self.ColorName + ' (' + self.FileName + ')'

    def __repr__(self):
        return self.ColorName + ' (' + str(self.Hue) + ')'

    def __eq__(self, other):
        return self.ColorName == other.ColorName

    def __ne__(self, other):
        return not (self == other)

    def __setColors__(self):
        img = Image.open(self.FilePath)
        pixels = img.load()
        rgb_val = pixels[1,1]
        self.Red = rgb_val[0]
        self.Green = rgb_val[1]
        self.Blue = rgb_val[2]
        self.Hue = colorsys.rgb_to_hsv(self.Red, self.Green, self.Blue)[0]         

    def __setColorName__(self):
        name_part = self.FileName.split('.')[0]
        self.ColorName = toTitleCase(name_part.split('_'))
            
        return self.ColorName

    def formatToImageTag(self, className=None):
        if (className != None):
            return self.imageTagFmtClass.format(classes=className, image=self.FileName)
        else:
            return self.imageTagFmt.format(self.FileName)

    def formatToCmykValues(self):
        cmyk_val = rgb_to_cmyk(self.Red, self.Green, self.Blue)
        return 'Cyan: {0:.1f} Magenta: {1:.1f} Yellow: {2:.1f} Black: {3:.1f}' \
                .format(cmyk_val[0], cmyk_val[1], cmyk_val[2], cmyk_val[3])


RGB_SCALE = 255
CMYK_SCALE = 100


def rgb_to_cmyk(r, g, b):
    if (r, g, b) == (0, 0, 0):
        # black
        return 0, 0, 0, CMYK_SCALE

    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / RGB_SCALE
    m = 1 - g / RGB_SCALE
    y = 1 - b / RGB_SCALE

    # extract out k [0, 1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy

    # rescale to the range [0,CMYK_SCALE]
    return c * CMYK_SCALE, m * CMYK_SCALE, y * CMYK_SCALE, k * CMYK_SCALE

def toTitleCase(words: list) -> str:
    out = ''
    if len(words) == 0:
        return out
    
    for word in words:
        firstLetter = word[0]
        remainder = word[1:]
        out = out + ' ' + firstLetter.upper() + remainder
    return out[1:]