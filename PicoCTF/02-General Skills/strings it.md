## **Descripcion**

Can you find the flag in [file](https://challenge-files.picoctf.net/c_fickle_tempest/563d66bbed3925c75ed71efa974bfafab26460ae99938d699a8881cd173fca60/strings) without running it?

## **Solucion**
Se utilizo estos comandos
wget https://challenge-files.picoctf.net/c_fickle_tempest/563d66bbed3925c75ed71efa974bfafab26460ae99938d699a8881cd173fca60/strings
cat strings
strings strings | grep picoCTF

picoCTF{5tRIng5_1T_dB2CEA76}
