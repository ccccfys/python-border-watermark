from fractions import Fraction
from PIL import Image, ImageDraw, ImageFont, ImageOps
from devicename import device_name
import PIL
import os

fontPath = "C:/Windows/Fonts"
bold_font = os.path.join(fontPath, "Comic Sans MS/comicbd.ttf")
regular_font = os.path.join(fontPath, "Comic Sans MS/comicbd.ttf")
# Supplemental/
scale = 10
benchmark_bold_font_size = 20
benchmark_regular_font_size = 18
benchmark_device_font_size = 34
benchmark_width = 800
benchmark_padding = 24
benchmark_margin = 8

def create_watermark_style4(im_target, exif, logo, author):
    device_type = device_name(exif.get('Model'))
    metadata = str(int(exif.get('FocalLength'))) + 'mm ' + 'f/' + str(exif.get('FNumber')) + ' ' + str(Fraction(exif.get('ExposureTime'))) + ' ISO ' + str(exif.get('ISOSpeedRatings'))
    #print(metadata)
    authordata = 'Shot By '+author
    t_size = im_target.size
    scale = t_size[0] // benchmark_width
    bold_font_size =  scale * benchmark_bold_font_size
    device_font_size=  scale * benchmark_device_font_size
    regular_font_size =  scale * benchmark_regular_font_size
    margin = scale * benchmark_margin
    padding = scale * benchmark_padding
    b_font = ImageFont.truetype(bold_font, bold_font_size)
    device_font = ImageFont.truetype(regular_font, device_font_size)
    r_font = ImageFont.truetype(regular_font, regular_font_size, encoding="unic")

    draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    device_type_textsize = draw.textbbox((0,0),text = device_type, font=b_font) ## 拿到字体大小 计算白边高度

    device_type_height = device_type_textsize[3] - device_type_textsize[1]
    meta_textsize = draw.textbbox((0,0),text = authordata, font=r_font)

    meta_height = meta_textsize[3] - meta_textsize[1]
    device_textsize = draw.textbbox((0,0),text = device_type, font=device_font)
    #print("数据高度",metadata_textsize)
    device_height = device_textsize[3] - device_textsize[1]
    device_width = device_textsize[2] - device_textsize[0]
    
    #textbsize:(width, height)
    #textbbox:(left, top, right, bottom) bounding box

    im_white = Image.new('RGBA', size=(t_size[0], device_type_height + padding * 2 + meta_height + margin), color=(255, 255, 255))
    im_white_draw = ImageDraw.Draw(im_white)
    # metadata
    im_white_draw.text((padding, padding), metadata, fill=(0, 0, 0), font=b_font)
    # author
    im_white_draw.text((padding, padding + device_type_height + margin), authordata, fill=(90, 90, 90), font=r_font)
    # device
    device_x = t_size[0] - device_width - padding
    # line scale 线条宽度
    line_x = device_x - margin - scale -padding
    im_white_draw.line((line_x, padding, line_x, im_white.size[1] - padding), fill=(221, 221, 221), width=2*scale)
    im_white__logo_height = im_white.size[1] - padding * 2
    im_white__logo_width = logo.size[0] / logo.size[1] * im_white__logo_height
    # 0.6 logo logo 调整系数
    logo_resized = logo.resize((int(im_white__logo_width), int (im_white__logo_height)), Image.LANCZOS)
    # 第三个参数蒙版 让 logo 背景变透明
    logo_x = device_x - margin * 2 - logo_resized.size[0] - 2*padding
    logo_y =  padding
    im_white.paste(logo_resized, (logo_x, logo_y), logo_resized)
    # metadata
    device_y = padding + (logo_resized.size[1] - device_height)//4
    im_white_draw.text((device_x, device_y), device_type, fill=(0, 0, 0), font=device_font)

    return im_white

if __name__ == '__main__':
    create_watermark_style4()
