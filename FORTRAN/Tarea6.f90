  PROGRAM oplog
  REAL::a,b
  WRITE(*,*)"Asignar n£meros a A y B"
  READ(*,*)a,b
  IF(((a>0).and.(b>0)).and.(a == b))THEN
  WRITE(*,*)"Datos iguales y positivos"
  END IF
  IF(((a>0).and.(b>0)).and.(a /= b))THEN
  WRITE(*,*)"Datos diferentes y positivos"
  END IF
  IF(((a<0).and.(b<0)).and.(a == b))THEN
  WRITE(*,*)"Datos iguales y negativos"
  END IF
  IF(((a<0).and.(b<0)).and.(a /= b))THEN
  WRITE(*,*)"Datos diferentes y negativos"
  END IF
  IF((a<0).OR.(b<0))THEN
  WRITE(*,*)"Dato negativo"
  END IF
  PAUSE
  END PROGRAM oplog
