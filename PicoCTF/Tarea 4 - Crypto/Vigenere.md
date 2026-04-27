## **Descripcion**
Can you decrypt this message? Decrypt this [message](https://artifacts.picoctf.net/c/160/cipher.txt) using this key "CYLAB".
## **Solucion**
picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_2951a89h}

## **Notas adicionales**
Paso 1. Se abre el archivo se encontrara esto
~$ cat cipher.txt
rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}
Paso 2. se ingresa la pagina https://www.dcode.fr/vigenere-cipher en el apartado de Vigenere ciphertext pega lo del archivo.
Paso 3. en el apartado  Decryption method ahi otra opcion  llamada Knowing the Key/Password ahi pondras CYLAB
Paso 4. Le presionas a Decrypt y ahi obtienes la bandera.

## **Referencias**
https://www.dcode.fr/vigenere-cipher
