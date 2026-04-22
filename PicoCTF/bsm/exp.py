## basic-mod1`python
# leemos el mensaje y quitamos espacios y dividimos en partes
data = open('message.txt','r').read().strip().split(' ')

print(data)
flag = ''

# recorremos el mensaje para decodificarlo
for c in data:
        char = int(c) % 37
        print(f'{c:<5} - {char:<5} - ',end='')
         # mapeamos a letras en codigo ascii sumando 65
        if char>=0 and char<=25:
                s = chr(char+65)
        # mapeamos a numeros en codigo ascii (48 - 26)
        elif char>=26 and char<=35: 
                s= chr(char+22)
        elif char==36:
                s = '_'
        flag += s
        print(s)
print(f'picoCTF{{{flag}}}')
