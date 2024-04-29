from fractions import Fraction
from PIL import Image, ImageDraw, ImageFont, ImageOps
from style1 import create_watermark_style1
from style2 import create_watermark_style2
from style3 import create_watermark_style3
import PIL
import os

style2_padding = 0.07
def create_white(im, name, output_path, style): 
    style = style or '1'
    #print("STYLE:",style)
    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in im._getexif().items()
        if k in PIL.ExifTags.TAGS
    }
    logo = Image.open('./logo/sony.png').convert("RGBA")
    #print("设备制造商：",exif.get('Make'))
    if exif.get('Make') == 'SONY':
        logo = Image.open('./logo/sony.png').convert("RGBA")
    elif exif.get('Make') == 'Canon':
        logo = Image.open('./logo/canon.png').convert("RGBA")
    elif exif.get('Make') == 'DJI':
        logo = Image.open('./logo/dji.jpeg').convert("RGBA")
    elif exif.get('Make') == 'Apple':
        logo = Image.open('./logo/apple.png').convert("RGBA")
    im = ImageOps.exif_transpose(im)
    x, y = im.size
    #print("照片：",name,"尺寸",im.size)
    

    if style == '1':
        white = create_watermark_style1(im, exif, logo)
        target = Image.new('RGB', size=(x, y + white.size[1]), color=(255, 255, 255))
        # white.show()
        target.paste(im, (0, 0))
        target.paste(white, (0, y))
        op = output_path or './output/'
        target.save(op + name, quality=80)
    elif style == '2':
        white = create_watermark_style2(im, exif, logo)
        target = Image.new('RGB', size=(int(x*(1+style2_padding)), y + int(x*style2_padding/2) + white.size[1]), color=(255, 255, 255))
        # white.show()
        target.paste(im, (int(x*style2_padding/2), int(x*style2_padding/2)))
        target.paste(white, (int(x*style2_padding/2), y+int(x*style2_padding/2)))
        op = output_path or './output/'
        target.save(op + name, quality=80)
    elif style == '3':
        white = create_watermark_style3(im, exif, logo)
        target = Image.new('RGB', size=(x, y + white.size[1]), color=(255, 255, 255))
        # white.show()
        target.paste(im, (0, 0))
        target.paste(white, (0, y))
        op = output_path or './output/'
        target.save(op + name, quality=80)


if __name__ == '__main__':
    create_white()


