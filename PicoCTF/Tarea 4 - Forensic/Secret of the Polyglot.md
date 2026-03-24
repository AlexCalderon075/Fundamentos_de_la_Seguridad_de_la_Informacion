tf## **Descripcion**
The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file? Download the suspicious file [here](https://artifacts.picoctf.net/c_titan/99/flag2of2-final.pdf).
## **Solucion**
picoCTF{f1u3n7_1n_pn9_&_pdf_2a6a1ea8}
## **Notas adicionales**

Paso 1: Descargarmos el archivo y lo abrimos
```
┌──(kali㉿kali)-[~/Documents/Fundamentos8A/sotp]
└─$ open flag2of2-final.pdf


```
cuando se abra veras la mitad de  bandera ahora conseguiremos completarla

Paso 2:
usaremos este comando
```
┌──(kali㉿kali)-[~/Documents/Fundamentos8A/sotp]
└─$ mv flag2of2-final.pdf flag2of2-final.png     
```
esto hara un nuevo archivos, usaras de nuevo open pero sera `open flag2of2-final.png`  
ahi estara la otra parte para completar la bandera.