from PIL import Image
import os

string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*(),./<>?;':\"[]\\{}|-=_+"
print(len(string))

pic = Image.open("C:/Users/Kit Vander Wilt/Pictures/ascii_consolas.png")
print(pic.size)
temp = pic.crop((0,0,7,15))
#temp.show()

print(pic.getpixel((0,0))) # from JPG: (198,194,195)  |  from PNG: (192,192,192, 255)
print(pic.getpixel((2,6))) # from JPG: (0,4,11)       |  from PNG: (0,0,0,255)

backgroundPixel = pic.getpixel((0,0))
for i in range(pic.size[0]):
    for j in range(pic.size[1]):
        if pic.getpixel((i,j)) == backgroundPixel:
            #print(i,j)
            pic.putpixel((i,j), (255,255,255,255))
#pic.show()
greyPic = pic.convert("L")
#greyPic.show()

#print(greyPic.getpixel((0,6)))
#print(greyPic.getpixel((1,6)))
#print(greyPic.getpixel((2,6)))
mapping=  []

for char in range(len(string)): #range(0, 658, 7):
    #print(string[char])
    tempPic = greyPic.crop((char*7,0,(char+1)*7,15))
    #tempPic.show()
    total = 0
    for i in range(0, 7):
        for j in range(0,15):
            total += tempPic.getpixel((i,j))
    avg = total / (7*15)
    mapping.append(avg)

tempVal = 0
stringList = list(string)
for a in range(len(mapping)):
    for b in range(len(mapping)):
        if mapping[a] < mapping[b]:
            tempVal = mapping[a]
            mapping[a] = mapping[b]
            mapping[b] = tempVal
            tempVal = stringList[a]
            stringList[a] = stringList[b]
            stringList[b] = tempVal
print(stringList)

output = ""
for i in range(len(stringList)):
    print(stringList[i] + "\t" + str(mapping[i]))
    output = stringList[i] + output

print(output)
