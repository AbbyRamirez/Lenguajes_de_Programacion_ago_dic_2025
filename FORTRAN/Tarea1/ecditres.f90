PROGRAM Ecditres
REAL:: v , v_0, a, t,x,x_0
character(len = 3), PARAMETER:: Velocidad = "m/s"
character(len = 6), PARAMETER:: Aceleracion = "m/s**2"
character(len = 1), PARAMETER:: Tiempo = "s"
character(len = 1), PARAMETER:: distancia = "m"
WRITE(*,*)"La ecuacion de la distancia es : x = x_0+v*t-(a*(t**2)/2)"
a = 3.
t = 4.
x_0 = 56.
v = 35.
t= 8.
x = x_0 + v*t -(a*(t**2)/2)
WRITE (*,*)"la aceleracion es de ",a,aceleracion
WRITE (*,*)"El tiempo es de ",t,Tiempo
WRITE (*,*)"la distancia inical es de ",x_0,distancia
WRITE (*,*)"la velocidad es de ",v,Velocidad
WRITE (*,*)"la distancia final es de ",x,distancia


PAUSE

END PROGRAM Ecditres
