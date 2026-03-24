
## **Descripcion**
Every file gets a flag. The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/260/flag.png).
## **Solucion**
picoCTF{hiddinng_An_imag3_within_@n_ima9e_ad9f6587}

## **Notas adicionales**

Paso 1:
Aplicamos este comando
```
(kali㉿kali)-[~/Documents/Fundamentos8A/hm]
└─$ binwalk -e flag.png  
```

Paso 2: nos a guardada dos archivos
```
┌──(kali㉿kali)-[~/Documents/Fundamentos8A/hm]
└─$ ls
flag.png  _flag.png.extracted
```
Paso 3:  entramos a la carpeta _flag_ despues vemos que habra mas archivos
```
┌──(kali㉿kali)-[~/Documents/Fundamentos8A/hm]
└─$ cd _flag.png.extracted                                                   
──(kali㉿kali)-[~/Documents/Fundamentos8A/hm/_flag.png.extracted]
└─$ ls
29  29.zlib  9B3B.zip  secret
```
Paso 3:
Ahora entraremos a la carpeta secret,viendo el archivo solo nos tocara aplicar open flag.png y ahi estara la bandera 
```
┌──(kali㉿kali)-[~/Documents/Fundamentos8A/hm/_flag.png.extracted]
└─$ cd secret             
┌──(kali㉿kali)-[~/…/Fundamentos8A/hm/_flag.png.extracted/secret]
└─$ ls
flag.png
```
