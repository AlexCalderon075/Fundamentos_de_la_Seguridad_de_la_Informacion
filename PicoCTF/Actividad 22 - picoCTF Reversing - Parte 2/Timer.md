## **Descripcion**
You will find the flag after analysing this apkDownload [here](https://artifacts.picoctf.net/c/449/timer.apk).

## **Solucion**
picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}


## **Notas adicionales**
Paso 1. Se descargo el archivo es un "TImer.apk"
Paso 2. Usaremos el programa de https://www.decompiler.com/
Paso 3. Seleccionamos desde el programa el timer.apk
Paso 4. Cuando se cargue nos mostrara dos apartado "source" y "resource"
Paso 5. Escojemos source de ahi nos vamos a la carpeta "com" y despues a "example". "timer"
Paso 6. al ultimo nos saldra 3 archivos javas escojemos el de - [BuildConfig.java](https://www.decompiler.com/jar/ae81a9d6c4de3688b49de6b9e8560c5c/timer.apk/sources/com/example/timer/BuildConfig.java)
ahi estara la bandera.


## **Referencias**
https://www.decompiler.com/