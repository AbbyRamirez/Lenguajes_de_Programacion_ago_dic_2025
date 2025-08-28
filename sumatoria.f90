PROGRAM Sumatoria
REAL:: suma, sumane, sumap,n
INTEGER:: cneg,cpos,control
LOGICAL::bandera
WRITE(*,*)"sumatoria de numeros"
bandera = .true.
suma = 0
sumane = 0
sumap = 0
cneg = 0
cpos = 0

DO WHILE (bandera .eqv. .true.)
 WRITE(*,*)"escriba el numero a sumar"
 READ(*,*)n
 suma = suma + n
 if (n < 0) THEN
  sumaneg = sumaneg + n
  cneg = cneg +1
  end if
  if(n >= 0) THEN
  sumapos = sumapos + n
  cpos = cpos+1
 end if
 WRITE(*,*)"¨Desea seguir sumando?, 1 para terminar?"
 READ(*,*)control
 if(control==1) THEN
 bandera =.FALSE.
 else
 bandera = .TRUE.
 end if
END DO
WRITE(*,*)"la suma de negativos",sumaneg
WRITE(*,*)"la suma de positivos",sumapos
WRITE(*,*)"la cantidad de negativos",cneg
WRITE(*,*)"la cantidad de positivos",cpos
WRITE(*,*)"la suma TOTAL",suma
PAUSE
END PROGRAM Sumatoria





