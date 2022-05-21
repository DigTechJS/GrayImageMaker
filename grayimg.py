from PIL import Image
import pyautogui as pt
import cv2
from numpy import asarray
import os
imagename = "C:\\Users\\hp\\Downloads\\l2.png"
image = Image.open(imagename)
image2= image.convert('L')
loc="C:\\Users\\hp\\OneDrive\\Desktop\\New folder"
name="image"
completeLoc=os.path.join(name+".png")
cv2.imwrite(os.path.join(loc , completeLoc), asarray(image2))
cv2.waitKey(0)
i=0
while i<5:
    pt.keyDown("#")
    pt.write("Gray Image Created Successfully\n")
    i+=1
#Gray Image Created Successfully
#Gray Image Created Successfully
#Gray Image Created Successfully
#Gray Image Created Successfully
#Gray Image Created Successfully








