import glob, re
from PIL import Image
from pathlib import Path

# Path to your projects home directory
myPath = Path('/Users/michaeldargenio/projects/research')


# The input and output folders
inputFolder = Path(myPath / 'test_images')
outputFolder = Path(myPath / 'split_images')


# Function to split GSV images down the middle into equal squares (832x832)
def image_split(image):
    imgLeft = image.crop((0, 0, 832, 832))
    imgRight = image.crop((832, 0, 1664, 832))

    # Crops the image and label whether it is the left or right side
    imgLeft.save('{}/{}{}'.format(outputFolder, imgName,'(left).jpg'))
    imgRight.save('{}/{}{}'.format(outputFolder, imgName,'(right).jpg'))


# 'for loop' which iterates over your GSV images folder (inputFolder)
# and then calls the image_splitter function
for filename in glob.glob('{}{}'.format(inputFolder, '/*.jpg')):
    imgName = re.search(r'test_images\/(.*?)\.jpg', filename).group(1)
    img = Image.open(filename)

    # Executes the image_split function for each iteration
    image_split(img)