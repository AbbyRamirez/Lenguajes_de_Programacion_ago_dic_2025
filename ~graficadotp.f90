PROGRAM Graficadotp
IMPLICIT NONE
REAL::angulo,x,y,v0,t,c2
Integer::control
WRITE(*,*)"escriba el  ngulo y velocidad del lanzamiento"
READ(*,*)angulo,v0
OPEN(UNIT = 410, FILE = "Pc5.txt", STATUS = "NEW", ACTION = "WRITE")
DO control = 10,40,1
   c2= control  !t es en centesimas  de segundo
  t = c2/100
  x = v0*COS(angulo*(3.14/180))*t
  y = (v0*SIN(angulo*(3.14/180))*t) -  (0.5*9.81*(t**2))
Write(410,*)x, y
end do
Pause
END PROGRAM graficadotp
  

