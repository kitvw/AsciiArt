# New file for running the ascii art converter.
# 
# program will take an image and turn it in to ascii art.
#
# inspired by: https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/
# written by: Kit Vander Wilt

from PIL import Image
import os

def tupleAvg(tuple):
    # Assume tuple is a tuple containing numbers
    # will return the floor of the average so as to avoid decimals.
    sum = 0
    for x in tuple:
        sum += x
    return sum // len(tuple)

# steps to complete
# 0. Choose an image
# 1. Read your image and print its height and width in pixels
path = input("Enter the file name: ")
pic = Image.open(path)
#print(pic.size) # (width, height) in pixels
pic = pic.resize((os.get_terminal_size()[0]-1,os.get_terminal_size()[1]-3))
'''term = os.get_terminal_size()
width,height = pic.size
ratio = width/(height/2)

print(term)
print(ratio)
print(int(term[1]*ratio-1),term[1]-4)
print(term[0]-1,term[0]//ratio-4)

if term[0]/ratio > term[1]: #can't fit image with ratio without scrolling
    width,height = int(term[1]*ratio-1),term[1]-4
else:
    width,height = term[0]-1,term[0]//ratio-4
print(width,height)
pic = pic.resize((width,height))'''
#pic = pic.resize((160,120))


x,y = pic.size
#x,y = 6,4
pixels = [[0 for i in range(x)] for j in range(y)] # using list comprehension because multiplication of lists creates shallow copies that all refer to the same object.
#print(pic.getbands())
#print(len(list(pic.getdata())))
#print(640 * 480)



# 2. Load your image’s pixel data into a 2-dimensional array
for c in range(y): # the number of rows = height of picture
    for r in range(x): # the number of columns = width of picture
        pixels[c][r] = pic.getpixel((r,c)) # getpixel returns a 3-tuple containing the R G B values (int between 0-255)
#print(pixels)



# 3. Convert the RGB tuples of your pixels into single brightness numbers
grayPixels = [[0 for i in range(x)] for j in range(y)]
for c in range(y):
    for r in range(x): 
        grayPixels[c][r] = tupleAvg(pixels[c][r]) # each value with be an int between 0 and 255
#print(pixels[3][4])
#print(grayPixels[3][4])



# 4. Convert brightness numbers to ASCII characters
thing = "`^\",:;Il!i~+_?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
#  all chars:      `.-'_:,"^>~<;r*=L\/!?cvz+sJ(7TF)x}YfitC1o|Z{3lnIyu]e2[EVwSaA54jPKk6XO9hMmWUGbpH8dqD#0R$NBQ%&g@
#thing = "`.-'_,^><;*=L/!cv+s(7F)}Yit1oZ{lnyue2EVSa54PK6X9hmWGbH8qD0RNB%&@"
asciiPixels = [[0 for i in range(x)] for j in range(y)]
for c in range(y):
    for r in range(x): 
        asciiPixels[c][r] = thing[ grayPixels[c][r] // 4 ]
#print(asciiPixels[3][4])
#print(thing[255//4])
#print(thing[160//4])



# 5. Print your ASCII art!
output = ''
for c in range(y):
    for r in range(x): 
        output += asciiPixels[c][r]
        #output += asciiPixels[c][r]
        #output += asciiPixels[c][r]
    output += '\n'
print(output)
