import numpy as np
from scipy import ndimage,misc
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import random

mapache = misc.face()
N = 3

xImagen = 768
yImagen = 1024
if N == 3:
    mapache = np.delete(mapache,1,axis=1)
    yImagen = 1023

arregloCuadros = []
for linea in np.hsplit(mapache,N):
    print(linea.shape)
    arregloCuadros.append(np.split(linea,N))
    print(len(arregloCuadros))
arregloCuadros = np.array(arregloCuadros)


for arreglo in arregloCuadros:
    np.random.shuffle(arreglo)
np.random.shuffle(arregloCuadros)
print(type(arregloCuadros))

posX = random.randint(0,N-1) 
posY = random.randint(0,N-1) 
arregloCuadros[posX][posY] = np.full((int(xImagen/N), int(yImagen/N), 3), 255)

lineas = arregloCuadros.reshape(N,xImagen,int(yImagen/N),3)
imagenNueva = np.stack(lineas,axis=1).reshape(xImagen,yImagen,3)


myobjct = plt.imshow(imagenNueva, extent=[0, yImagen, 100, xImagen])
plt.plot()


class Index(object):
    ind = 0
    posX = 0
    posY = 0
    def __init__(self,posX,posY):     
        self.posX = posX
        self.posY = posY
    
    def arriba(self, event):
        if not (self.posY == N-1):
            aux = arregloCuadros[self.posX][self.posY].copy()
            arregloCuadros[self.posX][self.posY] = arregloCuadros[self.posX][self.posY+1].copy()
            arregloCuadros[self.posX][self.posY+1] = aux.copy()
            lineas = arregloCuadros.reshape(N,xImagen,int(yImagen/N),3)
            imagenNueva = np.stack(lineas,axis=1).reshape(xImagen,yImagen,3)
            myobjct.set_data(imagenNueva)
            self.posY += 1
            print("finalizado")
        else:
            pass

    def abajo(self, event):
        if not (self.posY == 0):
            aux = arregloCuadros[self.posX][self.posY].copy()
            arregloCuadros[self.posX][self.posY] = arregloCuadros[self.posX][self.posY-1].copy()
            arregloCuadros[self.posX][self.posY-1] = aux.copy()
            lineas = arregloCuadros.reshape(N,xImagen,int(yImagen/N),3)
            imagenNueva = np.stack(lineas,axis=1).reshape(xImagen,yImagen,3)
            myobjct.set_data(imagenNueva)
            self.posY -= 1
            print("finalizado")
        else:
            pass

    def izquierda(self, event):
        if not (self.posX == N-1):
            aux = arregloCuadros[self.posX][self.posY].copy()
            arregloCuadros[self.posX][self.posY] = arregloCuadros[self.posX+1][self.posY].copy()
            arregloCuadros[self.posX+1][self.posY] = aux.copy()
            lineas = arregloCuadros.reshape(N,xImagen,int(yImagen/N),3)
            imagenNueva = np.stack(lineas,axis=1).reshape(xImagen,yImagen,3)
            myobjct.set_data(imagenNueva)
            self.posX += 1
            print("finalizado")
        else:
            pass

    def derecha(self, event):
        if not (self.posX == 0):
            aux = arregloCuadros[self.posX][self.posY].copy()
            arregloCuadros[self.posX][self.posY] = arregloCuadros[self.posX-1][self.posY].copy()
            arregloCuadros[self.posX-1][self.posY] = aux.copy()
            lineas = arregloCuadros.reshape(N,xImagen,int(yImagen/N),3)
            imagenNueva = np.stack(lineas,axis=1).reshape(xImagen,yImagen,3)
            myobjct.set_data(imagenNueva)
            self.posX -= 1
            print("finalizado")
        else:
            pass

callback = Index(posX,posY)
axarriba = plt.axes([0.45, 0.06, 0.1, 0.05])
axabajo = plt.axes([0.45, 0.01, 0.1, 0.05])
axizquierda = plt.axes([0.35, 0.035, 0.1, 0.05])
axderecha = plt.axes([0.55, 0.035, 0.1, 0.05])

barriba = Button(axarriba, 'Arriba')
barriba.on_clicked(callback.arriba)
babajo = Button(axabajo, 'Abajo')
babajo.on_clicked(callback.abajo)
bizquierda = Button(axizquierda, 'Izquierda')
bizquierda.on_clicked(callback.izquierda)
bderecha = Button(axderecha, 'Derecha')
bderecha.on_clicked(callback.derecha)

plt.show()