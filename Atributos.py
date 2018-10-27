# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 18:26:19 2018

@author: IgorPC
"""

from Limiar import get_vizinhos
#from Limiar import get_coor_ps
import math
import numpy as np
from collections import deque

def get_area(img):
    w, h = img.shape
    area = 0
    for i in range (w):
        for j in range (h):
            if img[i, j] == 255:
                area = area + 1
    return area

def ver_vizinho_branco(img, x, y):
    h, w = img.shape
    vizinhos = get_vizinhos(x, y, w, h)
    for i in range(len(vizinhos)):
        if img[vizinhos[i]]==0 and img[x, y]==255:
            return True
        return False

def get_coor_ps (img):
    # Após a imagem passar pelo processo de convolucao sao perdirdos
    # 4 pixeis
    w, h = img.shape
    coor = deque()
    for i in range (w-2):
        for j in range (h-2):
            if img[i, j] == 255:
                coor.append((i, j))
    return coor


def get_perimetro(img):
    h, w = img.shape
    perimetro = 0
    for i in range (h):
        for j in range (w):
            if ver_vizinho_branco(img, i, j):
                perimetro = perimetro + 1
    return perimetro+1 # Quando ocorrem erros na segmentacao

def get_circularidade (img):
    
    return ((4*math.pi*get_area(img)/(get_perimetro(img)**2)))

def get_desvioP (img, img_seg):
    #w, h = img_seg.shape
    coor_ps = get_coor_ps(img_seg)
    intensi_pix = np.zeros(len(coor_ps))
    for i in range (intensi_pix.size):
        intensi_pix[i] = img[coor_ps[i]]
    
    return intensi_pix.std()

def get_razao_ap (img):
    return (get_area(img))/(get_perimetro(img))

#def get_desvioP (img):
#    return img.std()

def mostrar_atrib (img, img_seg):
    print ('Área: ', get_area(img_seg))
    print ('Razao entre área e perímetro: ', (get_area(img_seg))/(get_perimetro(img_seg)))
    print ('Circularidade: ', get_circularidade(img_seg))
    print ('Desvio padrão: ', get_desvioP(img, img_seg))


def remover_ruido (img):
    w, h = img.shape
    count_v_brancos = 0
    count_v_pretos = 0
    p_brancos = get_coor_ps(img)
    for p in p_brancos:
        p_vizinhos = get_vizinhos(p[0], p[1], h, w)
        while p_vizinhos:
            if img[p_vizinhos.popleft()] == 0:
                count_v_pretos = count_v_pretos + 1
            else:
                count_v_brancos = count_v_brancos + 1
        if (count_v_pretos > count_v_brancos):
            img[p] = 0
    return img        