PROGRAM HipoY
IMPLICIT NONE
REAL::co,ca,h,y,a
WRITE(*,*)"INGRESE LA HIPOTENUSA Y EL ANGULO Y (en radianes pls)"
READ(*,*)h,y
co = SIN(y)*h
ca = COS(y)*h
a = (co*ca)/2
WRITE(*,*)"EL cateto opuesto es: ",co
WRITE(*,*)"EL cateto adyacente es: ",ca
WRITE(*,*)"EL area es: ",a
PAUSE
END PROGRAM HipoY
