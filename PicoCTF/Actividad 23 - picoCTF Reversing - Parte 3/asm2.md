## **Descripcion**
What does asm2(0x7,0x29) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://challenge-files.picoctf.net/c_fickle_tempest/cc2091d0d95199e62c9fe8a28ff021685c232d6912f8101cda832c5a28873a4c/test.S)

## **Solucion**

0x5c

## **Notas adicionales**
Paso 1. Abrimos el archivo, esta en lenguaje ensamblador
Paso 2.Vamos hacer una serie de oparaciones para encontrar la bandera.
Paso 3. Primera operacion 0x7 <= 0x30c8
Paso4 . hacermos lo siguiente hex(0x29+0x1)
Paso 5. siguiente hex(0x7+0xf7)
Paso 6.haremos ahora esta comparacion "0xfe <=0x30c8"
Paso 7.Hacemos esta division "0x30c8 / 0xf7"
Paso 8. Vamos a tranformar a entero este numero con este comando int(0x29)
Paso 9. Ya teniendo el numero entero lo vamos a sumar en hex con el resultado que nos dio la division del paso 7, hex(41+51) ahi obtendremos nuestra bander
## **Referencias**
picoCTF 2019 writeup [54] - Reverse Engineering - asm2