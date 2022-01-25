import os
import sys
from PIL import Image
# check whether the user passed the input image or not
if len(sys.argv) > 1:
    directory = sys.argv[1]
    for file in os.listdir(directory):
        if file[-4:] not in ['.jpg', '.png']:
            # filename = file.split(".")
            target_name = file[:-3] + ".jpg"
            img = Image.open(directory + '/' + file)
            rgb_image = img.convert('RGB')
            rgb_image.save(directory + '/' + target_name)
            print("Converted image saved as " + target_name)
            os.remove(directory + '/' + file)
            print("Deleted " + file)
else:
    print("please execute the script with input image as : python imgconverter.py <directory>")
