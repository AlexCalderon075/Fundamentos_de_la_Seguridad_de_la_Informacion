## **Descripcion**

This service can provide you with a random number, but can it do anything else?Connect to the program with netcat:`$ nc saturn.picoctf.net 49814`The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/514/picker-I.py).
## **Solucion**

picoCTF{4_d14m0nd_1n_7h3_r0ugh_6e04440d}

## **Notas adicionales**
Paso 1. Descargamos el archivo .py
Paso 2. Nos metemos al servidor 
Paso 3. En una parte del codigo llamado win() ahi viene lo que contiene la bandera.
Paso 4. entonces en el servidor ponemos win() y nos dara una serie de numeros hexa
Paso 5. Utilizamos cyberchef configurado al hex y obtendremos la bandera.

## **Referencias**
https://gchq.github.io/CyberChef/