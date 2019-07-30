from PIL import Image
import image2gif
import numpy as np
import os

outfilename = "D:\PyCharmProject\objDetect\keras-yolo3\gif\\1\\1.gif" # 转化的GIF图片名称
l = os.listdir("D:\PyCharmProject\objDetect\keras-yolo3\gif\\1")
frames = []
for image_name in l:                # 索引各自目录
    im = Image.open("D:\PyCharmProject\objDetect\keras-yolo3\gif\\1\\"+image_name)             # 将图片打开，本文图片读取的结果是RGBA格式，如果直接读取的RGB则不需要下面那一步
    im = im.convert("RGB")                  # 通过convert将RGBA格式转化为RGB格式，以便后续处理
    im = np.array(im)                       # im还不是数组格式，通过此方法将im转化为数组
    frames.append(im)                       # 批量化
image2gif.writeGif(outfilename, frames, duration=0.1, subRectangles=False)