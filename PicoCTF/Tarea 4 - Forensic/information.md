## **Descripcion**
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://challenge-files.picoctf.net/c_wily_courier/76e95e3e6ee69b4f82b3cea25051f5a9a5918b57809a1f90b29b06b776c73bc7/cat.jpg)
## **Solucion**
picoCTF{the_m3tadata_1s_modified}

## **Notas adicionales**

 ## Paso 1: 
 Se descarga el archivo 
 Paso 2:
 Usamos este comando para saber mas
```
file cat.jpg
```
Paso 3: usamos hexeditor
```
hexeditor  cat.jpg
```

nos saldra una serie de numeros hexa y comentarios donde viene licence ahi que tomar ese codigo
```
license r df:resource='cGlb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```
Paso 4 utilicemos este comando y ahi nos dara la bandera..
```
echo -n cGlb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d
```
