 PROGRAM EcuacionCuadratica
 Character(len = 1), PARAMETER:: imaginario = "i"
 REAL:: a,b,c,x1,x2,d,r
 WRITE(*,*)"Escribe los coeficientes a.b.c de la ecuaci¢n respectivamente"
 READ(*,*)a,b,c
 d = (b**2) - (4*a*c)
 IF ( d == 0) THEN
    WRITE(*,*)" Las ra¡ces son iguales y reales"
    x1 = ((-1*b)+(d**0.5))/(2*a)
    x2 = ((-1*b)-(d**0.5))/(2*a)
     WRITE(*,*)"Las raices son: " ,x1,x2
 ELSE IF (d > 0) THEN
    WRITE(*,*)" Las ra¡ces son diferentes y reales"
    x1 = ((-1*b)+(d**0.5))/(2*a)
    x2 = ((-1*b)-(d**0.5))/(2*a)
    WRITE(*,*)"Las raices son: " ,x1,x2
ELSE
    WRITE(*,*)" Las ra¡ces son conjugadas e imaginarias"
    r = (-1*b)/(2*a)
    x1 = ((-1*d)**0.5)/(2*a)
    WRITE(*,*)"Las raices son: ", r, "+" ,x1, "," ,r, "-" ,x2
    END IF
    PAUSE
    END PROGRAM EcuacionCuadratica
 
