import argparse
from yolo import YOLO, detect_video
from PIL import Image


class detect():
    def __init__(self):
        c={}
        c['image'] = True
        c['input'] = 'D:\PyCharmProject\keras-yolo3\\test.jpg'
        c['output'] = 'D:\PyCharmProject\keras-yolo3\output'
        self.yolo = YOLO(**c)

    def detect(self, path):
        image = Image.open(path)
        r_image, out = self.yolo.detect_image(image)
        print(type(out))
        print(out)
        #r_image.show()
        r_image.save('D:\PyCharmProject\objDetect\keras-yolo3\output\\test.jpg')
        return out

# d = detect()
# d.detect("D:\PyCharmProject\objDetect\keras-yolo3\\test.jpg")