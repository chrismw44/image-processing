import sys
import os
from PIL import Image

existing_folder = sys.argv[1]
new_folder = sys.argv[2]


if not os.path.exists(new_folder):
    os.mkdir(new_folder)

for file in os.listdir(existing_folder):
    file_path = os.path.join(existing_folder, file)
    if os.path.isfile(file_path):
        file_name = os.path.splitext(file)[0]
        img = Image.open(file_path)
        img.save(f'{new_folder}{file_name}.png', 'png')
