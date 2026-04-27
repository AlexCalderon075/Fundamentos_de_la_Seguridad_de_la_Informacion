## **Descripcion**
In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding!The source code for this vault is here: [VaultDoor5.java](https://challenge-files.picoctf.net/c_fickle_tempest/f2e90d844f6e64092bc1a611c16d52a832e0f2cb856991bc9fa205bcd0cd31bd/VaultDoor5.java)
## **Solucion**
picoCTF{c0nv3rt1ng_fr0m_ba5e_64_4bb22721}
## **Notas adicionales**
paso 1. - Examinamos el código fuente en Java que se nos da
Paso2.La flag esta codificada con : URL Encode y Base64 hay que revertilos
Nota: El maestro utilizo 3 metodos yo nuevamente utilice 1.

Paso 3. en esta parte de codigo
```
JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTM0JTYyJTYyJTMyJTMyJTM3JTMyJTMx
```
Lo tomamos vamos cyberchef y usar la recetas: From Base64 y URL Decode
y obtendremos la bandera.
## **Referencias**
[https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/ "https://gchq.github.io/CyberChef/")
[picoCTF 2019 writeup [51] - Reverse Engineering - vault-door-5](https://www.youtube.com/watch?v=ZB0nUEEDyBQ&pp=ygUUcGljb2N0ZiB2YXVsdCBkb29yIDU%3D "picoCTF 2019 writeup [51] - Reverse Engineering - vault-door-5") 
