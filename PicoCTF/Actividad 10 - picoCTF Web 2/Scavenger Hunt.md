## **Descripcion**
There is some interesting information hidden around this site. Can you find it?http://wily-courier.picoctf.net:57503/
## **Solucion**
picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_9588550}
## **Notas adicionales**
Se ingreso al sitio,despues del sitio se hizo una serie de pasos para ir encontrando la bandera, 
el primero fue entrar al codigo y despues a  mycss.css, en el myjs.js ya nos pide usar los robots(Tema que ya se habia visto antes), entrando al robots.txt nos hace mencion de usar .htaccess para encontrar la otras partes se hizo uso de .Ds_Store se usa en mac finalmente ahi encontramos la ultima parte de la bandera.

Los ficheros `.htaccess` (o "ficheros de configuración distribuida") facilitan una forma de realizar cambios en la configuración en contexto directorio. Un fichero, que contiene una o más directivas, se coloca en un documento específico de un directorio, y estas directivas aplican a ese directorio y todos sus subdirectorios.
Un archivo `.DS_Store` (Desktop Services Store) es un archivo oculto generado automáticamente por el sistema operativo macOS en cada carpeta que se explora. Su función es guardar configuraciones personalizadas, como la posición de los iconos, el tamaño de la ventana, el fondo de la carpeta y las opciones de visualización.
## **Referencias**
picoCTF 2021 writeup [13] - Web - Scavenger Hunt
https://www.youtube.com/watch?v=E2gN3AGHirc&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=13
https://httpd.apache.org/docs/current/es/howto/htaccess.html
https://www.softzone.es/programas/sistema/ds_store/