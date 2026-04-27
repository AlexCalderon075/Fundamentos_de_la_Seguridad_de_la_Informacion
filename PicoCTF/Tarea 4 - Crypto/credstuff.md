## **Descripcion**
We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it? Download the leak [here](https://artifacts.picoctf.net/c/151/leak.tar). The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.
## **Solucion**
picoCTF{C7r1F_54V35_71M3}
## **Notas adicionales**
Paso 1. Se descargo el archivo .tar
Paso 2. Se vio en el que habia dos archivos  usernames.txt y password.txt
Paso 3. Se ubico el usuario cultiris  y la contraseña del usuario cvpbPGS{P7e1S_54I35_71Z3}
Paso 4. Se utilizo cyberchef  donde se pego la contraseña y usamos la opcion rot13 para obtener la bandera.

## **Referencias**
https://gchq.github.io/CyberChef/