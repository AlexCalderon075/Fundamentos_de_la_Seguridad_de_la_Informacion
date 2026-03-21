## **Descripcion**
Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download disk image](https://artifacts.picoctf.net/c/70/disk.img.gz)
- Remote machine: `ssh -i key_file -p 58601 ctf-player@saturn.picoctf.net`
## **Solucion**
picoCTF{k3y_5l3u7h_b5066e83}
## **Notas adicionales**

Paso 1:

Primero, se descarga y descomprime el archivo de la imagen de disco proporcionada por el reto.


```
# Descargar la imagen
wget https://artifacts.picoctf.net/c/70/disk.img.gz

# Descomprimir el archivo .gz
gunzip -d disk.img.gz
```

Paso 2:
mmls disk.img

Paso 3:
Listar archivos en la raíz de la partición 
fls -o 206848 disk.img

Listar contenido de la carpeta /root 
fls -o 206848 disk.img 470

Paso 4:
Extraer la llave  y guardarla como 'key_file' icat -o 206848 disk.img 2345 > key

Paso 5:
chmod 400 key_file

Paso 6:
`ssh -i key_file -p 58601 ctf-player@saturn.picoctf.net`

Paso 7:
ls 
cat flag.txt
Obtenemos la bandera

## **Referencias**
  
picoCTF 2021 writeup [32] - Forensic - Operation Oni - https://www.youtube.com/watch?v=PVeV-S3Zbqk&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=32