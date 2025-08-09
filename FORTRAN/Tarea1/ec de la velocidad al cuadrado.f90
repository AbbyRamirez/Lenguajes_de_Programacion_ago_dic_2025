PROGRAM ec_de_velocidad_al_cuadrado

REAL:: v , v_0, a, t
character(len = 3), PARAMETER:: Velocidad = "m/s"
character(len = 6), PARAMETER:: Aceleracion = "m/s**2"
character(len = 1), PARAMETER:: distancia = "m"
WRITE(*,*)"La ecuacion de la velocidad cuadrada es : v*2 = v_0*2+ 2*a*(x-x_0)"
v_0 = 5.
a = 3.
x = 10.
x_0 = 4.
v2 = (v_0**2)+(2*a*(x-x_0))


WRITE (*,*)"la velocidad inicial es de ",v_0,Velocidad
WRITE (*,*)"la aceleracion es de ",a,Aceleracion
WRITE (*,*)"la distancia inical es de ",x_0,distancia
WRITE (*,*)"la distancia final es de ",x,distancia
WRITE (*,*)"la velociad cuadrada es de ",v2,velocidad


PAUSE

END PROGRAM ec_de_velocidad_al_cuadrado
