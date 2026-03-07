## **Descripcion**
This file contains more than it seems. Get the flag from [garden.jpg](https://challenge-files.picoctf.net/c_fickle_tempest/150b6eaad43200d3dc91f98c390e4c6168620b57d0b95a7e9d04c92910bbbe16/garden.jpg).

## **Solucion**
picoCTF{more_than_m33ts_the_3y3a63b5b27}

## **Notas adicionales**
Se hizo uso de hexeditor, una herramienta  que ya tiene  kali 
┌──(kali㉿kali)-[~/Downloads]
└─$ hexeditor garden.jpg   
se abrira una ventana nueva con numeros hexa, presionaras ctrl-w y sabe buscar por texto o numero,eliges texto y pones  pico y ohtendras la bandera.

otro metodo es usar el comando
└─$ strings garden.jpg   
saldra una serie de texto al final estara la bandera
## **Referencias**
  
picoCTF 2021 writeup [14] - Forensic - Glory of the Garden https://www.youtube.com/watch?v=xxhnGxgOtWs&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=14