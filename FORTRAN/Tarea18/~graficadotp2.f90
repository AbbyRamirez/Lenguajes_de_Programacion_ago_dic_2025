PROGRAM Graficadotp
IMPLICIT NONE
REAL::angulo,x,y,v0,t,c2,x1,y1,c
Integer::control
WRITE(*,*)"escriba el  ngulo y velocidad del lanzamiento"
READ(*,*)angulo,v0
WRITE(*,*)"escriba la posici¢n inicial en (x,y)"
READ(*,*)x1,y1
c = x1/v0
OPEN(UNIT = 410, FILE = "P2c4b.txt", STATUS = "NEW", ACTION = "WRITE")
DO control = c,500,10
   c2= control  !t es en centesimas  de segundo
  t = c2/100
  x = x1+v0*COS(angulo*(3.14/180))*t
  y = y1+(v0*SIN(angulo*(3.14/180))*t) -  (4.9*(t**2))
Write(410,*)x, y
end do
Pause
END PROGRAM graficadotp


