PROGRAM Energia
REAL,PARAMETER::g = 9.81
character(len = 1), PARAMETER:: Joules = "J"
REAL:: h,m,v,k,u,E
WRITE(*,*)"Escriba el valor de la velocidad, altura, masa respectivamente"
READ (*,*) v,h,m
k = (m*(v**2))/2
u = m*g*h
E = u+k
WRITE(*,*)"La energ¡a cin‚tica es: ",k,Joules
WRITE(*,*)"La energ¡a potencial es: ",u, Joules
WRITE(*,*)"La energ¡a Mec nica es: ",E, Joules
PAUSE
END PROGRAM Energia
