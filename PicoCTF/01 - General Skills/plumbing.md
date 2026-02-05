# **Descripcion**

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag?Connect to fickle-tempest.picoctf.net 55527.
# **Solucion** 
Se  utilizo  nuevamente la terminal de linux( en mi caso la estoy usando) se guio  del mismo pico diciendo que utilizaras el comando nc y tambien basandonos al ejercicio anterior

man nc
nc host port = nc fickle-tempest.picoctf.net 55527 (se utilzo el signo = solo para decir que es equivalente, el comando usado fue nc fickle-tempest.picoctf.net 55527)
nc fickle-tempest.picoctf.net 55527 | grep pico

picoCTF{digital_plumb3r_0BAc587E}

## **Referencias

hint de picoCTF