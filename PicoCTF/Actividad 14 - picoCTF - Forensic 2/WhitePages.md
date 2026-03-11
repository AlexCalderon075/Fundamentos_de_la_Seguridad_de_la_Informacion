
## **Descripcion**
I stopped using YellowPages and moved onto WhitePages... but [the page they gave me](https://challenge-files.picoctf.net/c_fickle_tempest/f35d2be8de731d412d3dbd8c79e6c5b32c62efbb124cf319f54ebddf76ea0ffe/whitepages.txt) is all blank!
## **Solucion**
se hizo uso de la terminal
picoCTF{not_all_spaces_are_created_equal_f6166971531e3ad3b35138611330bba8}
## **Notas adicionales**
- Verificamos que el archivo es UTF-8 con lineas largas

`file whitepages.txt`

- Visualizamos el hexdump del archivo y vemos que es una seuencia de caracteres unicode (e2 80 83 y 20 )

`xxd -g 1 -l 100 whitepages.txt`

- Reemplazamos e2 80 83 por 0s y 20 por 1s

`sed 's/\xe2\x80\x83/0/g' whitepages.txt | sed 's/\x20/1/g'`

-Aqui un punto importante en el video, el maestro hizo un programa en python que es algo igual haciendo esa misma funcion del comando..
## **Referencias**
  
picoCTF 2019 writeup [20] - Forensic - WhitePages https://www.youtube.com/watch?v=427HDV7tzow&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=20
https://cryptii.com/pipes/binary-decoder
https://en.wikipedia.org/wiki/Unicode
https://en.wikipedia.org/wiki/UTF-8