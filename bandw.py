#import library
from PIL import Image

#opening the image
image= Image.open("tiger.jpg")
#image.show()

#get the RBG values
imdata = image.getdata()
imagelist= list(imdata)
#print(imagelist)

newimg = Image.new("RGB",(999,773) )    #to make it any image size do    int(image.size()
#newimg.show()
newlist = []

def pixsum(pix):
    return pix[0]+pix[1]+pix[2]
#making a for loop to change the RGB values
for pix in imagelist:
    if (pixsum(pix) < 100):
        newlist.append((0,0,0))
    if ((pixsum(pix) >= 100) and (pixsum(pix) < 200)):
        newlist.append((45,45,45))
    if ((pixsum(pix) >= 200) and (pixsum(pix) < 300)):
        newlist.append((90,90,90))
    if ((pixsum(pix) >= 300) and (pixsum(pix) < 400)):
        newlist.append((135,135,135))
    if ((pixsum(pix) >= 400) and (pixsum(pix) < 500)):
        newlist.append((180,180,180))
    if ((pixsum(pix) >= 500) and (pixsum(pix) < 600)):
        newlist.append((215,215,215))
    if (pixsum(pix) >= 600):
        newlist.append((255,255,255))


newimg.putdata(newlist)
newimg.show()
        #make a new pixel in the color pink
        #and append it to the new list
