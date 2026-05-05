## **Descripcion**

Can you figure out how this program works to get the flag?Connect to the program with netcat:`$ nc saturn.picoctf.net 60698`The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/527/picker-IV.c). The binary can be downloaded [here](https://artifacts.picoctf.net/c/527/picker-IV).
## **Solucion**

picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_01672a61}

## **Notas adicionales**
Paso 1. Se descargan los dos archivos uno es .c y otro es binary
Paso 2. Ingresamos al servidor
Paso 3. Nos saldra "enter the address in hex to jump to, excluding '0x' "
Paso 4. utilizaremos el programa https://dogbolt.org/
Paso 5. Seleccionamos nuestro archivo  binario y despues nos abrira  4 opciones escojemos la de hex-rays
Paso 6. Dentro de ahi buscamos una funcion llamada int win(), encontrandola arriba estara un numero hexa, lo agarramos despues nos pasamos al terminal y pegamos. si lo hiciste correcto debe de dar la bandera.


## **Referencias**