## **Descripcion**
Find the flag being held on this server to get ahead of the competitionhttp://wily-courier.picoctf.net:60527/
## **Solucion**
Se hizo uso del inspector del mozilla y uso de la terminal
picoCTF{r3j3ct_th3_du4l1ty_8b13f07}

## **Notas adicionales**
uso de inspector
-se elige network, escojes el que sea azul o rojo, escogi el azul, tienes que configurar el post 200,
entrando a block, ahi lo cambias a HEAD, y en el apartado headers ahi encontraras la bandera
-Terminal,  ahi se usa este comando 
curl -I  HEAD  http://wily-courier.picoctf.net:60527/index.php
y nos lanzara la bandera.

se hizo mencion de otra forma pero nuevamente me guie mejor con estos dos..

## **Referencias**
picoCTF 2021 writeup [11] - Web - GET aHEAD
https://www.youtube.com/watch?v=oiZk0tIkR48&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=11