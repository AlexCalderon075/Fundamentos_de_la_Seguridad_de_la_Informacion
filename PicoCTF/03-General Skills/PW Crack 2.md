
## **Descripcion**
Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/13/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/13/level2.flag.txt.enc) in the same directory too.

## **Solucion**
Uso de comandos en la terminal
cat level2.py 
python level2.py

picoCTF{tr45h_51ng1ng_489dea9a}


## **Notas adicionales**
igual que el pw crack 1 se uso el cat level2.py para ver cual es la contraseña pero esta ocasion utilizamos el mismo python para decifrar que contraseña sera (chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36))
obteniendo el resultado fue la contraseña 
