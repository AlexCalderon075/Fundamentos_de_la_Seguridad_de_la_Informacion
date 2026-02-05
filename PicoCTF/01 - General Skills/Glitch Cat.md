# **Descripcion**

Our flag printing service has started glitching!`$ nc saturn.picoctf.net 61449`
# **Solucion** 

Se utilizo  nuevamente la terminal de linux( en mi caso la estoy usando) se guio  del mismo pico diciendo que utilizaras el comando nc y esta ves usamos python porque se esta manejando con hexadecimales

nc saturn.picoctf.net 61449
python3
>>'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36)\
 + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'

picoCTF{gl17ch_m3_n07_bda68f75}

## **Notas adicionales**

Esto salio "picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36)\
 + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'"
 en la hora de ejecutar nc saturn.picoctf.net 61449
## **Referencias

https://www.rapidtables.com/convert/number/decimal-to-binary.html

