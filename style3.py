from fractions import Fraction
from PIL import Image, ImageDraw, ImageFont, ImageOps
from devicename import device_name
import PIL
import os

fontPath = "/System/Library/Fonts/"
bold_font = os.path.join(fontPath, "Supplemental/Arial Bold.ttf")
regular_font = os.path.join(fontPath, "Supplemental/Arial.ttf")
# Supplemental/
scale = 10
benchmark_bold_font_size = 20
benchmark_regular_font_size = 12
benchmark_meta_font_size = 20
benchmark_width = 800
benchmark_padding = 24
benchmark_margin = 8

def create_watermark_style3(im_target, exif, logo):
    metadata = str(int(exif.get('FocalLength'))) + 'mm ' + 'f/' + str(exif.get('FNumber')) + ' ' + str(Fraction(exif.get('ExposureTime'))) + ' ISO ' + str(exif.get('ISOSpeedRatings'))
    #print(metadata)
    t_size = im_target.size
    scale = t_size[0] // benchmark_width
    bold_font_size =  scale * benchmark_bold_font_size
    meta_font_size=  scale * benchmark_meta_font_size
    regular_font_size =  scale * benchmark_regular_font_size
    margin = scale * benchmark_margin
    padding = scale * benchmark_padding
    b_font = ImageFont.truetype(bold_font, bold_font_size)
    meta_font = ImageFont.truetype(regular_font, meta_font_size)
    r_font = ImageFont.truetype(regular_font, regular_font_size)

    draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    
    metadata_textsize = draw.textbbox((0,0),text = metadata, font=meta_font)
    #print("数据高度",metadata_textsize)
    metadata_height = metadata_textsize[3] - metadata_textsize[1]
    metadata_width = metadata_textsize[2] - metadata_textsize[0]
    
    #textbsize:(width, height)
    #textbbox:(left, top, right, bottom) bounding box

    im_white = Image.new('RGBA', size=(t_size[0], metadata_height *3 + padding * 3  + margin), color=(255, 255, 255))
    im_white_draw = ImageDraw.Draw(im_white)
    # metadata
    metadata_x = t_size[0]//2 - metadata_width//2
    im_white__logo_height = metadata_height * 2.5
    im_white__logo_width = logo.size[0] / logo.size[1] * im_white__logo_height
    # 0.6 logo logo 调整系数
    logo_resized = logo.resize((int(im_white__logo_width), int (im_white__logo_height)), Image.LANCZOS)
    # 第三个参数蒙版 让 logo 背景变透明
    logo_x = t_size[0]//2 - logo_resized.size[0]//2
    logo_y =  padding
    im_white.paste(logo_resized, (logo_x, logo_y), logo_resized)
    # metadata
    metadata_y = padding//2 + logo_y + im_white__logo_height
    im_white_draw.text((metadata_x, metadata_y), metadata, fill=(170, 170, 170), font=meta_font)

    return im_white

if __name__ == '__main__':
    create_watermark_style3()