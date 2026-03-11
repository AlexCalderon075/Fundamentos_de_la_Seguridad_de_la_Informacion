## **Descripcion**
Decode this [message](https://challenge-files.picoctf.net/c_fickle_tempest/678ff56c639c7645276578f3a9767ec2feaed1450045dd982c525b5795f7f589/message.wav) from the moon.
## **Solucion**
Se hizo uso de la terminal
picoCTF{beep_boop_im_in_space}
## **Notas adicionales**
Usamos estos comandos 
## m00nwalk
-Verificamos el tipo de archivo con file
```
file message.wav 
```
- Descargamos decodificador STTV de github y lo instalamos
> https://github.com/colaclanth/sstv
```
cd /opt
sudo git clone https://github.com/colaclanth/sstv
cd sstv
https://github.com/colaclanth/sstv
```
- Decodificamos el mensaje oculto en el .wav y lo guardamos en flag.png
```
sstv -d message.wav -o flag.png
```
- Abrimos el archivo y copiamos la flag
```
open flag.png
```

## **Referencias**
  
picoCTF 2021 writeup [19] - Forensic - m00nwalk https://www.youtube.com/watch?v=UyLTEpAz6eE&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=19
https://github.com/colaclanth/sstv