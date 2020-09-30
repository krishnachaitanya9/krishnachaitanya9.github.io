import os
import sys
from shutil import copyfile
from PIL import Image

basewidth = 230

if __name__ == "__main__":
    image_file = sys.argv[1]
    image_file_name = image_file.split('.')[0]
    if "-logo" not in image_file_name:
        raise Exception("The name should contain logo for example: pytorch-logo.jpg")
    image_file_extension = image_file.split('.')[1]
    file_path = os.path.dirname(os.path.abspath(__file__))
    original_image = f"{file_path}/assets/img/posts/{image_file}"
    img = Image.open(original_image)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    assets_path = f"{file_path}/assets/img/posts/{image_file_name}_placehold.{image_file_extension}"
    img.save(assets_path)
    for each_extra_file_name in ['_thumb', '_thumb@2x']:
        dst_file = f"{file_path}/assets/img/posts/{image_file_name}{each_extra_file_name}.{image_file_extension}"
        copyfile(assets_path, dst_file)
