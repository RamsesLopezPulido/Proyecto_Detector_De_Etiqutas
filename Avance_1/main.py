import cv2
import numpy as np

img = cv2.imread('rec.png')
img2 = img.copy()
# Convertir a escala de girises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar binarización a la imagen
_, th = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)

# Morfológica de cierre
kernel = np.ones((5,5), np.uint8)

# Funcion para operaciones mofologicas
closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

# Obtener bordes dela imagen
#bordes = cv2.Canny(closing, 135, 255)

# Buscar contornos
contoours, jerarquia = cv2.findContours(closing, cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)

#########


def dibujarContorno(contornos, color):
  global con
  con = 0
  for (i, c) in enumerate(contornos):

    M = cv2.moments(c)
    if (M["m00"]==0): M["m00"]==1
    x = int(M["m10"]/M["m00"])
    y = int(M["m01"]/M["m00"])
    cv2.drawContours(imagen, [c], 0, color, 2)
    cv2.putText(imagen, str(i+1), (x-10,y+10), 1, 2,(0,0,0),2)
    con += (i+1)



rojoBajo1 = np.array([0, 100, 20], np.uint8)
rojoAlto1 = np.array([10, 255, 255], np.uint8)
rojoBajo2 = np.array([175, 100, 20], np.uint8)
rojoAlto2 = np.array([180, 255, 255], np.uint8)
imagen = cv2.imread('rec.png')
imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
#Detectando colores

maskRojo1 = cv2.inRange(imagenHSV, rojoBajo1, rojoAlto1)
maskRojo2 = cv2.inRange(imagenHSV, rojoBajo2, rojoAlto2)
maskRojo =  cv2.add(maskRojo1, maskRojo2)
#Encontrando contornos


contornosRojo = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

dibujarContorno(contornosRojo, (0, 255, 255))
print(con)

##########

# Dibujar contornos
#cv2.drawContours(img2, contoours, -1, (0, 255, 0), 3)

cantidadPerfume = len(contoours)

if(con > 0):
    cv2.drawContours(img2, contoours, -1, (0, 255, 0), 3)
    cv2.putText(img2, str(cantidadPerfume) +
            ' etiquetas', (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 0, 255), 1, cv2.LINE_AA)
    print( str(cantidadPerfume) + ' etiquetas')
else:
    cv2.drawContours(img2, contoours, -1, (0, 0, 255), 3)
    cv2.putText(img2, str(cantidadPerfume) +
                ' Error', (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 1, cv2.LINE_AA)
    print(str(cantidadPerfume) + ' etiquetas')




cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Closing', cv2.WINDOW_NORMAL)
cv2.namedWindow('resultado', cv2.WINDOW_NORMAL)

cv2.imshow('Original', img)
cv2.imshow("Closing", closing)
#cv2.imshow("Bordes", bordes)
cv2.imshow("resultado", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()