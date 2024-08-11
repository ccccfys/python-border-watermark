# Python边框水印使用教程


![效果展示](https://github.com/ccccfys/python-border-watermark/blob/main/after/%E5%93%88%E8%8B%8F%E8%A3%81%E5%88%87.jpg)


#### 1. 在 <a href="https://www.python.org/" title="Python官网">Python官网</a> 下载并安装Python
 
#### 2. 安装pillow和click包
```python
pip install pillow -i  http://mirrors.aliyun.com/pypi/simple/
pip install click -i  http://mirrors.aliyun.com/pypi/simple/
```

#### 3. 下载项目代码：  <a href="https://github.com/ccccfys/python-border-watermark" title="Python边框水印">Python边框水印</a> 
#### 4. 设置Windows系统字体：原项目代码在非Windows系统上测试，Windows系统上需要修正字体路径。字体路径为：

```
C:/Windows/Fonts
```
#### 5. 添加新的相机logo：原项目代码仅支持佳能、索尼、苹果和大疆设备，可以自己添加其它支持的品牌。在logo文件夹中放入相机品牌logo图片，并在watermark.py中按照已有格式添加相应的代码。

#### 6. 在本地打开项目，运行代码即可对图片进行批量处理

```python
# -i input folder
# -o output folder
# -s style type
# -a author name
# -q quality 100为原图，不输入默认100
python3 cli.py -i prev/ -o after/ -s 1 -q 80
python3 cli.py -i prev/ -o after/ -s 2 -q 80
python3 cli.py -i prev/ -o after/ -s 3 -q 80
python3 cli.py -i prev/ -o after/ -s 4 -a ShiliChan -q 80
```

## Know Issues
- 在https://github.com/loannechan/image-metadata-watermark基础上进行了细微代码修改，以适应Windows系统
