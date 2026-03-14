## **Descripcion**
We found this file. Recover the flag.[tunn3l_v1s10n](https://challenge-files.picoctf.net/c_wily_courier/626df9feed926c1e1280804f5d87fde5576e266ff250a819a5528b0471b0f3f7/tunn3l_v1s10n)
## **Solucion**
Se hizo uso de la terminal con el hexeditor
picoCTF{qu1t3_a_v13w_2020}
## **Notas adicionales**
- verificamos el tipo de archivo, pero dice es `data`

`file tunn3l_v1s10n`

- vemos los metadatos y ahí verificamos que es un `bmp` que se corrompio

`exiftool unn3l_v1s10n`


- Un archivo BMP tiene un encabezado de 12 bytes, lo visualizamos

`xxd -l 12 -g 1 tunn3l_v1s10n` 

- luego vienen 40 bytes adicionales de información del encabezado, los visualizamos

`xxd -l 52 -g 1 tunn3l_v1s10n`

- De esos 40 bytes, los primeros 4 indican el tamaño de la información del encabezado que es 40 (28 en ex), lo ponemos en el offset 0xE, visualizamos para verificar

`xxd -s 0xc -l 4 tunn3l_v1s10n 0000000c: 0000 bad0   xxd -s 0xc -l 4 tunn3l_v1s10n 0000000c: 0000 2800`  

- Luego los últimos 4 bytes del encabezado, indican el offest donde inician los datos, que es 40 (28 en hex) eso lo ponemos en el offset 0xA, y verificamos

`xxd -s 0x8 -l 4 tunn3l_v1s10n 00000009: 0000 bad0     xxd -s 0x8 -l 4 tunn3l_v1s10n 00000008: 0000 2800` 

- Abrimos el archivo y nos damos cuenta que es ancho pero poco alto
- Modificamos la altura en el offset 0x16 y le ponemos la misma altura que aparece en el offset 0x12 para hacer la imagen simétrica, y verificamos

`xxd -s 0x14 -l 4 tunn3l_v1s10n 00000014: 0000 3201       xxd -s 0x14 -l 4 tunn3l_v1s10n 00000014: 0000 6e04`  
exiftool tunn3l_v1s10n.bpm
ExifTool Version Number         : 13.36
File Name                       : tunn3l_v1s10n.bpm
Directory                       : .
File Size                       : 2.9 MB
File Modification Date/Time     : 2026:03:14 01:55:50-04:00
File Access Date/Time           : 2026:03:14 01:56:11-04:00
File Inode Change Date/Time     : 2026:03:14 01:55:50-04:00
File Permissions                : -rw-rw-r--
File Type                       : BMP
File Type Extension             : bmp
MIME Type                       : image/bmp
BMP Version                     : Windows V3
Image Width                     : 1134
Image Height                    : 1088
Planes                          : 1
Bit Depth                       : 24
Compression                     : None
Image Length                    : 2893400
Pixels Per Meter X              : 5669
Pixels Per Meter Y              : 5669
Num Colors                      : Use BitDepth
Num Important Colors            : All
Image Size                      : 1134x1088
Megapixels                      : 1.2
-Antes de abrir el archivo se pasa .bpm para poder abrirlo y ver la bandera
## **Referencias**
 [https://www.donwalizerjr.com/understanding-bmp/](https://www.donwalizerjr.com/understanding-bmp/ "https://www.donwalizerjr.com/understanding-bmp/")
picoCTF 2021 writeup [27] - Forensic - tunn3l v1s10n - https://www.youtube.com/watch?v=1ucy2G1PIh4&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=27
 