import cv2
import numpy as np
import os
import speech_recognition as sr
from gtts import gTTS, tts 
from playsound import playsound

coloractual = 'none'

def dibujar(mask,color):
  contornos, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE)
  for c in contornos:
    area = cv2.contourArea(c)
    if area > 3000:
      M = cv2.moments(c)
      if (M["m00"]==0): M["m00"]=1
      x = int(M["m10"]/M["m00"])
      y = int(M['m01']/M['m00'])
      nuevoContorno = cv2.convexHull(c)
      cv2.circle(frame,(x,y),7,(0,255,0),-1)
      epsilon = 0.01*cv2.arcLength(nuevoContorno,True)
      approx = cv2.approxPolyDP(nuevoContorno,epsilon,True)
      cv2.drawContours(frame, [nuevoContorno], 0, color, 3)

      if len(approx) == 3:
        if color == (0,0,255):
          cv2.putText(frame,'Rojo',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'rojo':
            if os.path.exists('rojoTriangulo.mp3'):
              playsound('rojoTriangulo.mp3')
            else:
              tts = gTTS('rojo, triángulo', lang='es-us')
              tts.save('rojoTriangulo.mp3')
              playsound('rojoTriangulo.mp3')
            coloractual == 'rojo'
        if color == (0,255,0):
          cv2.putText(frame,'Verde',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'verde':
            if os.path.exists('verdeTriangulo.mp3'):
              playsound('verdeTriangulo.mp3')
            else:
              tts = gTTS('verde, triángulo', lang='es-us')
              tts.save('verdeTriangulo.mp3')
              playsound('verdeTriangulo.mp3')
            coloractual == 'verde'
        if color == (255,0,0):
          cv2.putText(frame,'Azul',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'azul':
            if os.path.exists('azulTriangulo.mp3'):
              playsound('azulTriangulo.mp3')
            else:
              tts = gTTS('azul, Triángulo', lang='es-us')
              tts.save('azulTriangulo.mp3')
              playsound('azulTriangulo.mp3')
            coloractual == 'azul'
      
      if len(approx) == 4:
        if color == (0,0,255):  
          cv2.putText(frame,'Rojo',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'rojo':
            if os.path.exists('rojoCuadrado.mp3'):
              playsound('rojoCuadrado.mp3')
            else:
              tts = gTTS('rojo, cuadrado', lang='es-us')
              tts.save('rojoCuadrado.mp3')
              playsound('rojoCuadrado.mp3')
            coloractual == 'rojo'
        if color == (0,255,0):
          cv2.putText(frame,'Verde',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'verde':
            if os.path.exists('verdeCuadrado.mp3'):
              playsound('verdeCuadrado.mp3')
            else:
              tts = gTTS('verde, cuadrado', lang='es-us')
              tts.save('verdeCuadrado.mp3')
              playsound('verdeCuadrado.mp3')
            coloractual == 'verde'
        if color == (255,0,0):
          cv2.putText(frame,'Azul',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'azul':
            if os.path.exists('azulCuadrado.mp3'):
              playsound('azulCuadrado.mp3')
            else:
              tts = gTTS('azul, cuadrado', lang='es-us')
              tts.save('azulCuadrado.mp3')
              playsound('azulCuadrado.mp3')
            coloractual == 'azul'
      
      if len(approx) == 5:
        if color == (0,0,255):  
          cv2.putText(frame,'Rojo',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'rojo':
            if os.path.exists('rojoPentagono.mp3'):
              playsound('rojoPentagono.mp3')
            else:
              tts = gTTS('rojo, pentágono', lang='es-us')
              tts.save('rojoPentagono.mp3')
              playsound('rojoPentagono.mp3')
            coloractual == 'rojo'
        if color == (0,255,0):
          cv2.putText(frame,'Verde',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'verde':
            if os.path.exists('verdePentagono.mp3'):
              playsound('verdePentagono.mp3')
            else:
              tts = gTTS('verde, pentágono', lang='es-us')
              tts.save('verdePentagono.mp3')
              playsound('verdePentagono.mp3')
            coloractual == 'verde'
        if color == (255,0,0):
          cv2.putText(frame,'Azul',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'azul':
            if os.path.exists('azulPentagono.mp3'):
              playsound('azulPentagon.mp3')
            else:
              tts = gTTS('azul, pentágono', lang='es-us')
              tts.save('azulPentagono.mp3')
              playsound('azulPentagono.mp3')
            coloractual == 'azul'
      
      if len(approx) == 6:
        if color == (0,0,255):  
          cv2.putText(frame,'Rojo',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'rojo':
            if os.path.exists('rojoHexagono.mp3'):
              playsound('rojoHexagono.mp3')
            else:
              tts = gTTS('rojo, hexagono', lang='es-us')
              tts.save('rojoHexagono.mp3')
              playsound('rojoHexagono.mp3')
            coloractual == 'rojo'
        if color == (0,255,0):
          cv2.putText(frame,'Verde',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'verde':
            if os.path.exists('verdeHexagono.mp3'):
              playsound('verdeHexagono.mp3')
            else:
              tts = gTTS('verde, hexágono', lang='es-us')
              tts.save('verdeHexagono.mp3')
              playsound('verdeHexagono.mp3')
            coloractual == 'verde'
        if color == (255,0,0):
          cv2.putText(frame,'Azul',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'azul':
            if os.path.exists('azulHexagono.mp3'):
              playsound('azulHexagono.mp3')
            else:
              tts = gTTS('azul, hexágono', lang='es-us')
              tts.save('azulHexagono.mp3')
              playsound('azulHexagono.mp3')
            coloractual == 'azul'
      
      if len(approx) == 7:
        if color == (0,0,255):  
          cv2.putText(frame,'Rojo',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'rojo':
            if os.path.exists('rojoCirculo.mp3'):
              playsound('rojoCirculo.mp3')
            else:
              tts = gTTS('rojo, circulo', lang='es-us')
              tts.save('rojoCirculo.mp3')
              playsound('rojoCirculo.mp3')
            coloractual == 'rojo'
        if color == (0,255,0):
          cv2.putText(frame,'Verde',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'verde':
            if os.path.exists('verdeCirculo.mp3'):
              playsound('verdeCirculo.mp3')
            else:
              tts = gTTS('verde, círculo', lang='es-us')
              tts.save('verdeCirculo.mp3')
              playsound('verdeCirculo.mp3')
            coloractual == 'verde'
        if color == (255,0,0):
          cv2.putText(frame,'Azul',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
          if coloractual != 'azul':
            if os.path.exists('azulCirculo.mp3'):
              playsound('azulCirculo.mp3')
            else:
              tts = gTTS('azul, círculo', lang='es-us')
              tts.save('azulCirculo.mp3')
              playsound('azulCirculo.mp3')
            coloractual == 'azul'

cap = cv2.VideoCapture(0)

azulBajo = np.array([100,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)

rojoBajo1 = np.array([0,100,20],np.uint8)
rojoAlto1 = np.array([5,255,255],np.uint8)

rojoBajo2 = np.array([175,100,20],np.uint8)
rojoAlto2 = np.array([179,255,255],np.uint8)

verdeBajo = np.array([36, 100, 20], np.uint8)
verdeAlto = np.array([70, 255, 255], np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX

if os.path.exists('inicio.mp3'):
  playsound('inicio.mp3')
else:
  tts = gTTS('Hola, coloca las tarjetas frente la cámara', lang='es-us')
  tts.save('inicio.mp3')
  playsound('inicio.mp3')
while True:

  ret,frame = cap.read()

  if ret == True:
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    maskAzul = cv2.inRange(frameHSV,azulBajo,azulAlto)
    maskRojo1 = cv2.inRange(frameHSV,rojoBajo1,rojoAlto1)
    maskRojo2 = cv2.inRange(frameHSV,rojoBajo2,rojoAlto2)
    maskRojo = cv2.add(maskRojo1,maskRojo2)
    maskVerde = cv2.inRange(frameHSV, verdeBajo, verdeAlto)
    dibujar(maskAzul,(255,0,0))
    dibujar(maskRojo,(0,0,255))
    dibujar(maskVerde,(0,255,0))
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break

cap.release()
cv2.destroyAllWindows()