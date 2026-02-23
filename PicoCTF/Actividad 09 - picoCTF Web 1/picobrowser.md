## **Descripcion**
This website can be rendered only by picobrowser, go and catch the flag!http://fickle-tempest.picoctf.net:61434
## **Solucion**
Se utilizo la terminal de linux
picoCTF{p1c0_s3cr3t_ag3nt_fba5c48f}
## **Notas adicionales**
Se utilizo esta serie de comando para obtener la bandera
curl -s http://fickle-tempest.picoctf.net:61434/flag -H "User-Agent: picobrowser" | grep picoCTF
## **Referencias**
picoCTF 2019 writeup [5] - Web - picobrowser
https://www.youtube.com/watch?v=9d6-N0oJwOk&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=5