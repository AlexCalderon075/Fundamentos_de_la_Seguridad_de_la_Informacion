## **Descripcion**
I found a web app that can help process images: PNG images only!Try it [here](http://atlas.picoctf.net:65471/)!
## **Solucion**

picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_d3ac625b}

## **Notas adicionales**
Este ejercicio  se hizo uso de crear un webshell, despues lo aguardamos se cambia el nombre asi webshell.png.php
en el archivo nano de tu php, ponle arriba PNG.
ahora si teniendo eso lo subes a la pagina, va decir que estas correcto, al ultimo agregas esto en el navegador. "http://atlas.picoctf.net:65471/uploads/webshell.png.php?cmd=ls%20.."
ahi debe de aparecer varios archvos, ahi un txt. con serie de numero ahora haras esto "http://atlas.picoctf.net:65471/aquiponeslaseriedenumeros.txt.
enter y estara la bandera.
## **Referencias**
  
picoCTF 2023 - [ Web ] - Trickster - https://www.youtube.com/watch?v=co8MZmviC1U&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=65