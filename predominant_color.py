import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



def grab_frame(cap):
    ret,frame = cap.read()
    return cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

def atualizar(i):
    img = grab_frame(captura)
    im1.set_data(img)
    im2.set_data(retangulo(img))

def close(event):
    if event.key == 'q':
        plt.close(event.canvas.figure)


def unique_count_app(a):
    colors, count = np.unique(a.reshape(-1,a.shape[-1]), axis=0, return_counts=True)
    return colors[count.argmax()]

def retangulo(img):
    r, g, b = contar_kmeans(img)
    h, w, c = img.shape
    rect = np.zeros((h, w, 3), np.uint8)
    rect[0:h, 0:w] = (r,g,b)
    return rect

def contar_kmeans(img):
    data = np.reshape(img, (-1,3))
    data = np.float32(data)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness, labels, centers = cv2.kmeans(data, 1, None, criteria, 10, flags)
    return centers[0]

#Inicialização
captura = cv2.VideoCapture(0)
imagem = grab_frame(captura)

#Cria os dois subplots
ax1 = plt.subplot(1,2,1)
ax2 = plt.subplot(1,2,2)

#Cria duas imagens nos subplots
im1 = ax1.imshow(imagem)
im2 = ax2.imshow(retangulo(imagem))

#Animação e atualização
ani = FuncAnimation(plt.gcf(), atualizar, interval=200)

#Fechar
cid = plt.gcf().canvas.mpl_connect("key_press_event", close)
#Mostrar o gráfico
plt.show()
