## **Descripcion**
We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/capture.pcap) and [key](https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/picopico.key). Recover the flag.
## **Solucion**
se uso el terminal y el programa wireshark
picoCTF{honey.roasted.peanuts}
## **Notas adicionales**
- Verificamos el tipo de archivo, uno es una captura de paquetes, el otro una llave rsa con la que fue encriptado el tráfico TLS en el paquete

`file capture.pcap file picopico.key` 
### Forma 1

- Abrir el archivo con Wireshark

`wireshark capture.pcap &` 

- Cambiar la llave rsa , Ve a Edit - Preferences - Protocols - TLS , sigue el mismo procedimiento del reto anterior, solo borra la llave anterior
- Extraer la imagen en el trafico
    
    - Ve a File - Export Objects - HTTP
    - Selecciona el archivo `vultre.jpg`
    
- Click en Save
- Extrae las cadenas en la imagen y encontraras la banera

`strings -n 10 vulture.jpg` 

### Forma 2

- Decodificar el paquete usando la llave rsa con `ssldump`:

`ssldump -r capture.pcap -k picopico.key -d | grep pi -A 10`

## **Referencias**
https://en.wikipedia.org/wiki/Transport_Layer_Security
  
picoCTF 2019 writeup [25] - Forensic - WebNet1 - https://www.youtube.com/watch?v=Ym3i79nEHjw&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=25