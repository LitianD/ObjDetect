import os

l = os.listdir(r"D:\PyCharmProject\objDetect\keras-yolo3\positiveimageset")
fa =open("train1.txt","w")
plane =0
ship = 0
for i in l:
    str = r"D:\PyCharmProject\objDetect\keras-yolo3\ground truth\\"+i[:-4]+r".txt"
    f = open(str)

    base = ""
    while True:
        text = f.readline()

        if not text:
            break
        t = text.replace("(", "")
        t1 = t.replace(")", "")
        t2 = t1.replace(" ", "")
        t3 = t2.replace("\n", "")
        print(t3.split(","))
        ls = t3.split(",")
        if len(ls)>=5:
            if ls[4]=='1':
                base = base + " " + t3[:-1]+'0'
                plane=plane+1
            if ls[4] == '2':
                base = base + " " + t3[:-1]+'1'
                ship = ship+1
    if len(base)>0:
        s = r"D:\PyCharmProject\objDetect\keras-yolo3\positiveimageset\\"+i+base+"\n"
    fa.write(s)
print(plane,"" ,ship )
f.close()
