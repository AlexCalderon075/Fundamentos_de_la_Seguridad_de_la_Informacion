## **Descripcion
Can you look at the data in this binary? The bash script might help![static](https://challenge-files.picoctf.net/c_wily_courier/a7a487d82414dabf57a3ec5db604ae18c17b11406225839247539d5edb709957/static), [ltdis.sh](https://challenge-files.picoctf.net/c_wily_courier/a7a487d82414dabf57a3ec5db604ae18c17b11406225839247539d5edb709957/ltdis.sh)

## **Solucion**
Se utilizo los siguientes comando.
chmod +x static
chmod +x ltdis.sh
./ltdis.sh 
./ltdis.sh static
cat static.ltdis.strings.txt

picoCTF{d15a5m_t34s3r_20335e41}


## **Notas adicionales**
El comando chmod (modo de cambio) en Linux/UNIX se utiliza para modificar los permisos de archivos y directorios. Controla quién puede leer, escribir o ejecutar un archivo estableciendo derechos de acceso para el propietario, el grupo y otros. Se utiliza para cambiar permisos de archivos y directorios Gestiona el acceso para el propietario, el grupo y otros Controla los permisos de lectura (r), escritura (w) y ejecución (x) Ayuda a mantener la seguridad del sistema y un control de acceso adecuado

El comando cat static.ltdis.strings.txt se obtuvo cuando se realizo  "./ltdis.sh static"
"Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset"
## **Referencias**
https://www.geeksforgeeks.org/linux-unix/chmod-command-linux/