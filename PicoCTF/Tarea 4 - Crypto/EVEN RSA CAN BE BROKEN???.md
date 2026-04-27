## **Descripcion**
This service provides you an encrypted flag. Can you decrypt it with just N & e? Connect to the program with netcat: `$ nc verbal-sleep.picoctf.net 61906` The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_verbal_sleep/c798cbe85b3e431345406f393827b9b905481b5fcd6d4b4a845527ee0602da9b/encrypt.py).
## **Solucion**
picoCTF{tw0_1$_pr!m341c6ed35}
## **Notas adicionales**
Paso 1 se hizo la conexion y obtuvimos esto . `nc verbal-sleep.picoctf.net 61906`
`N: 25306859889024320304781630284890207147350196147219074885827096742390039136763343781637762061307693442768662529486219542923261982335766581227325672232554382`
`e: 65537`
`cyphertext: 735869466556969215417111467579535572599191774779844154176856568975383332925655451103127320992010041353435516059730381031595150966216998077931571722844119`

Paso 2. se utilizo  la herramienta de  https://www.dcode.fr/rsa-cipher
donde se introducieron los valores  en cada campo correspodiente y asi se obtuvo la bandera
## **Referencias**
https://www.dcode.fr/rsa-cipher

