import glob, re
from PIL import Image
from pathlib import Path

# Path to your projects home directory
myPath = Path('/Users/michaeldargenio/projects/research')


# The input and output folders
rawFolder = Path(myPath / 'images')
testFolder = Path(myPath / 'test_images')
splitFolder = Path(myPath / 'split_images')

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


# Function to split GSV images down the middle into equal squares (832x832)
def image_split(inputFolder, outputFolder):

    # 'for loop' which iterates over your GSV images folder (testFolder)
    # and then calls the image_splitter function
    for filename in glob.glob('{}{}'.format(inputFolder, '/*.jpg')):
        imageName = re.search(r'test_images\/(.*?)\.jpg', filename).group(1)
        image = Image.open(filename)
        imageLeft = image.crop((0, 0, 832, 832))
        imageRight = image.crop((832, 0, 1664, 832))

        # Crops the image and label whether it is the left or right side
        imageLeft.save('{}/{}{}'.format(outputFolder, imageName,'(left).jpg'))
        imageRight.save('{}/{}{}'.format(outputFolder, imageName,'(right).jpg'))


# Executes both the functions
move_images(rawFolder, testFolder)
image_split(testFolder, splitFolder)