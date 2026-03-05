## **Descripcion**
How about trying to match a regular expressionThe website is running [here](http://saturn.picoctf.net:49152/).
## **Solucion**
se hizo uso de la pagina  https://regexr.com/
picoCTF{succ3ssfully_matchtheregex_f89ea585}

## **Notas adicionales**
Muestra una pagina y le pones cualquier dato y marca como error, tienes que pasar a ver el codigo de la pagina y te encontraras con este scripts
```
|   |
|---|
|<script>|
|function send_request() {|
|let val = document.getElementById("name").value;|
|// ^p.....F!?|
|fetch(`/flag?input=${val}`)|
|.then(res => res.text())|
|.then(res => {|
|const res_json = JSON.parse(res);|
|alert(res_json.flag)|
|return false;|
|})|
|return false;|
|}|
||
|</script>|
```
 De hay tomaras el P....F!? y lo pegaras en expression de la pagina indicada y en tools te va dando los pasos, si llegaste a p12345F, lo copias y pegas en la pagina, te dara la bandera..
## **Referencias**
https://regexr.com/
picoCTF 2023 - [ Web ] - MatchTheRegex -https://www.youtube.com/watch?v=YZemkSTN50U&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=64