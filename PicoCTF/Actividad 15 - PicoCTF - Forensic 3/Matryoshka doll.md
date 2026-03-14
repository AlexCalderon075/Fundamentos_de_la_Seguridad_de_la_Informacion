## **Descripcion**
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one?Image: [dolls.jpg](https://challenge-files.picoctf.net/c_wily_courier/b236ead0cb75e5a4b8b8d5aa15c6cc80369b3ea778f1a116911f23d774a92bf4/dolls.jpg)
## **Solucion**

picoCTF{LL9lb1dR4QbGe4l4iWCvGq9pdtwt7392}
## **Notas adicionales**
- verificamos en tipo de archivo y veremos que es un imagen jpg

`file dolls.jpg` 

- verificamos si tiene contenido anexo con `binwalk`, hay un archivo .zip dentro

`binwalk dolls.jpg`  

- extraemos el archivo .zip , se crea un diectorio `base_images` y dentro de el hay otra imagen

`unzip dolls.jpg`  

- repetimos el proceso de extracción hasta obtener la bandera

## **Referencias**
picoCTF 2021 writeup [26] - Forensic - Matryoshka doll - https://www.youtube.com/watch?v=NkbtA7x5aVI&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=26
https://es.wikipedia.org/wiki/Matrioshka