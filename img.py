import os
import PIL
from PIL import Image

from watermark import create_white


PATH = "./prev/" #需要拼接的图片所在的路径

PIL.Image.MAX_IMAGE_PIXELS = 93312000000000

def process_images(path, out_path, style):
    image_names = get_image_names(path)
    for image_name in image_names:
        if image_name != ".DS_Store":
            image = Image.open(path + image_name)
            create_white(image, image_name, out_path, style)
            print(image_name,"Finish!")


#获取需要拼接图片的名称
def get_image_names(path):
    #获取目标文件夹下的所有文件的文件
    image_names = list(os.walk(path))[0][2] 
    return image_names


if __name__ == '__main__':
    process_images(PATH)