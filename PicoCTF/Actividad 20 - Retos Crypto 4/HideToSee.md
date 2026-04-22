## **Descripcion**
How about some hide and seek heh?Look at this image [here](https://artifacts.picoctf.net/c/238/atbash.jpg).
## **Solucion**
picoCTF{atbash_crack_8a0feddc}

## **Notas adicionales**

Paso 1. Se descargo el contenido.
Paso 2. - Extraemos el texto dentro de la imagen con `steghide` y abrimos la imagen

`sudo apt install steghide steghide --extract -sf atbash.jpg`
Paso 3.- mostramos el texto encriptado dentro del archivo de texto que extragimos

`cat encrypted.txt`
Paso 4. Nos saldra algo asi 

`krxlXGU{zgyzhs_xizxp_8z0uvwwx}

Paso 5. En cyberchef escogemos abatsh cipher y pegamos lo anterior y se obtendra la bandera.
## **Referencias**
https://gchq.github.io/CyberChef/