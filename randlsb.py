import cv2
import binascii
import random
"""strr="a"
for i in range(0,1024):
    strr=strr+"a"
"""
strr=input()
bitstr=' '.join(format(ord(x), 'b') for x in strr)
print(bitstr)
bitstr=bitstr.replace(" ","")
print(bitstr)
print(len(bitstr))
lengt=str(len(bitstr))+"*"
print(lengt)
length=' '.join(format(ord(x), 'b') for x in lengt)
print(length)
length=length.replace(" ","")
print(length)

image = cv2.imread('IRONMANbmp.bmp',cv2.IMREAD_COLOR)
size=image.shape
print(size[0])
print(size[1])
print(len(bitstr))
l=len(bitstr)%3
ll=int(len(bitstr)/3)
print(l)
print(ll)
length_of_word=ll+1

counter=0
for i in range(0,length_of_word):
    random.seed( i )
    x=random.randint(0,size[0]-1)
    y=random.randint(0,size[1]-1)
    print ("first number  - ", random.randint(0,size[0])-1)
    print ("Second number- ", random.randint(0,size[1])-1)
    print(image[x][y])

    for k in range(0,3):
        if counter==len(bitstr):
            cv2.imwrite("randomlsb.bmp",image)
            break
        else:
            formated = "{0:b}".format(image[x, y][k])
            formated = formated[:-1]
            formated = formated+""+bitstr[counter]
            formated = int(formated, 2)
            image[x, y][k] = formated
            counter = counter + 1


output=[]
counter=0
for i in range(0,length_of_word):
    random.seed( i )
    x=random.randint(0,size[0]-1)
    y=random.randint(0,size[1]-1)
    print ("first number  - ", random.randint(0,size[0]-1))
    print ("Second number- ", random.randint(0,size[1]-1))
    print(image[x][y])
    for k in range(0,3):
        if counter==len(bitstr):
            break
        else:
            formated = "{0:b}".format(image[x, y][k])
            formated = formated[-1]
            output.append(formated)


output1=''.join(output)
print(output1)
output2=[]
x=0
for i in range(0,len(output1)):
    print(x)

    if x == len(output1) - 1:
        break
    try:
        str6 = ''.join(output1[x:x + 7])
        print(str6)
        if "100000" in str6:
            output2.append(" ")
            x=x+6
        else:
            n = int(str6, 2)
            n = binascii.unhexlify('%x' % n)
            output2.append(n.decode('utf-8'))
            x = x + 7

    except ValueError:
        print()
        break

    except:
        str6 = ''.join(output1[x:x + 7])
        print(str6)
        if "100000" in str6 :
            output2.append(" ")
            x=x+6
        else:
            n = int(str6, 2)
            n = binascii.unhexlify('0%x' % n)
            output2.append(n.decode('utf-8'))

print(output2)
out=''.join(output2)
print(out)

image = cv2.imread('IRONMANbmp.bmp')
cv2.imshow("before",image)

random= cv2.imread('randomlsb.bmp')
cv2.imshow("after randomlsb",random)
cv2.waitKey()

