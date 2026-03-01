## **Descripcion**
Who doesn't love cookies? Try to figure out the best one.http://wily-courier.picoctf.net:59415/
## **Solucion**
se hizo uso de cookie editor y la terminal
picoCTF{3v3ry1_l0v3s_c00k135_a4dadb49}

## **Notas adicionales**
En caso de cookie editor fue la configuracion name con value 18,
en caso de terminal se utilizo este codigo for i in {0..20}; do curl -s http://wily-courier.picoctf.net:59415/check  -H "Cookie: name=$i"; done | grep picoCTF ahi nos lanzo la bandera.

El maestro utilizo mas metodos,pero en mi caso decidi quedarme con estos dos.
## **Referencias**
picoCTF 2021 writeup [12] - Web - Cookies
https://www.youtube.com/watch?v=LseQ-XWCXVo&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=12
