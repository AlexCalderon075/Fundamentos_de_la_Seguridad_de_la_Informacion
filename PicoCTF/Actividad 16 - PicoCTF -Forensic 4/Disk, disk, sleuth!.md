## **Descripcion**
Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image.[dds1-alpine.flag.img.gz](https://challenge-files.picoctf.net/c_wily_courier/a118330a1c5e12f3b59fc45a75b8838700482f89c8ea71a28aa1bd66c7ba3968/dds1-alpine.flag.img.gz)

## **Solucion**
Se hizo uso de la terminal 
picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}
## **Notas adicionales**

#### Paso 1
Se descargo el archivo -d dds1-alpine.flag.img.gz

#### Paso 2
Se utilizo este comando para extraer el archivo
gzip -d dds1-alpine.flag.img.gz 

#### Paso 3
Se utilizo  para darnos la bandera.
strings dds1-alpine.flag.img  | grep pico