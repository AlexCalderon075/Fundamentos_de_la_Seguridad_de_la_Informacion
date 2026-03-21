picoCTF{h4un71ng_p457_0a710765} 

## **Descripcion**
Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/212/disk.flag.img.gz)
## **Solucion**
picoCTF{h4un71ng_p457_0a710765} 

## **Notas adicionales**
Paso 1: Descargamos y descomprimimos


```
wget https://artifacts.picoctf.net/c/136/disk.flag.img.gz
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
    Usamos `fls` para listar los archivos., se enfoca en la partición que comienza en el sector **411648**.
    
    fls -o 411648 disk.flag.img
Paso 4:
Al explorar el directorio `root`, se encuentran dos archivos relevantes: `flag.txt` (que parece borrado) y `flag.txt.enc` (archivo cifrado)

Usamos `icat` para extraer el contenido del inodo correspondiente a `flag.txt.enc` y guardarlo localmente.

```
icat -o 411648 disk.flag.img 172 > flag.txt.enc
```
Paso 5:
se encuentra un comando de OpenSSL que revela la clave: `unbreakablepassword1234567`

Paso 6:
**Ejecutar OpenSSL para descifrar:**

```
openssl aes-256-cbc -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
```
Paso 7:
Finalmente, se visualiza el contenido del archivo resultante.
    cat flag.txt
