import os, random, helpers
import genanki as genki
from ColorOption import ColorOption


colorFilesPath = r'C:\Users\jgsch\Desktop\Development\Color Code Anki\color_imgs'
outputPath = r'C:\Users\jgsch\Desktop\Development\Color Code Anki\output.apkg'

# Get list of available colors
color_images = os.listdir(colorFilesPath)

colorOptions = []
for colorImg in color_images:
    colorImgPath = os.path.join(colorFilesPath, colorImg)

    colorOption = ColorOption(colorImgPath)    
    colorOptions.append(colorOption)

# shuffle colors
random.shuffle(colorOptions)
random.shuffle(colorOptions)
random.shuffle(colorOptions)

# keep a sorted list
sortedColorOptions = sorted(colorOptions, key=lambda x: x.Hue)



#print(sorted(colorOptions, key=lambda x: x.Hue))
# Build deck!
colorImage_fld = 'Color Image'
colorImages_fld = 'Color Images'
colorName_fld = 'Color Name'
colorParts_fld = 'Color Parts'

deck_id = random.randrange(1 << 30, 1 << 31)
my_deck = genki.Deck(
    deck_id,
    'CSS Colors'
)

#-------------------------------------------------------------
# Color :: Word
color_word_id = random.randrange(1 << 30, 1 << 31)
color_word_styling = """
.color{
  background: #808080;
  padding: 10px;
}

.name {
  text-align: center;
  font-size: 2em;
  padding: 10px;
}

.parts{
  text-align: center;
}

img{
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 40%;
}
"""

color_word = genki.Model(
    color_word_id,
    'Color :: Word',
    fields=[
        { 'name': colorImage_fld },
        { 'name': colorName_fld },
        { 'name': colorParts_fld },
    ],
    templates=[
        {
            'name': 'Main',
            'qfmt': '<div class="color">{{' + colorImage_fld + '}} </div>',
            'afmt': '{{FrontSide}} <hr id="answer" /> <div class="name"> {{' + colorName_fld + '}} </div>' +
                    '<br /> <div class="parts"> {{' + colorParts_fld + '}} </div>'
        }
    ],
    css=color_word_styling
    )

for colorOption in colorOptions:
    note = genki.Note(
        model=color_word,
        fields=[
            colorOption.formatToImageTag(),
            colorOption.ColorName,
            colorOption.formatToCmykValues(),
        ])

    my_deck.add_note(note)

#-------------------------------------------------------------
# Word with varied options :: Color
word_with_varied_id = random.randrange(1 << 30, 1 << 31)
word_with_varied_styling = """
.color{
  background: #808080;
  padding: 10px;
}

.name {
  text-align: center;
  font-size: 2em;
  padding: 10px;
}

.parts{
  text-align: center;
}

img.multiple{
  display: inline;
  margin-left: auto;
  margin-right: auto;
  width: 20%;
}

img{
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 40%;
}
"""

word_with_varied = genki.Model(
    word_with_varied_id,
    'Color (varied options) :: Word',
    fields=[
        {'name': colorName_fld},
        {'name': colorImages_fld},
        {'name': colorImage_fld},
        {'name': colorParts_fld},
    ],
    templates=[
        {
            'name': 'Main',
            'qfmt': '<div class="name"> {{' + colorName_fld + '}} </div>' +
                    '\n<div class="color">{{' + colorImages_fld + '}}</div>',
            'afmt': '<div class="name"> {{' + colorName_fld + '}} </div>' +
                    '<hr id="answer" />' + 
                    '<div class="color">{{' + colorImage_fld + '}}</div>' +
                    '<br /> <div class="parts"> {{' + colorParts_fld + '}} </div>',
        }
    ],
    css=word_with_varied_styling
    )

for colorOption in colorOptions:
    options = helpers.getFiveRandom(colorOption, colorOptions)
    tags = ''.join([ x.formatToImageTag('multiple') for x in options ])
    note = genki.Note(
        model=word_with_varied,
        fields=[
            colorOption.ColorName,
            tags,
            colorOption.formatToImageTag(),
            colorOption.formatToCmykValues(),
        ])

    my_deck.add_note(note)

#-------------------------------------------------------------
# Word with similar color options :: Color
word_with_similar_id = random.randrange(1 << 30, 1 << 31)
word_with_similar_styling = """
.color{
  background: #808080;
  padding: 10px;
}

.name {
  text-align: center;
  font-size: 2em;
  padding: 10px;
}

.parts{
  text-align: center;
}

img.multiple{
  display: inline;
  margin-left: auto;
  margin-right: auto;
  width: 33%;
}

img{
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 40%;
}
"""

word_with_similar = genki.Model(
    word_with_similar_id,
    'Color (similar options) :: Word',
    fields=[
        {'name': colorName_fld},
        {'name': colorImages_fld},
        {'name': colorImage_fld},
        {'name': colorParts_fld},
    ],
    templates=[
        {
            'name': 'Main',
            'qfmt': '<div class="name"> {{' + colorName_fld + '}} </div>' +
                    '\n<div class="color">{{' + colorImages_fld + '}}</div>',
            'afmt': '<div class="name"> {{' + colorName_fld + '}} </div>' +
                    '<hr id="answer" />' + 
                    '<div class="color">{{' + colorImage_fld + '}}</div>' +
                    '<br /> <div class="parts"> {{' + colorParts_fld + '}} </div>',
        }
    ],
    css=word_with_similar_styling
    )

for colorOption in colorOptions:
    # create 3 cards for each, left-middle-center variaties
    for i in range(3):
        options = helpers.getThree(colorOption, sortedColorOptions, i)
        if options == None:
            continue
        tags = ''.join([ x.formatToImageTag('multiple') for x in options ])
        note = genki.Note(
            model=word_with_similar,
            fields=[
                colorOption.ColorName,
                tags,
                colorOption.formatToImageTag(),
                colorOption.formatToCmykValues(),
            ])

        my_deck.add_note(note)

#-------------------------------------------------------------
# Word with no color options :: Color
word_color_id = random.randrange(1 << 30, 1 << 31)
# word_color_styling - same styling can be applied

word_color = genki.Model(
    word_color_id,
    'Word :: Color',
    fields=[
        {'name': colorName_fld},
        {'name': colorImage_fld},
        {'name': colorParts_fld},
    ],
    templates=[
        {
            'name': 'Main',
            'qfmt': '<div class="name"> {{' + colorName_fld + '}} </div>',
            'afmt': '{{FrontSide}} <hr id="answer" /> <div class="color">{{' + colorImage_fld + '}} </div>' +
                    '<br /> <div class="parts"> {{' + colorParts_fld + '}} </div>',
        }
    ],
    css=color_word_styling
    )

for colorOption in colorOptions:
    note = genki.Note(
        model=word_color,
        fields=[
            colorOption.ColorName,
            colorOption.formatToImageTag(),
            colorOption.formatToCmykValues(),
        ])

    my_deck.add_note(note)

#-------------------------------------------------------------
# Package
colorPaths = []
for colorOption in colorOptions:
    colorPaths.append(colorOption.FilePath)

my_package = genki.Package(my_deck)
my_package.media_files = colorPaths
my_package.write_to_file(outputPath)


