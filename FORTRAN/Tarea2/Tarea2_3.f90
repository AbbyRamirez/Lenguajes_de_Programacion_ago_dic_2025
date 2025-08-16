PROGRAM ec_de_velocidad_al_cuadrado
IMPLICIT NONE
REAL:: vd , v_0, a, x ,x_0
character(len = 3), PARAMETER:: Velocidad = "m/s"
character(len = 6), PARAMETER:: Aceleracion = "m/s**2"
character(len = 1), PARAMETER:: distancia = "m"
WRITE(*,*)"La ecuacion de la velocidad cuadrada es : v*2 = v_0*2+ 2*a*(x-x_0)"
WRITE(*,*)"Escribe la v.Inicial, aceleracion, distancia y distancia inicial"
READ(*,*),v_0,a,x,x_0

vd = (v_0**2)+(2*a*(x-x_0))


WRITE (*,*)"la velocidad inicial es de ",v_0,Velocidad
WRITE (*,*)"la aceleracion es de ",a,Aceleracion
WRITE (*,*)"la distancia inical es de ",x_0,distancia
WRITE (*,*)"la distancia final es de ",x,distancia
WRITE (*,*)"la velociad cuadrada es de ",vd,velocidad
PAUSE
END PROGRAM ec_de_velocidad_al_cuadrado
