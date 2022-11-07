import cv2
import numpy as np

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
    con += (i)



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
#Imagen Resumen

cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()