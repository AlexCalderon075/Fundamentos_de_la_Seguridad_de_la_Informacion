
## **Descripcion**
Download this image and find the flag.

- [Download image](https://artifacts.picoctf.net/c/216/pico.flag.png)
## **Solucion**
picoCTF{7h3r3_15_n0_5p00n_a1062667}

## **Notas adicionales**
- Descargar el archivo con `wget` o botón derecho `Open Image in New Tab` y descargarla de ahí
`wget https://artifacts.picoctf.net/c/216/pico.flag.png  `

- Aplicar `zsteg` ampliando el buffer de ruby para evitar desbordamientos, la bandera aparece

`export RUBY_THREAD_VM_STACK_SIZE=500000000                      
zsteg pico.flag.png`