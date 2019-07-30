import os
import xml.dom.minidom as xmldom



l = os.listdir("D:\PyCharmProject\objDetect\keras-yolo3\dataset\img")

path = "D:\PyCharmProject\objDetect\keras-yolo3\dataset\\ann"
f = open('train.txt', 'w', encoding='utf-8')
for i in l:
    # rint(i[:-4])

    xml_filepath = os.path.abspath(path+"\\"+i[:-4]+".xml")
    dom_obj = xmldom.parse(xml_filepath)
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
        index = " "
        if name == "bus":
            continue
        if name == "car":
            continue
        if name == "plane":
            index="1"
        if name == "ship":
            index="2"
        str = xmin + "," + ymin + "," + xmax+"," + ymax+","+index+" "
        base = base + str
        print(base)
    f.write("D:\PyCharmProject\objDetect\keras-yolo3\dataset\img\\"+i+" "+base[:-1]+"\n")

f.close()


