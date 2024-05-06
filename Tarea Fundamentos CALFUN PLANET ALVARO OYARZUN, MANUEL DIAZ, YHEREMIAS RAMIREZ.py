#IMPORTAMOS RANDOM Y TIME


import random;
import time;

###########DEFINIMOS VARIABLES!##########


acumulao=0;
ultimotexto="";
petalos=("ME QUIERE MUCHO", "ME QUIERE POQUITO", "ME QUIERE NADA");

##########MENÚ INICIAL DE JUEGO


print ("BIENVENIDOS A CALFÚN PLANET!!\n");
time.sleep(1);
print ("JUEGATE TU FORTUNA AMOROSA!\nSABRÁS SI TE QUIEREN O NO!!\n");

start=input("Presione enter para jugar!!");
if (start==""):
    print ("");
else:
    print ("");

##########CICLO DE TEXTO RANDOM(DONDE OCURRE LA MAGIA)##########


for i in range(5):
    ultimotexto=random.choice(petalos);
    print (f"{ultimotexto}\n");
    time.sleep(1);

###########COMANDO IF PARA MENSAJE FINAL PERSONALIZADO############


if (ultimotexto==("ME QUIERE MUCHO")):
    print("Felicidades, ¡¡¡¡¡TE QUIERE MUCHOO!!!!!\n                      MUCHO!!!\n                      MUCHO!!!\n                      MUCHO!!!\n");
    time.sleep(2);
elif (ultimotexto==("ME QUIERE POQUITO")):
    print("TE QUIERE POQUITO, TE FALTA MEWING!!!!!!\n");
    time.sleep(2);
elif (ultimotexto==("ME QUIERE NADA")):
    print("NO TE QUIERE NADA, GG, NA Q HACERLEE!!\n");
    time.sleep(2);




##########TRABAJO HECHO POR ALVARO OYARZÚN, MANUEL DÍAZ Y YHEREMIAS RAMÍREZ
##########PROFESOR: FRANCISCO CALFÚN    