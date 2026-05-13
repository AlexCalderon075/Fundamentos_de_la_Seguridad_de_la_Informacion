## **Descripcion**
What does asm1(0x36e) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://challenge-files.picoctf.net/c_fickle_tempest/742701d2dc84a01fe69c48228c14feafdcd3658f83e99b887c550bed0302419e/test.S)

## **Solucion**
0x374


## **Notas adicionales**
Paso 1. Abrimos el archivo, esta en lenguaje ensamblador
Paso 2.Vamos hacer una serie de oparaciones para encontrar la bandera.
Paso 3. hacermos esta comparacion "**Es 0x36e > 0x6c8?**" no
Paso 4 Segunda comparacion. "0x36e != 0x36e"..? no
Paso 5. Operacion aritmetica "$0x36e + 0x6 = 0x374$.", esa es nuetra bandera.
## **Referencias**
picoCTF 2019 writeup [53] - Reverse Engineering - asm1 - https://www.youtube.com/watch?v=Dy-gHlymkdo