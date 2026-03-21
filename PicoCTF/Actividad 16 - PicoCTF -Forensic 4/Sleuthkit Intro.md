## **Descripcion**
Download the disk image and use `mmls` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory. [Download disk image](https://artifacts.picoctf.net/c/164/disk.img.gz) Access checker program: `nc saturn.picoctf.net 57717`
## **Solucion**
picoCTF{mm15_f7w!}

## **Notas adicionales**

Paso 1:  
Descargamos la imagen del disco (vía `wget` o el enlace del reto) y procedemos a descomprimirla, ya que viene en formato `.gz`.

```
wget https://artifacts.picoctf.net/c/164/disk.img.gz
gunzip disk.img.gz
```
Paso 2:
Utilizamos la herramienta `mmls` de **The Sleuth Kit**. Esta herramienta nos permite ver el diseño del sistema de archivos sin necesidad de montar la imagen.

```
mmls disk.img
```

Paso 3:
Utilizamos la herramienta `mmls` de **The Sleuth Kit**. Esta herramienta nos permite ver el diseño del sistema de archivos sin necesidad de montar la imagen.

```
mmls disk.img
```

**Resultado esperado en consola:** Al ejecutar el comando, verás una tabla similar a esta: | Slot | Start | End | Length | Description | | :--- | :--- | :--- | :--- | :--- | | 000 | 0000000000 | 0000000000 | 0000000001 | Primary Table | | 001 | 0000000000 | 0000002047 | 0000002048 | Unallocated | | 002 | **0000002048** | 0000204799 | **0000202752** | **Linux (0x83)** |

Paso 4:
En la salida del comando anterior, buscamos la fila que indica **Linux (0x83)**.

- **Sector de inicio:** 2048
    
- **Tamaño (Length):** 202752 (Este es el valor que nos pide el reto).
    

Paso 5:
Nos conectamos al servidor de picoCTF mediante el comando proporcionado en la descripción del reto (usualmente vía `nc` o `socat`).

Bash

```
`nc saturn.picoctf.net 57717`
```

Cuando el servidor pregunte: _"What is the size of the Linux partition in the given disk image?"_, ingresamos el valor de la columna **Length**:

> **Input:** `202752`
## **Referencias**
  
picoCTF 2021 writeup [31] - Forensic - Sleuthkit Intro - https://www.youtube.com/watch?v=NrwL5YnC4Gk&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=31