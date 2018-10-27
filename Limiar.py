# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:11:42 2018

@author: IgorPC
"""


import numpy as np
from collections import deque
import warnings
warnings.filterwarnings("ignore")

#Sabemos que todas a imegens tem dimensao 200x200
def get_slices(img):
    
    w, h = img.shape
    slices = np.zeros(shape=(w, h), dtype = np.uint8)
    
#    semente[:, :3] = 255
#    semente[:, 100:103] = 255
#    semente[:, 50:53] = 255
#    semente[:, 150:153] = 255
#    semente[:, 197:] = 255
    
    slices[:3, :] = 255
    slices[50:53, :] = 255 
    slices[150:153, :] = 255
    slices[100:103, :] = 255
    slices[197:, :] = 255
    
    return slices

# Retorna uma lista com as coordeanadas dos pixels vizinhos do
# pixel img(x, y)
def get_vizinhos(x, y, w, h):
    lista = deque()
    pontos = [(x-1,y), (x+1, y), (x,y-1), (x,y+1),
              (x-1,y+1), (x+1, y+1), (x-1,y-1), (x+1,y-1),
             ]
    for p in pontos:
        if (p[0]>=0 and p[1]>=0 and p[0]<w and p[1]<h):
            lista.append((p[0], p[1]))        
    return lista

def get_coor_slices (img, slices):
    
    count = 0
    w, h = img.shape
    fila = deque()
    
    for x in range(w):
        for y in range(h):
            if slices[x,y]==255:
                count = count+1
                fila.append((x,y))
    #print (count)
    return fila

#def get_maior_dif(pixel, semente):
#    maior = 0
#    x, y = pixel
#    h, w = semente.shape # ou img.shape
#    vizinhos = get_vizinhos(x, y, w, h)
#    for i in range(len(vizinhos)):
#        if ((abs(img[pixel] - img[vizinhos[i]]) >= maior)):
#            maior = abs(img[pixel] - img[vizinhos[i]])
#            
#    return maior

#def get_intesidad_media (img, semente):
#    
#    #soma = np.zeros(h*3+w*3)
#    soma = 0
#    count = 0
#    h, w = img.shape
#    for x in range(h):
#        for y in range(w):
#            if semente[x, y]==255:
#                count = count+1
#                soma = soma + img[x, y]
#    print(count)
#    return soma/count

def get_maior_dif(img, pixel, slices):
    #maior = 0
    x, y = pixel
    h, w = slices.shape # ou img.shape
    vizinhos = get_vizinhos(x, y, w, h)
    difs = np.zeros(len(vizinhos))
    for i in range(len(vizinhos)):
        difs[i] = abs(img[pixel] - img[vizinhos[i]])        
    return difs.mean()

def get_epsilon (img):
    semente = get_slices(img)
    coor_p_semente = get_coor_slices(img, semente)
    difs = np.zeros(len(coor_p_semente))
    for i in range(len(coor_p_semente)):
        pixel = coor_p_semente.pop()
        difs[i] = get_maior_dif(img, pixel, semente)
    
    return difs.mean().round(5)

    
    
    
    
    
    
    
    
    
    
    