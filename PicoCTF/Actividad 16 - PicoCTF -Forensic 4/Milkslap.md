## **Descripcion**
http://wily-courier.picoctf.net:51489/
## **Solucion**
picoCTF{imag3_m4n1pul4t10n_sl4p5}\n
## **Notas adicionales**

- Descargar el archivo con `wget` o botón derecho `Open Image in New Tab` y descargarla de ahí
`wget http://mercury.picoctf.net:7585/concat_v.png`

- Aplicar `zsteg` ampliando el buffer de ruby para evitar desbordamientos, la bandera aparece

`export RUBY_THREAD_VM_STACK_SIZE=500000000 zsteg concat_v.png`
