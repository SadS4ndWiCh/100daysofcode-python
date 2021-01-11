import sys
import re
import imageio
from pathlib import Path
from typing import List

GIF_DEFAULT_DURATION = 0.5
GIF_DEFAULT_NAME = 'output.gif'
VALIDS_IMAGES_EXTENSIONS = ('.jpg', '.png')
RE_VALID_IMAGE_NAME = re.compile(r'^[0-9]+\.(?:jpg|png)$')

def getImagesFromPath(dirPath: str):
    path = Path(dirPath)
    return [file.absolute() for file in sorted(path.iterdir(), key=lambda i: i.name) if isValidFile(file)]

def isValidFile(filePath: str):
    path = Path(filePath)
    return path.is_file() and path.suffix in VALIDS_IMAGES_EXTENSIONS and bool(RE_VALID_IMAGE_NAME.match(path.name))

def convertToGif(filenames: List[str], *, duration: float = GIF_DEFAULT_DURATION, outPath: str = '.', gifName: str = GIF_DEFAULT_NAME):
    images = [imageio.imread(filename) for filename in filenames]
    finalDirectory = Path(outPath).joinpath(gifName)

    imageio.mimsave(finalDirectory, images, duration=duration)

if(__name__ == '__main__'):
    script = sys.argv.pop(0)
    args = sys.argv

    filenames = None

    if(len(args) == 0):
        print(f'Usage: {script} <images directory>')
        sys.exit()

    elif(len(args) == 1):
        filenames = getImagesFromPath(args[0])

    if(all([not file.suffix in VALIDS_IMAGES_EXTENSIONS for file in filenames])):
        print(f'Valid extensions are: {", ".join(VALIDS_IMAGES_EXTENSIONS)}')
        sys.exit(1)

    if(all([not isValidFile(file) for file in filenames])):
        print('Images must have a name like this: <frame>.<image extension> (1.png, 2.png, 3.png, 4.png)')
        sys.exit(1)

    convertToGif(filenames)