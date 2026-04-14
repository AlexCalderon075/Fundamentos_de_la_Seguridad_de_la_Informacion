## **Descripcion**
Can you get the real meaning from this file. Download the file [here](https://artifacts.picoctf.net/c_titan/2/enc_flag).
## **Solucion**
picoCTF{caesar_d3cr9pt3d_78250afc}
## **Notas adicionales**
# interencdec
- Decodificar base64
- Eliminar caracteres : 'b y ' 
- Decodificar nuevamente en base64
```
cat enc_flag | base64 -d | tr -d "'b" | base64 -d
```
- Ir a cyberchef elegir la receta rot13 y rotar 19 posiciones
