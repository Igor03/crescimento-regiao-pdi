import matplotlib.pyplot as plt
import numpy as np
from collections import deque
from scipy import signal as sg
import cv2
from Limiar import get_epsilon
import Atributos as atb

def obterSemente(image):
    w, h = image.shape
    semente = np.zeros((w, h))
    semente[:, :3] = 255 # Lateral esquerda
    semente[:, (h-3):] = 255 # Lateral direita
    
    return semente

def vizinhos(x, y, w, h):
    lista = deque()
    
    pontos = [(x-1,y), (x+1, y), (x,y-1), (x,y+1),
              (x-1,y+1), (x+1, y+1), (x-1,y-1), (x+1,y-1),
             ]
    for p in pontos:
        if (p[0]>=0 and p[1]>=0 and p[0]<w and p[1]<h):
            lista.append((p[0], p[1]))
            
    return lista
    
def crescerRegiao(image, reg, epsilon=5):
    w, h = image.shape
    
    fila = deque()
    for x in range(w):
        for y in range(h):
            if reg[x,y]==255:
                fila.append((x,y))
                
    while fila: 
        ponto = fila.popleft()
        x = ponto[0]
        y = ponto[1]

        v_list = vizinhos(x, y, w, h)
        for v in v_list:
            v_x = v[0]
            v_y = v[1]
            if( (reg[v_x][v_y]!=255) and (abs(image[x][y]-image[v_x][v_y])<epsilon)):
                reg[v_x][v_y] = 255
                fila.append((v_x,v_y))
    return reg
                
def plots(p1, p2, pil):
    fig = plt.figure(figsize=(9,3), dpi=80)
    a = fig.add_subplot(1,3,1)
    a.axis('off')
    plt.imshow(p1, cmap=plt.cm.gray)
    a.set_title('Original em tons de cinza')

    a = fig.add_subplot(1,3,2)
    a.axis('off')
    plt.imshow(p2, cmap=plt.cm.gray)
    a.set_title('Imagem segmentada')

    a = fig.add_subplot(1,3,3)
    a.axis('off')
    plt.imshow(p1, cmap=plt.cm.gray)
    plt.imshow(p2, alpha=0.5)
    a.set_title('Região Segmentada')

    plt.savefig('resultados/'+pil+'/('+x+').jpg')

    plt.show()
    
def inv_img (img):
    h, w = img.shape
    #print ('A:', h, 'L:', w)
    for i in  range(h):
        for j in  range(w):
            if img[i, j] == 0:
                img[i, j] = 255
            else:
                img[i, j] = 0
    return img
#######################################################################
    
k = 0
pil = 'WB' 
qtd_imgs = 18
area_media = 0
circ_media = 0
razao_ap_media = 0
desv_padrao_medio = 0
for i in range (qtd_imgs):
    k=k+1
    x = str(k)
    img1 = cv2.imread('images/'+pil+'/'+pil+' ('+x+').jpg', 0)
    img1 = (img1 * 255).round().astype(np.uint8)
    semente = obterSemente(img1)
    media3 = [[1./9., 1./9., 1./9.], 
          [1./9., 1./9., 1./9.],
          [1./9., 1./9., 1./9.]]
    c_media = sg.convolve(img1, media3, "valid")
    #c_media = cv2.medianBlur(img1,9)
    v = get_epsilon(c_media)
    regiao = crescerRegiao(c_media, semente, epsilon=v)
    regiao = inv_img(regiao)
    regiao = regiao.astype(np.uint8)
    regiao = cv2.medianBlur(regiao,9)
    #regiao = atb.remover_ruido(regiao)
    #cv2.imwrite(pil+'/('+x+').jpg', regiao)
    print ('----------------------------')
    print ('Pilula '+pil+' ('+x+')')
    print ('----------------------------')
    #Calculando atributos
    atb.mostrar_atrib(c_media, regiao)
    area_media = area_media + atb.get_area(regiao)
    razao_ap_media = razao_ap_media + atb.get_razao_ap(regiao)
    circ_media = circ_media + atb.get_circularidade(regiao)
    desv_padrao_medio = desv_padrao_medio + atb.get_desvioP(c_media, regiao) 
    plots(c_media, regiao, pil)
    
print ('Atributos '+ pil + '\n------------------')
print ('Área média: ', area_media/qtd_imgs)
print ('Razão entre área e perímetro: ', razao_ap_media/qtd_imgs)
print ('Circularidade média: ', circ_media/qtd_imgs)
print ('Desvio padrão: ', desv_padrao_medio/qtd_imgs)

