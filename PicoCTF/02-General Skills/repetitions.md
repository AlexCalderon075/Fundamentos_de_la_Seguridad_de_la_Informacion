
# **Descripcion**
Can you make sense of this file?Download the file [here](https://artifacts.picoctf.net/c/477/enc_flag).

**Solucion**
Se utilizo comando linux y pagina web https://www.base64decode.org/
```
Alexander_Calderon-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/477/enc_flag
--2026-02-10 20:43:06--  https://artifacts.picoctf.net/c/477/enc_flag
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.33, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 349 [application/octet-stream]
Saving to: 'enc_flag'

enc_flag            100%[==================>]     349  --.-KB/s    in 0s      

2026-02-10 20:43:07 (151 MB/s) - 'enc_flag' saved [349/349]

Alexander_Calderon-picoctf@webshell:~$  cat enc_flang
cat: enc_flang: No such file or directory
Alexander_Calderon-picoctf@webshell:~$ cat enc_flag                           
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbHBWV0VKVVZGWmFWMDVHV2tkYVNHUlZDazFyY0ZkVWJGWlhZVlpLU0dWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
```

picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_de523f49}

## **Referencias**
https://www.base64decode.org/

