# img2pdf

A simple script that converts images to a single PDF file.

## Get Started
---
### Clone repo
``` shell
git clone https://github.com/SpinningK/img2pdf.git
cd img2pdf
```
### Create virtual environtment(Optional)
> These commands are for mac and linux users
``` shell
python3 -m venv venv
source ./venv/bin/activate
```

### Install requirements
``` shell
pip3 install -r requirements.txt
```

### Try the demo
> This command will convert all demo images in the "images" direcotry of this project to a single pdf and save it as "output.pdf" in the same directory.
``` shell
python3 main.py
```

### Convert your own images
> You can put your own images in the "images" directory of this project just like the demo, and simply run:
``` shell
python3 main.py
```

> Also, you can specify the directory that contains all images with -d, and the output is always in the same directory as the input images:
``` shell
python3 main.py -d /path/to/the/directory
```