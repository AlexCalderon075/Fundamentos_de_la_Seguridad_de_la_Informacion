## **Descripcion**
I've hidden a flag in this file. Can you find it?[Forensics_is_fun.pptm](https://challenge-files.picoctf.net/c_wily_courier/d78815176c19ddc85a1388233268d2f4c459fcbbaab197b4a29ebafc88294c54/Forensics_is_fun.pptm)
## **Solucion**
Se hizo uso de la terminal 
picoCTF{D1d_u_kn0w_ppts_r_z1p5}
## **Notas adicionales**
- Verificamos el tipo de archivo, para darnos cuenta que es un `.pptx` de `Power Point`:
`file "Forensics is fun.pptm"`
- Lo desempacampos con `unzip` dado que los archivos de office son en escencia archivos empaquetados:
`unzip "Forensics is fun.pptm"`
- Al desempacar pudimos percatarnos de la presencia del archivo `hidden`, nos movemos a la carpeta donde esta y lo mostramos
`cd ppt/slideMasters cat hidden`
- Es una cadena en `base64` con espacios, la decodificamos para ver la bandera
`cat hidden | tr -d ' ' | base64 -d`

- Aqui tambien el maestro instalo el programa de visual studio, este fue para entrar a la parte de las carpetas del archivo que seria al hidden y ahi estuvo una serie de numeros y letras que due la que se decodifico para la bandera
## **Referencias**
https://www.reviversoft.com/es/file-extensions/pptm
picoCTF 2021 writeup [28] - Forensic - MacroHard WeakEdge - https://www.youtube.com/watch?v=CsCeOp9PFGs&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=28