'''
from PIL import Image
import os
folder="D:/post_phd/in cabin monitoring/images from google"
i=0
for filename in os.listdir(folder):

    image = Image.open(os.path.join(folder, filename))
    new_image = image.resize((640, 640))
    new_image.save('D:/post_phd/in cabin monitoring/resized images/im'+str(i)+'.jpg')
    i=i+1
'''


import cv2
import matplotlib.pyplot as plt
import os
folder="D:/post_phd/in cabin monitoring/rasha images/images for kids/babies in car seat"
i=1505
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename))
    if img is not None:
        img=cv2.resize(img, (640,640))
        cv2.imwrite('D:/post_phd/in cabin monitoring/resized images/im'+str(i)+'.jpg', img)
        i=i+1