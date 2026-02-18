## **Descripcion**


My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/69/challenge.zip)
## **Solucion**
Se hizo uso de los comando siguientes
wget  https://artifacts.picoctf.net/c_titan/69/challenge.zip
unzip challenge.zip 
entrar a la carpeta drop-in 
cd drop-in 
se vio que tiene de archivos
flag.py
se ejecuto y no se obtuvo nada
hasta aplicar estos comandos
git branch -a
git checkout feature/part-1
git checkout feature/part-2
git checkout feature/part-3
cat flag.py

picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_e4b79efb}

## **Notas adicionales**
Tuve que investigar nuevamente para este desafio.
git branch El comando branch **te permite crear ramas de tu codigo**. El comando branch te permite crear ramas de tu código, cambiarte y verlas.
El comando git checkout feature cambia tu directorio de trabajo actual y el puntero HEAD del repositorio a la rama existente llamada "feature". Esto actualiza todos los archivos de tu directorio de trabajo para que coincidan con la versión almacenada en esa rama y ordena a Git que registre las nuevas confirmaciones en esa rama.
## **Referencias**
https://github.com/richistron/aprendiendo-git/blob/master/docs/branch.md