PROGRAM ec_de_distancia
IMPLICIT NONE
REAL:: v , v_0, a, t,x_0,x
character(len = 3), PARAMETER:: Velocidad = "m/s"
character(len = 6), PARAMETER:: Aceleracion = "m/s**2"
character(len = 1), PARAMETER:: Tiempo = "s"
character(len = 1), PARAMETER:: distancia = "m"
WRITE(*,*)"La ecuacion de la distancia es : x = x_0+(v_0*t)+ (at**2)/2"
WRITE(*,*)"Escribe los valores de la v inicial, aceleracion, tiempo y d.inicial"
READ(*,*)v_0,a,t,x_0

x = x_0+(v_0*t)+(a*(t**2))/2
WRITE (*,*)"la velocidad inicial es de ",v_0,Velocidad
WRITE (*,*)"la aceleracion es de ",a,Aceleracion
WRITE (*,*)"El tiempo es de ",t,Tiempo
WRITE (*,*)"la distancia inical es de ",x_0,distancia
WRITE (*,*)"la distancia final es de ",x,distancia


PAUSE

END PROGRAM ec_de_distancia
