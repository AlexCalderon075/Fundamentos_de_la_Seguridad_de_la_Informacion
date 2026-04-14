## **Descripcion**
I found this cipher in an old book. Can you figure out what it says? Connect with nc fickle-tempest.picoctf.net 51868.
## **Solucion**
picoCTF{b311a50_0r_v1gn3r3_c1ph3rdAAB11d9}

## **Notas adicionales**
Paso 1. Se conecto a nc fickle-tempest.picoctf.net 51868

Paso 2. Nos sale una serie de texto.

Paso 3. Usemos cyberchef con vigere decode.

Paso 4. Nos pedida la key, ahi ahora utilicemos la pagina vigenere solver

Paso5.Pegamos nuestro serie de texto,los valores los dejamos asi por defecto.

Paso 6. Nos da como key "flag", regresamos a cyberchef ponemos esa key y en la salida ahi encontraremos la bandera..
## **Referencias**
https://gchq.github.io/CyberChef/
https://www.guballa.de/vigenere-solver
picoCTF 2019 writeup [37] - Cryptography - la cifra de - https://www.youtube.com/watch?v=ACVSzc-wH8o&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=37