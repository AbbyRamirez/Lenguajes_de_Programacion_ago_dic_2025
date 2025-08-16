PROGRAM Ecdidos
IMPLICIT NONE
REAL:: v , v_0, a, t,x,x_0
character(len = 3), PARAMETER:: Velocidad = "m/s"
character(len = 6), PARAMETER:: Aceleracion = "m/s**2"
character(len = 1), PARAMETER:: Tiempo = "s"
character(len = 1), PARAMETER:: distancia = "m"
WRITE(*,*)"La ecuacion de la distancia es : x = x_0+(v_0*t+v*t)/2"
WRITE(*,*)"Escriba la velocidad,v_0,aceleracion,tiempo y dI"
READ(*,*)v,v_0,a,t,x_0
x = x_0+(v_0*t+v*t)/2
WRITE (*,*)"la velocidad inicial es de ",v_0,Velocidad
WRITE (*,*)"El tiempo es de ",t,Tiempo
WRITE (*,*)"la distancia inical es de ",x_0,distancia
WRITE (*,*)"la velocidad final es de ",x,Velocidad
WRITE (*,*)"la distancia final es de ",x,distancia


PAUSE

END PROGRAM Ecdidos
