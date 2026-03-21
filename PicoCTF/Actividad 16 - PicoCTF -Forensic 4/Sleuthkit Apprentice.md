## **Descripcion**
Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/136/disk.flag.img.gz)
## **Solucion**
picoCTF{by73_5urf3r_3497ae6b}
## **Notas adicionales**

Paso 1: Descargamos y descomprimimos


```
wgethttps://artifacts.picoctf.net/c/136/disk.flag.img.gz
gunzip -d disk.flag.img.gz
```

Paso 2:
Para ver la estructura de las particiones dentro de la imagen, se utiliza la herramienta `mmls` (de la suite Sleuth Kit).

Listar particiones
```
    mmls disk.flag.img
```

Paso 3:
Explorar el contenido de la partición:**
    Usamos `fls` para listar los archivos., se enfoca en la partición que comienza en el sector 360448.
    
    fls -o 360448 disk.flag.img
Paso 4:
Ahora usaremos este
fls -r -o 360448 disk.flag.img | grep -i flag
Nos saldra otros dos archivos

Paso 5: por ultimo viendo los dos archivos ya mencionados 
Se aplicara este comando
icat -o  360448 disk.flag.img 2371 
Ahi nos dara la bandera