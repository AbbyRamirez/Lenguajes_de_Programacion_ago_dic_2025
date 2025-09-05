PROGRAM Acromatica
IMPLICIT NONE
REAL,PARAMETER:: N1 = 1.4702, N2 = 1.4624, NA = 1
REAL:: rads,idr1,idr2,abcromatica
INTEGER::control
DO control = 1, 90, 1
  rads =  control*(3.1416/180)
  idr1 = (NA/N1)*SIN(rads)
  idr2 = (NA/N2)*SIN(rads)
  abcromatica = idr2-idr1
  WRITE(*,*)"angulo",control, "   aberracion cromatica ",abcromatica
  END DO
PAUSE
END PROGRAM Acromatica


