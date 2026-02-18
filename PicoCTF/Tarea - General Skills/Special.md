## **Descripcion**
Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)Start your instance to see connection details.`ssh -p 58098 ctf-player@saturn.picoctf.net`The password is `d8819d45`

## **Solucion**
se ingreso al servidor  `ssh -p 58098 ctf-player@saturn.picoctf.net`
aqui se intento varias forma de obtener la bandera hasta que se pudo

`Alexander_Calderon-picoctf@webshell:~$ ssh -p 58098 ctf-player@saturn.picoctf.net
ctf-player@saturn.picoctf.net's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.8.0-1044-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Last login: Wed Feb 18 22:26:43 2026 from 127.0.0.1
Special$ find
Find 
sh: 1: Find: not found
Special$ find .
Find . 
sh: 1: Find: not found
Special$ clear & find .
Clear & find . 
sh: 1: Clear: not found
.
./blargh
./blargh/flag.txt
./.cache
./.cache/motd.legal-displayed
Special$ cls & cat ./blargh/flag.txt
Cos & cat ./blargh/flag.txt 
sh: 1: Cos: not found
picoCTF{5p311ch3ck_15_7h3_w0r57_0c61d335}Special$ 
`
picoCTF{5p311ch3ck_15_7h3_w0r57_0c61d335}
## **Notas adicionales**
Se explotó un **filtro defectuoso que alteraba el primer comando** (probablemente un "spell checker" o script que capitalizaba la primera palabra).

Se evitó el filtro usando:

`comando_falso & comando_real`

Así:
- El primero fallaba.
    
- El segundo se ejecutaba normalmente.