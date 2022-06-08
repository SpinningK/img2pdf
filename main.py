from sys import exit, argv
from getopt import getopt, GetoptError
from PIL import Image, ImageOps
from os import path, listdir

EXTENSIONS = ['png', 'jpg', 'jpeg']

def get_images(folder_path):
    files = listdir(folder_path)
    images = []
    for file in files:
        extension = file.split(".").pop().lower()
        if extension in EXTENSIONS:
            images.append(path.join(folder_path, file))
    images.sort()
    return images

def open_with_exif(image):
    return ImageOps.exif_transpose(Image.open(image)).convert('RGB')

def combine_images(folder):
    images = get_images(folder)
    output_path = path.join(folder, 'output.pdf')
    sources = []

    try:
        output = open_with_exif(images.pop(0))
    except IndexError:
        print("No Image found in " + folder)
        exit(1)

    for img in images:
        img = open_with_exif(img)
        sources.append(img)
    
    output.save(output_path, save_all=True, append_images=sources)


if __name__ == "__main__":
    project_root = path.dirname(path.abspath(__file__))
    default_folder = path.join(project_root, "images")
    specified_folder = ""
    try:
        opts, args = getopt(argv[1:], "d:")
    except GetoptError:
        print("Wrong command line arguments, please try: ")
        print("python3 main.py [-d /path/to/directory/contains/all/images]")
        exit(2)

    for opt, arg in opts:
        if opt == "-d":
            specified_folder = arg

    folder = specified_folder if specified_folder else default_folder
    combine_images(folder)
