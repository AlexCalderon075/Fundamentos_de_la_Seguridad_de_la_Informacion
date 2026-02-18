## **Descripcion**
I accidentally wrote the flag down. Good thing I deleted it!You download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/77/challenge.zip)
## **Solucion**
Se hizo uso de los comando siguientes
wget  https://artifacts.picoctf.net/c_titan/69/challenge.zip
unzip challenge.zip 
entrar a la carpeta drop-in 
cd drop-in 
se encontro  a dentro de ahi un archivo message.txt, haciendo
un cat no se logro aun la bandera.
git log
git checkout 3d5ec8a26ee7b092a1760fea18f384c35e435139
cat message.txt

picoCTF{s@n1t1z3_30e86d36}
## **Notas adicionales**
Este numero 3d5ec8a26ee7b092a1760fea18f384c35e435139 se encontro haciendo git log
`git log` mostró que `HEAD` ya apuntaba a ese commit.