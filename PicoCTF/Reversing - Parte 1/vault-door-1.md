## **Descripcion**
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://challenge-files.picoctf.net/c_fickle_tempest/df83732fa379fb7cf3373e872748a40ec53c5baa532f3274e1ab499cd3d3b197/VaultDoor1.java)
## **Solucion**
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_1ef266}

## **Notas adicionales**
Paso 1. Examinamos el código fuente en Java que se nos da
Paso2. De la función `checkPassword` copiamos a un archivo, las lineas con `password.charAt`
Paso3.Agregamos 0s a las cantidades para hacerlas de dos dígitos y poderlas ordenar

Paso 5.- Ordenamos

`cat flag | sort`

Paso6. Imprimimos 3a columna

`cat flag | sort | awk '{print($3)}'`

Paso6.Quitamos comilla que abre y cierra

`cat flag | sort | awk '{print($3)}' | tr -d "\'"`  

Paso7. Quitamos saltos de linea
cat flag | sort | awk '{print($3)}' | tr -d "'" | tr -d "\n"
y obtenemos la bandera.

## **Referencias**
[picoCTF 2019 writeup [48] - Reverse Engineering - vault-door-1](https://www.youtube.com/watch?v=QZ1ttEjyKxY&pp=ygUUcGljb2N0ZiB2YXVsdCBkb29yIDE%3D "picoCTF 2019 writeup [48] - Reverse Engineering - vault-door-1") 