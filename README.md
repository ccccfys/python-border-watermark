# image-metadata-watermark


## Usage

```python
# -i input folder
# -o output folder
# -s style type
python3 cli.py -i prev/ -o after/ -s 1
```

## Example
### Before process Sony
![](./example/prev/DSC00307.JPG)

### After process Sony Style1
![](./example/after/DSC00307_1.JPG)

### After process Sony Style2
![](./example/after/DSC00307_2.JPG)

### After process Sony Style3
![](./example/after/DSC00307_3.JPG)

### After process Canon Style1
![](./example/after/IMG_1494.JPG)

### After process Apple Style1
![](./example/after/IMG_4759.JPG)

### After process Dji Style1
![](./example/after/dji_mimo_20240316_165244_20240316165243_1710600947481_photo.JPG)



## Know Issues
- 基于https://github.com/lovemegowin/image-metadata-watermark 进行开发
- 在作者原代码的基础上做出的改动包括：
	- 支持Sony、Canon、大疆、iphone相机的照片
	- 调整了水印样式
	- 增加了Style1、2、3两种边框，可供使用者选择
	- pillow10以上的版本可用
	- 针对索尼A7C2设备，显示的设备名称从ILCE-7CM2改为Alpha 7C II
	- 针对大疆Pocket3设备，显示的设备名称从PP-101改为Pocket 3

