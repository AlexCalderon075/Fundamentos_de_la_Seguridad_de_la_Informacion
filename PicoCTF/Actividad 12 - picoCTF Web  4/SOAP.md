## **Descripcion**
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?[Web Portal](http://saturn.picoctf.net:52798/)

## **Solucion**
Se uso el inspector de mozilla
picoCTF{XML_3xtern@l_3nt1t1ty_540f4f1e}

## **Notas adicionales**
El maestro utilizo un proxy y el burpsite, en mi caso tuve problemas con el bursipe y trabaje desde el mismo inspector
-en la pagina usas el inspector,pasas al partado de network y presiona la tecla details de PIcoCTF
en network saldra POST entonces te diriges a headers y presionas resend

En ese apartado hasta en ultimo donde dice body pondras este comentario <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY example SYSTEM "/etc/passwd"> ]><data><ID>&example;</ID></data> 
Despues lo aguardas y vas a reponse al final obtendras tu bandera.
## **Referencias**
https://book.hacktricks.wiki/en/pentesting-web/xxe-xee-xml-external-entity.html
picoCTF 2023 - [ Web ] - SOAP