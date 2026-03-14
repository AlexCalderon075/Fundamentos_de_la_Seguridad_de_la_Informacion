## **Descripcion**
We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/66113619363fca174ef6bf56587007af1626f99c44fc5cf92333f9fd8876ce9a/capture.pcap) and [key](https://challenge-files.picoctf.net/c_fickle_tempest/66113619363fca174ef6bf56587007af1626f99c44fc5cf92333f9fd8876ce9a/picopico.key). Recover the flag.
## **Solucion**
Se hizo uso de la terminal y el programa  wireshark
picoCTF{nongshim.shrimp.crackers}
## **Notas adicionales**
- Verificamos el tipo de archivo, uno es una captura de paquetes, el otro una llave rsa con la que fue encriptado el tráfico TLS en el paquete

`file capture.pcap file picopico.key` 
### Forma 1

- Abrir el archivo con Wireshark

`wireshark capture.pcap &` 

- Ve a Edit - Preferences - Protocols - TLS
    
    - ponemos la llave en RSA Keys list en la columna de key
    - ponemos un nombre a TLS debug file
    
- Ve a Edit - Find Next , Packet Details (en el primer drop down list), `String` picoCTF
- En el encapsulado, seleccionar la bander - click botón derecho copy .. as pritable text

### Forma 2

- Decodificar el paquete usando la llave rsa con `ssldump`:

`ssldump -r capture.pcap -k picopico.key -d | grep pico -A 2`
## **Referencias**

https://en.wikipedia.org/wiki/Transport_Layer_Security
picoCTF 2019 writeup [24] - Forensic - WebNet0 - https://www.youtube.com/watch?v=9uflLPoETOc&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=24