## **Descripcion**
Someone's commits seems to be preventing the program from working. Who is it?You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/159/challenge.zip)
## **Solucion**
Se uso los comando 
wget https://artifacts.picoctf.net/c_titan/159/challenge.zip
luego descomprimir el archivo
unzip challenge.zip 
entrar a la carpeta drop-in 
cd drop-in 
se vio que tiene de archivos
se ejecuto git log message.py
se obtuvo la bandera 
picoCTF{@sk_th3_1nt3rn_81e716ff}
## **Notas adicionales**
Intente varias formas de ver la bandera con cat o python3, pero no me daba la bandera tuve que investigar mas y llegue a saber del comando git log 
El comando `git log` muestra todas las commits en el historial del repositorio.

Por defecto, el comando muestra los datos de cada commit:

- Secure Hash Algorithm (SHA).
- Autor.
- Fecha.
- Mensaje del commit.
## **Referencias**
https://www.freecodecamp.org/espanol/news/explicacion-del-comando-git-log/