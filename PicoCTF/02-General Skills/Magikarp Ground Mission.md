# **Descripcion**

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin.Login via `ssh` as `ctf-player` with the password, `8c606eb1` on the host `wily-courier.picoctf.net` and port `60953`.

## **Solucion**
ssh ctf-player@wily-courier.picoctf.net -p 59534

```
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
ctf-player@pico-chall$ cat 1of3.flag.txt  instructions-to-2of3.txt
picoCTF{xxsh_
Next, go to the root of all things, more succinctly `/`
ctf-player@pico-chall$ ls /
2of3.flag.txt  dev                       lib    opt   sbin  usr
bin            etc                       lib64  proc  srv   var
boot           home                      media  root  sys
challenge      instructions-to-3of3.txt  mnt    run   tmp
ctf-player@pico-chall$ cat /2of3.flag.txt /instructions-to-3of3.txt
0ut_0f_//4t3r_
Lastly, ctf-player, go home... more succinctly `~`
ctf-player@pico-chall$ ls ~
3of3.flag.txt  drop-in
ctf-player@pico-chall$ cat ~/3of3.flag.txt
0b24fc4f}
```

picoCTF{xxsh_0ut_0f_//4t3r_0b24fc4f}
## **Notas adicionales**
El comando `ls` (list) en Linux y sistemas Unix es una herramienta fundamental de la línea de comandos utilizada para listar archivos y directorios dentro de una ubicación específica

## **Referencias**
https://www.ionos.mx/digitalguide/servidores/configuracion/comando-ls-de-linux/#:~:text=ls%20es%20uno%20de%20los%20comandos%20de,se%20muestra%20por%20defecto%20en%20orden%20alfab%C3%A9tico.

