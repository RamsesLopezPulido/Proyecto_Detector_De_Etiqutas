import numpy as np
import cv2
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image, ImageTk


def iniciarCamara():
    global cameraObject
    cameraObject = cv2.VideoCapture(0)
    capturarImagen()

def capturarImagen():
    global cameraObject

    # Verificar objeto
    if cameraObject is not None:
        # capturar imagen
        retval, imagen = cameraObject.read()
        if retval == True:

            imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

            top_left_corner_coordinates = (200, 130)
            bottom_right_corner_coordinates = (430, 260)

            color = (0, 255, 0)

            thickness = 3

            imagen = cv2.rectangle(imagen, top_left_corner_coordinates, bottom_right_corner_coordinates, color,
                                   thickness)

            #camera_video = cv2.imshow('Camera', imagen)

            img = Image.fromarray(imagen)
            img = img.resize((480, 640))
            imgTk = ImageTk.PhotoImage(image=img)
            captureLable.configure(image=imgTk)
            captureLable.image = imgTk
            captureLable.after(10, capturarImagen)



        else:
            captureLable.image= ""
            cameraObject.release()

def cerrarCamara():
    global cameraObject
    captureLable.image = ""
    cameraObject.release()

def cerrarVentana():
    raiz.destroy()

raiz = Tk()
raiz.geometry("482x540")
raiz.title("Camara")

captureFrame = Frame()
captureFrame.config(width=480, height=640)
captureFrame.place(x=0, y=0)

btnFrame = Frame()
btnFrame.config(width=480, height=100)
btnFrame.place(x=0, y=440)

captureLable = Label(captureFrame)
captureLable.place(x=0, y=0)

btnCapture = Button(btnFrame, text="Capturar",command=iniciarCamara)
btnCapture.place(x=20, y=40)

btnCerrarvideo = Button(btnFrame, text="Cerrar camara",command=cerrarCamara)
btnCerrarvideo.place(x=200, y=40)

btnCerrar = Button(btnFrame, text="Cerrar", command=cerrarVentana)
btnCerrar.place(x=400, y=40)

raiz.mainloop()