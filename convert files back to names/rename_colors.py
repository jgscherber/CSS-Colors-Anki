import json, os, shutil

filePath = r'C:\Users\jgsch\Desktop\Development\Color Code Anki\convert files back to names\media.json'
fd = open(filePath)
# treats JSON objects as dicts and lists and lists - easy
colorMapping = json.loads(fd.read())

originalsFolderPath = r'C:\Users\jgsch\Desktop\Development\Color Code Anki\convert files back to names\originals'
finalFolderPath = r'C:\Users\jgsch\Desktop\Development\Color Code Anki\color_imgs'

colorFolder = os.listdir(originalsFolderPath)

for unnamed in colorFolder:
    currentPath = os.path.join(originalsFolderPath, unnamed)
    realFileName = colorMapping[unnamed].lower()
    destPath = os.path.join(finalFolderPath, realFileName)
    shutil.copyfile(currentPath, destPath)