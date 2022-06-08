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
    output = open_with_exif(images.pop(0))

    for img in images:
        img = open_with_exif(img)
        sources.append(img)
    
    output.save(output_path, save_all=True, append_images=sources)




if __name__ == "__main__":
    default_folder = path.dirname(path.abspath(__file__))
    
    folder = default_folder
    combine_images(folder)
