import glob, re
from PIL import Image
from pathlib import Path

# Path to your projects home directory
myPath = Path('/Users/michaeldargenio/projects/research')

# The input and output folders
rawFolder = Path(myPath / 'images')
trainFolder = Path(myPath / 'train')
testFolder = Path(myPath / 'test')
validateFolder = Path(myPath / 'validate')

# Function to move and rename images from one folder to another
def move_images(inputFolder, train, test, validate):

    # 'for loop' which iterates over your GSV images folder (inputFolder)
    for (i, filename) in enumerate(glob.glob('{}{}'.format(inputFolder, '/*.jpg'))):
        
        # This takes only 100 of the images to be used for your training set
        if i < 70:
            im_split(filename, train, i+1)
        elif i < 85:
            im_split(filename, test, i+1)
        elif i < 100:
            im_split(filename, validate, i+1)
        else:
            break

def im_split(filename, destination, n):
    image = Image.open(filename)
    imageLeft = image.crop((0, 0, 832, 832))
    imageRight = image.crop((832, 0, 1664, 832))

    imageLeft.save('{}/{}{}{}'.format(destination, 'Image-', n,'(left).jpg'))
    imageRight.save('{}/{}{}{}'.format(destination, 'Image-', n, '(right).jpg'))

# Executes both the functions
move_images(rawFolder, trainFolder, testFolder, validateFolder)