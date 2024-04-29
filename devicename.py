import os
import PIL
from PIL import Image



#特殊设备名字更换
def device_name(name):
    if name == "PP-101":
        name = "Pocket 3"
    elif name == "ILCE-7CM2":
        name = "Alpha 7C II"
    return name

if __name__ == '__main__':
    device_name(PATH)