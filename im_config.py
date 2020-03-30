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
            image = Image.open(filename)
            imageLeft = image.crop((0, 0, 832, 832))
            imageRight = image.crop((832, 0, 1664, 832))

            imageLeft.save('{}/{}{}{}'.format(train, 'Image-', i+1,'(left).jpg'))
            imageRight.save('{}/{}{}{}'.format(train, 'Image-', i+1, '(right).jpg'))
        elif i < 85:
            image = Image.open(filename)
            imageLeft = image.crop((0, 0, 832, 832))
            imageRight = image.crop((832, 0, 1664, 832))

            imageLeft.save('{}/{}{}{}'.format(test, 'Image-', i+1,'(left).jpg'))
            imageRight.save('{}/{}{}{}'.format(test, 'Image-', i+1, '(right).jpg'))
        elif i < 100:
            image = Image.open(filename)
            imageLeft = image.crop((0, 0, 832, 832))
            imageRight = image.crop((832, 0, 1664, 832))

            imageLeft.save('{}/{}{}{}'.format(validate, 'Image-', i+1,'(left).jpg'))
            imageRight.save('{}/{}{}{}'.format(validate, 'Image-', i+1, '(right).jpg'))
        else:
            break

# Executes both the functions
move_images(rawFolder, trainFolder, testFolder, validateFolder)