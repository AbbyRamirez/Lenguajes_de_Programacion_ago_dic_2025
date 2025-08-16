PROGRAM Hipob
IMPLICIT NONE
REAL::co,ca,h,b,a
WRITE(*,*)"INGRESE LA HIPOTENUSA Y EL ANGULO B (en radianes pls)"
READ(*,*)h,b
co = SIN(b)*h
ca = COS(b)*h
a = (co*ca)/2
WRITE(*,*)"EL cateto opuesto es: ",co
WRITE(*,*)"EL cateto adyacente es: ",ca
WRITE(*,*)"EL area es: ",a
PAUSE
END PROGRAM Hipob
