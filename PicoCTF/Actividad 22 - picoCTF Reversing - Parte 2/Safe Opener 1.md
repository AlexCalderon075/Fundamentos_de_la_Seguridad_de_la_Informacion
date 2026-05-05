## **Descripcion**
Can you open this safe?I forgot the key to my safe but this [program](https://artifacts.picoctf.net/c/83/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?Put the password you recover into the picoCTF flag format like:
## **Solucion**

picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}

## **Notas adicionales**
Paso 1. Descargamos el archivo java
Paso 2.lo vemos,abra en un apartado  asi `"public static boolean openSafe(String password) {`
        `String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";`
`"`
Paso 3. Temamos esa serie de numero base64, puedes usar el cyberchef poniendolo en base64 o el terminal y ahi encontraras la bandera.

## **Referencias**
https://gchq.github.io/CyberChef/