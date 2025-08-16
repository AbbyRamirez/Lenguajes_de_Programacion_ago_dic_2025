PROGRAM COCASYB
IMPLICIT NONE
REAL::co,ca,h,y,b,a
WRITE(*,*)"INGRESE CATETOS (primero co y luego ca) "
READ(*,*)co,ca
h = ((co**2)+(ca**2))**0.5
b = ATAN(co/ca)
y = 3.14-b
a = (co*ca)/2
WRITE(*,*)"La hipotenusa es ",h
WRITE(*,*)"Los angulos y b son respectivamente ",y,b
WRITE(*,*)"EL area es: ",a
PAUSE
END PROGRAM COCASYB
