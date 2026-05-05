## **Descripcion**
Can you figure out how this program works to get the flag?Connect to the program with netcat:`$ nc saturn.picoctf.net 60863`The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/526/picker-III.py).
## **Solucion**

picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_226dd285}

## **Notas adicionales**
Paso 1. Descargamos el archivo picker-III.py
Paso 2. nos conectamos al servidor.
Paso 3. Dentro de ahi ponemos la palabra help
Paso 4. Nos saldra un menu y selecionamos el 3 "write_variable"
Paso 5.Nos saldra algo como "please enter variable name to write" ahi pondremos read_variable
Paso 6. Nos saldra otra como "please enter new value of variable" y ahi ponemos whin
Paso 7. Nos saldra una serie de numeros hexa. los llevamos al cyberchef y escojemos el de hexa y tendremos la bandera.


## **Referencias**
https://gchq.github.io/CyberChef/