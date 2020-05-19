import os
import sys
from shutil import copyfile

if __name__ == "__main__":
    image_file = sys.argv[1]
    image_file_name = image_file.split('.')[0]
    image_file_extension = image_file.split('.')[1]
    file_path = os.path.dirname(os.path.abspath(__file__))
    assets_path = f"{file_path}/assets/img/posts/{image_file}"
    for each_extra_file_name in ['_placehold', '_thumb', '_thumb@2x']:
        dst_file = f"{file_path}/assets/img/posts/{image_file_name}{each_extra_file_name}.{image_file_extension}"
        copyfile(assets_path, dst_file)

