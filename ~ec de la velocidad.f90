PROGRAM Ec_de_velocidad

REAL:: v , v_0, a, t
character(len = 3), PARAMETER:: Velocidad = "m/s"
character(len = 6), PARAMETER:: Aceleracion = "m/s**2"
character(len = 1), PARAMETER:: Tiempo = "s"
WRITE(*,*)"La ecuacion de la velocidad es : V = v_0 + at"
v_0 = 5.
a = 3.
t = 4.

v = v_0 + a*(t**2)
WRITE (*,*)"la velocidad inicial es de ",v_0,Velocidad
WRITE (*,*)"la aceleracion es de ",a,Aceleracion
WRITE (*,*)"El tiempo es de ",t,Tiempo
WRITE (*,*)"la velocidad final es de ",v,Velocidad


PAUSE

END PROGRAM Ec_de_velocidad
