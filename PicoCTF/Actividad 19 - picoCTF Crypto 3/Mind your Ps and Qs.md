## **Descripcion**
In RSA, a small e value can be problematic, but what about N? Can you decrypt this? [values](https://challenge-files.picoctf.net/c_wily_courier/8f75844947ccdb93020eecaf5eea8be97753b2075202328032bb4854ca7c6863/values)
## **Solucion**
picoCTF{sma11_N_n0_g0od_1dc7ae91}

## **Notas adicionales**

Paso 1. Se descarga el archivo 
Paso 2. Abrimos el archivos y obtendremos esto
```
Decrypt my super sick RSA:
c: 15341890103764929939105506004034128738090325640037083301857608662849501626260517
n: 948406957756830799684818171639547165784816468744946013083947881743680617123566349
e: 65537
```

Paso 3. En la pagina de dcode.fr ahi veremos varios recuadros entonces  donde es C ponemos el c Value of the cipher message (Integer) C=
donde es el n va el n   Public Key value (Integer) N=
y al ultimo el e Public Key E (Usually E=65537) E= , cuando lo tengamos, solo presionamos calcute y obtenemos la bandera..
## **Referencias**
https://www.dcode.fr/rsa-cipher
picoCTF 2021 writeup [44] - Cryptography - Mind your Ps and Qs - https://www.youtube.com/watch?v=pwGSp_4YHTg
