## **Descripcion**

What does asm3(0xb58568e8,0xc63ab2a1,0xf9d33ef4) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://challenge-files.picoctf.net/c_fickle_tempest/b3fee52f11c2963c3f6008623c66d7c0906ab439f927132ac7fbc1d53f83c4ee/test.S)
## **Solucion**

0x9fba

## **Notas adicionales**

Paso 1.Se descarga el archivo.
Paso 2. Dentro del archivo se encuentra un codigo ensamblador.
Paso 3. Con la ayuda de la pagina https://carlosrafaelgn.com.br/Asm86/ vamos a sacar la bandera.
Paso 4. Pegamos el codigo a la pagina y agregando push 3 veces con las direcciones de memoria.
Paso 5. En windows escojemos registrer y compilamos por paso cuando lleguemos a nop, en el eax tendremos la bandera. 


## **Referencias**
https://carlosrafaelgn.com.br/Asm86/
picoCTF 2019 writeup [55] - Reverse Engineering - asm3 - https://www.youtube.com/watch?v=REQOuLONQQc