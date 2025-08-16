PROGRAM pregunta
IMPLICIT NONE
INTEGER::i1,i2,i3
REAL:: a1= 2.4, a2

i1 = a1
i2 = INT(a1*i1)
i3 = NINT(a1*i1)
a2 = a1**i1

WRITE(*,*) i1,i2,i3,a2
PAUSE
END PROGRAM pregunta

