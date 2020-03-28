import glob, re
from PIL import Image
from pathlib import Path

# Path to your projects home directory
myPath = Path('/Users/michaeldargenio/projects/research')


# The input and output folders
inputFolder = Path(myPath / 'images')
outputFolder = Path(myPath / 'test_images')


# Function to move and rename images from one folder to another
def move_images(inputFolder, outputFolder):

    # 'for loop' which iterates over your GSV images folder (inputFolder)
    for (i, filename) in enumerate(glob.glob('{}{}'.format(inputFolder, '/*.jpg'))):
        
        # This takes only 100 of the images to be used for your training set
        if i < 100:
            img = Image.open(filename)
            img.save('{}/{}{}{}'.format(outputFolder, 'Image-', i+1, '.jpg'))
        else:
            break


# Executes the move_images function
move_images(inputFolder, outputFolder)