import argparse
from yolo import YOLO, detect_video
from PIL import Image
import os

class detect():
    def __init__(self):
        c={}
        c['image'] = True
        c['input'] = 'D:\PyCharmProject\keras-yolo3\\test.jpg'
        c['output'] = 'D:\PyCharmProject\keras-yolo3\output1'
        self.yolo = YOLO(**c)

    def detect(self, path):
        image = Image.open(path)
        r_image, out = self.yolo.detect_image(image)
        r_image.save("D:\PyCharmProject\objDetect\keras-yolo3\\ui_result\\"+"result.jpg")
        return r_image,out
#
# l = os.listdir("D:\PyCharmProject\objDetect\keras-yolo3\JPEGImages")
# print(l)
# d = detect()
# f1 = open("D:\PyCharmProject\objDetect\keras-yolo3\\result\\03_car_result.txt", "w")
# s1=""
# f2 = open("D:\PyCharmProject\objDetect\keras-yolo3\\result\\03_bus_result.txt", "w")
# s2=""
# f3 = open("D:\PyCharmProject\objDetect\keras-yolo3\\result\\03_ship_result.txt", "w")
# s3=""
# f4 = open("D:\PyCharmProject\objDetect\keras-yolo3\\result\\03_plane_result.txt", "w")
# s4=""
# for i in l:
#     path = "D:\PyCharmProject\objDetect\keras-yolo3\JPEGImages\\"+i
#     img, out = d.detect(path)
#     print(i, "  ", out)
#     for key in out.keys():
#         q=out[key]
#         s = i+","+str(q[0])+","+str(q[1])+","+str(q[2][0])+","+str(q[2][1])+","+str(q[3][0])+","+str(q[3][1])
#         if str(q[0]) == 'car':
#             f1.write(str(s)+"\n")
#             s1=s1+s+"\n"
#         if str(q[0]) == 'bus':
#             f2.write(str(s)+"\n")
#             s2 = s2 + s + "\n"
#         if str(q[0]) == 'aeroplane':
#             s = i + "," + "plane" + "," + str(q[1]) + "," + str(q[2][0]) + "," + str(q[2][1]) + "," + str(q[3][0]) + "," + str(q[3][1])
#             f3.write(str(s)+"\n")
#             s3 = s3 + s + "\n"
#         if str(q[0]) == 'boat':
#             s = i + "," + "boat" + "," + str(q[1]) + "," + str(q[2][0]) + "," + str(q[2][1]) + "," + str(q[3][0]) + "," + str(q[3][1])
#             f4.write(str(s)+"\n")
#             s4 = s4 + s + "\n"
#         print(s)
#     img.save('D:\PyCharmProject\objDetect\keras-yolo3\output3\\'+i)
# f1.close()
# f2.close()
# f3.close()
# f4.close()
# print("---car---\n")
# print(s1)
# print("---bus---\n")
# print(s2)
# print("---plane---\n")
# print(s3)
# print("---ship---\n")
# print(s4)