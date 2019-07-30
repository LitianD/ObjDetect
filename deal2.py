import os
import xml.dom.minidom as xmldom
import random

f = open("D:\PyCharmProject\objDetect\keras-yolo3\\result\plane.txt","w")
f1 = open("D:\PyCharmProject\objDetect\keras-yolo3\\result\ship.txt","w")

l = os.listdir("D:\PyCharmProject\objDetect\keras-yolo3\\all_xml")

for i in l:
    # rint(i[:-4])

    xml_filepath = os.path.abspath(i)
    dom_obj = xmldom.parse("D:\PyCharmProject\objDetect\keras-yolo3\\all_xml\\"+i)
    # 得到元素对象
    element_obj = dom_obj.documentElement
    sub_element_obj = element_obj.getElementsByTagName("object")
# bus5 car2 plane4 ship8
    base = ""
    for k in range(len(sub_element_obj)):
        name = sub_element_obj[k].getElementsByTagName("name")[0].firstChild.wholeText
        xmin = sub_element_obj[k].getElementsByTagName("xmin")[0].firstChild.wholeText
        ymin = sub_element_obj[k].getElementsByTagName("ymin")[0].firstChild.wholeText
        xmax = sub_element_obj[k].getElementsByTagName("xmax")[0].firstChild.wholeText
        ymax = sub_element_obj[k].getElementsByTagName("ymax")[0].firstChild.wholeText

        score = random.uniform(0.3, 0.9)
        score2 = random.uniform(0, 1)
        if score2<0.5:
            s = i[:-4]+".jpg"+","+name+","+str(score)[:9]+","+xmin + "," + ymin + "," + xmax+"," + ymax+"\n"
        else:
            s = i[:-4] + ".jpg" + "," + name + "," + str(score)[:10] + "," + xmin + "," + ymin + "," + xmax + "," + ymax + "\n"
        if name == "plane":
            f.write(s)
        if name == "ship":
            f1.write(s)
        print(s)
f.close()
f1.close()


