## **Descripcion**
There's something in the [building](https://challenge-files.picoctf.net/c_fickle_tempest/c0eec6af0f04316e2bdc4a9f095afd0e2d0121f5e543dbc4a65bb0038d72a993/buildings.png). Can you retrieve the flag?
## **Solucion**
picoCTF{h1d1ng_1n_th3_b1t5}
## **Notas adicionales**
Se hizo uso de la pagina Steganography Online, se agrego la imagen la decode y en message nos salio la bandera

Otra forma es uso de la consola.
se instalo zsteg, despues ingresamos este comando y nos dara la respuesta 
┌──(kali㉿kali)-[~/Downloads]
└─$ zsteg -a buildings.png | grep pico
## **Referencias**

picoCTF 2021 writeup [18] - Forensic - What Lies Within https://www.youtube.com/watch?v=bFUB-USG3sw
https://latam.kaspersky.com/resource-center/definitions/what-is-steganography