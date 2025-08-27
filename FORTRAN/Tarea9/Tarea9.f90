PROGRAM Calcbasica
REAL:: a,b,r
INTEGER::control
WRITE(*,*)"da los valores para a y b"
READ(*,*) a,b
WRITE(*,*)"Seleccione su operaci¢n: 1;SUMA  2;RESTA  3;PRODUCTO  4;DIVISION  5;POTENCIA"
READ(*,*)control
IF(control == 1)THEN
r = a + b
WRITE(*,*)"EL RESULTADO ES: ",r
END IF
IF(control == 2)THEN
r = a - b
WRITE(*,*)"EL RESULTADO ES: ",r
END IF
IF(control == 3)THEN
r = a * b
WRITE(*,*)"EL RESULTADO ES: ",r
END IF
IF(control == 4)THEN
 if(b==0)THEN
   WRITE(*,*)"error"
 Else
  r = a / b
  WRITE(*,*)"EL RESULTADO ES: ",r
  END IF
END IF

IF(control == 5)THEN
if(a<0)THEN
   WRITE(*,*)"error"
  else
r = a ** b
WRITE(*,*)"EL RESULTADO ES: ",r
END IF
END IF
PAUSE
END PROGRAM Calcbasica

