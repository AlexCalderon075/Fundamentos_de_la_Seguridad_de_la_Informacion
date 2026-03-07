## **Descripcion**
We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/07bf5ee832c595a6de406476b6c07f164d2951fbcfcf9cf3739c25dea26e5f0b/capture.pcap). Recover the flag.
## **Solucion**
 picoCTF{p1LLf3r3d_data_v1a_st3g0}

## **Notas adicionales**
Se hizo uso del programa sharkwire, primero se busco un udp, despues vimos el stream, despues buscamos que sean 22,nos salio un apartado de muchas udp.
NOTA: El maestro hizo uso de python, en mi caso utilice una pagina de ascii code to text character,
razon no me quiso cargar algunas librerias..
## **Referencias**
picoCTF 2019 writeup [23] - Forensic - shark on wire 2 https://www.youtube.com/watch?v=WcMl1SvQ6hI
https://codeshack.io/ascii-to-text-converter/