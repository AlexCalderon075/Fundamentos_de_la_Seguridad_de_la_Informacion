## **Descripcion**
How about some hide and seek? Download this file [here](https://artifacts.picoctf.net/c_titan/6/unknown.zip).
## **Solucion**
picoCTF{ME74D47A_HIDD3N_a6df8db8}

## **Notas adicionales**

## Paso 1:  Descomprimir carpeta y luego usar el siguiente comando
`exiftool exiftool ukn_reality.jpg` 

## Paso 2: Despues nos saldra esto de ahi nos enfocaremos en el "Attribution URL "
```
======== ukn_reality.jpg
ExifTool Version Number         : 13.36
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2024:02:15 17:40:21-05:00
File Access Date/Time           : 2026:03:23 18:51:04-04:00
File Inode Change Date/Time     : 2026:03:23 18:51:04-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 :cGljb0NURntNRTc0RDQ3QV9ISUREM05fYTZkZjhkYjh9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
    1 image files read
    1 files could not be read
```

## Paso 3: Teniendo ya el Attribution URL  ahora pongamos este comando y ahi estara la bandera..
```
echo -n cGljb0NURntNRTc0RDQ3QV9ISUREM05fYjMyMDQwYjh9Cg== | base64 -d
```