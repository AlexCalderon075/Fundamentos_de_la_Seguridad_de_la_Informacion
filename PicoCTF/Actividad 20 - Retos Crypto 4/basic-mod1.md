b## **Descripcion**
We found this weird message being passed around on the servers, we think we have a working decryption scheme.Download the message [here](https://artifacts.picoctf.net/c/128/message.txt).Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)
## **Solucion**
Se utilizo la terminal
picoCTF{R0UND_N_R0UND_B6B25531}

## **Notas adicionales**
 Paso 1. Se descargo el archivos
 Paso 2. vimos que viene en el archivo messege.txt
 Paso 3. Se vio que contiene esto
 
`└─$ cat message.txt`
`165 248 94 346 299 73 198 221 313 137 205 87 336 110 186 69 223 213 216 216 177 138`  
Paso 4. Con  la ayuda del codigo del maestro lo utilizamos y obtuvimos la respuesta

leemos el mensaje y quitamos espacios y dividimos en partes
`data = open('message.txt','r').read().strip().split(' ')`

`print(data)`
`flag = ''`
`recorremos el mensaje para decodificarlo`
`for c in data:`
        `char = int(c) % 37`
        `print(f'{c:<5} - {char:<5} - ',end='')`
         `# mapeamos a letras en codigo ascii sumando 65`
        `if char>=0 and char<=25:`
                `s = chr(char+65)`
        `# mapeamos a numeros en codigo ascii (48 - 26)`
        `elif char>=26 and char<=35:` 
                `s= chr(char+22)`
        `elif char==36:`
                `s = '_'`
        `flag += s`
        `print(s)`
`print(f'picoCTF{{{flag}}}')
## **Referencias**
[picoCTF 2022 writeup [46] - Cryptography - basic-mod1](https://www.youtube.com/watch?v=t3vRV-j0mF0&pp=ygUTcGljb2N0ZiBiYXNpYy1tb2QgMQ%3D%3D "picoCTF 2022 writeup [46] - Cryptography - basic-mod1") 