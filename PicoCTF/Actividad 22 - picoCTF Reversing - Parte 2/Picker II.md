## **Descripcion**

Can you figure out how this program works to get the flag?Connect to the program with netcat:`$ nc saturn.picoctf.net 50133`The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/523/picker-II.py).
## **Solucion**
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_95d44590}
## **Notas adicionales**
Paso 1. Se descargo el archivo .py
Paso 2. Ingresamos al servidor.
Paso 3. Debemos de ingresar una parte del codigo que tenemos que seria esto "open('flag.txt', 'r').read()"
pero con un print asi print(open('flag.txt', 'r').read())
damos enter y obtendremos la bandera.
