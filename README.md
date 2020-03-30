# GSV-Image-Prep
> Running the im_config python script will take a given number (100) of GSV images and split the images into two equal squares of 832x832 pixels. Differentiating the images with a 'right' or 'left' label appended to the original image name. This can be used to prepare a training dataset or as a preprocessing step for a models data pipeline.

## Prerequisites
 - [Python >=3.5](https://www.python.org/downloads/)
 - [Pillow](https://pillow.readthedocs.io/en/stable/installation.html#basic-installation)
## Recommended
 - [Anaconda](https://docs.anaconda.com/anaconda/install/)

## Step-by-step Instructions

1. Install Python (and Anaconda)
2. Create a new directory and environment
3. Install Pillow and Pathlib using pip: `pip install pillow pathlib`
4. Clone the repository to your local directory
5. Configure the file with your correct folder and path locations
6. Run the file using: `python im_config.py`
