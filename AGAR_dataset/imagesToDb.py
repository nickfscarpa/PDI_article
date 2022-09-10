import numpy as np
import pandas as pd
import cv2 as cv2
import os as os
from skimage import io
from glob import glob   
from PIL import Image 
import matplotlib.pylab as plt
    
def load(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith(".jpg"):
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)           
    return images

root = 'C:/Users/User/Documents/GitHub/Math2237/PDI_article/AGAR_dataset/'
path1 = os.path.abspath('C:/Users/User/Documents/GitHub/Math2237/PDI_article/AGAR_dataset/higher-resolution-bright/*.jpg')
path2 = os.path.abspath('C:/Users/User/Documents/GitHub/Math2237/PDI_article/AGAR_dataset/higher-resolution-dark/*.jpg')
path3 = os.path.abspath('C:/Users/User/Documents/GitHub/Math2237/PDI_article/AGAR_dataset/higher-resolution-vague/*.jpg')
path4 = os.path.abspath('C:/Users/User/Documents/GitHub/Math2237/PDI_article/AGAR_dataset/lower-resolution/*.jpg')
folder = os.path.join(path1, path2, path3, path4)

folders = [os.path.join(root, x) for x in ('higher-resolution-bright', 'higher-resolution-dark', 'higher-resolution-vague', 'lower-resolution')]
all_images = [img for folder in folders for img in load(folder)]

for i in all_images:
    resized = cv2.resize(i, (1280,720))
    cv2.imshow("img", resized)
    cv2.waitKey(50)

