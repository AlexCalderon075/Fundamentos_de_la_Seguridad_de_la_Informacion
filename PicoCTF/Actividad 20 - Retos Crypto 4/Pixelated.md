## **Descripcion**
I have these 2 images, can you make a flag out of them?[scrambled1.png](https://challenge-files.picoctf.net/c_wily_courier/fd911d04c960ddc4effdf884e8cc954b91e1936eb4c1bdee81a39f7b16a5e465/scrambled1.png) [scrambled2.png](https://challenge-files.picoctf.net/c_wily_courier/fd911d04c960ddc4effdf884e8cc954b91e1936eb4c1bdee81a39f7b16a5e465/scrambled2.png)
## **Solucion**
picoCTF{8cdf93c3}
## **Notas adicionales**
Nota: el maestro lo hizo de 2 formas lo hice yo con una forma proporcinado a su codigo de python.

Paso1. Se descarga las 2 imagenes.
Paso 2. Con el codigo proporcionado del maestro
`from PIL import Image import numpy as np 
imagen1 = np.asarray( Image.open('scrambled1.png') ) 
imagen2 = np.asarray( Image.open('scrambled2.png') )
data = imagen1 + imagen2 nueva = Image.fromarray(data) nueva.save("out.png", "PNG")`
Paso 3. Se crear otra imagen nueva con el nombre out.png y la abrimos y se encuentra la bandera.
## **Referencias**
[picoCTF 2021 writeup [43] - Cryptography - Pixelated](https://www.youtube.com/watch?v=zWU6MV8dQQ4&pp=ygURcGljb2N0ZiBwaXhlbGF0ZWQ%3D "picoCTF 2021 writeup [43] - Cryptography - Pixelated") 