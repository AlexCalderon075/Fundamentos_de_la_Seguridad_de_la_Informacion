## **Descripcion**
There's an interesting script in the user's home directoryThe work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.

```
Hostname: saturn.picoctf.net
Port:     55982
Username: picoplayer
Password: password
```

## **Solucion**
se uso comando
ssh picoplayer@saturn.picoctf.net -p 55982
./useless -h
cat useless

picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_8504}
## **Notas adicionales**
-Se leyo un manual que se da atraves de cat useless donde se tiene que realizar operaciones matematicas para encontrar la respuesta.


