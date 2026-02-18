## **Descripcion**
Can you read files in the root file?The system admin has provisioned an account for you on the main server:`ssh -p 52684 picoplayer@saturn.picoctf.net`Password: `UYiOazkqY2`Can you login and read the root file?
## **Solucion**
Se metio al servidor para encontrar la carpeta y la bandera
ssh -p 52684 picoplayer@saturn.picoctf.ne
sudo -l
ls 
cd root
ls -al
cat .flag.txt

picoCTF{uS1ng_v1m_3dit0r_89e9cf1a}

## **Notas adicionales**
sudo -l se utiliza en Linux para listar los permisos que el usuario actual tiene con sudo
ls -la sirve para listar todos los archivos y directorios (incluidos los ocultos) en formato detallado.
## **Referencias**
https://documentation.suse.com/es-es/sle-micro/6.0/html/Micro-sudo-run-commands-as-superuser/index.html