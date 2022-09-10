import numpy as np
import pandas as pd
import cv2 as cv2
import os
from skimage import io
from glob import glob   
from PIL import Image 
import matplotlib.pylab as plt
    

imagem = cv2.imread("349.jpg")
imagem = cv2.resize(imagem, (800,800))
cv2.imshow('imagem', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

color = ('r','g','b')
for i,col in enumerate(color):
    hist = cv2.calcHist([imagem],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()