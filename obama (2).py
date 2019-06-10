#import library
from PIL import Image

#opening the image
image= Image.open("catanddog.jpg")
#image.show()

#get the RBG values
imdata = image.getdata()
imagelist= list(imdata)
#print(imagelist)

newimg = Image.new("RGB",(620,290) )    #to make it any image size do    int(image.size()
#newimg.show()
newlist = []

def pixsum(pix):
    return pix[0]+pix[1]+pix[2]
#making a for loop to change the RGB values
for pix in imagelist:
    if (pixsum(pix) < 182):
        newlist.append((0,51,76))
    if ((pixsum(pix) >= 182) and (pixsum(pix) < 364)):
        newlist.append((217,26,33))
    if ((pixsum(pix) >= 364) and (pixsum(pix) < 564)):
        newlist.append((112,150,166))
    if (pixsum(pix) >= 564):
        newlist.append((252,227,166))


newimg.putdata(newlist)
newimg.show()
        #make a new pixel in the color pink
        #and append it to the new list
