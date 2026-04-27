## **Descripcion**
This vault uses ASCII encoding for the password.The source code for this vault is here: [VaultDoor4.java](https://challenge-files.picoctf.net/c_fickle_tempest/3af806b1d880a4a7cecd00831a8bcc913cf57c68cb7f5cfb8597f710c5d771e1/VaultDoor4.java)
## **Solucion**
picoCTF{jU5t_4_bUnCh_0f_bYt3s_13df618a23}
## **Notas adicionales**
Paso1 - Examinamos el código fuente en Java que se nos da
Paso2. La Flag esta codificada en diferentes sistemas numericos solo hay que convertirlos a texto

Nota:El maestro uso dos formas,pero yo usare una..

Paso 3.- Ejecutamos el siguiente código en una consola javascript del navegador

```
`String.fromCharCode(106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 061 , 063 ) +
            ['d' , 'f' , '6' , '1' , '8' , 'a' , '2' , '3'].join('')`
```

y obtendremos la bandera.
## **Referencias**
[picoCTF 2019 writeup [50] - Reverse Engineering - vault-door-4](https://www.youtube.com/watch?v=rPvREN6AS0I&pp=ygUUcGljb2N0ZiB2YXVsdCBkb29yIDQ%3D "picoCTF 2019 writeup [50] - Reverse Engineering - vault-door-4") 