PROGRAM Tparabolico
IMPLICIT NONE
REAL:: vo, xmax,ymax,i,vuelo
WRITE(*,*)"Inserte una velocidad inicial"
READ (*,*)vo
DO i = 1,90,1
  ymax = ((Vo**2)*(SIN(i*(3.1416/180))**2))/9.81
  vuelo = (19.62/ymax)**0.5
  xmax = (vo*COS(i*(3.1416/180)))*vuelo
  WRITE(*,*)"angulo",i, "   Altura M xima ",ymax, "  Alcance M ximo",xmax
  END DO
PAUSE
END PROGRAM Tparabolico


