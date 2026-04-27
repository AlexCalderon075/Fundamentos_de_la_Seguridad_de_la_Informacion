## **Descripcion**
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher? Download the message [here](https://artifacts.picoctf.net/c/154/message.txt).
## **Solucion**

PICOCTF{5UB5717U710N_3V0LU710N_357BF9FF}
## **Notas adicionales**
Paso 1. Se abre el archivo se encontrara esto
~$ cat message.txt.2
ZGSOCXPQUYHMILERVTBWNAFJDK 

Qctcnrel Mcptzlo ztebc, fuwq z ptzac zlo bwzwcmd zut, zlo gtenpqw ic wqc gccwmc
xtei z pmzbb szbc ul fqusq uw fzb clsmebco. Uw fzb z gcznwuxnm bsztzgzcnb, zlo, zw
wqzw wuic, nlhlefl we lzwntzmubwb—ex sentbc z ptczw rtukc ul z bsuclwuxus reulw
ex aucf. Wqctc fctc wfe tenlo gmzsh brewb lczt elc cjwtciuwd ex wqc gzsh, zlo z
melp elc lczt wqc ewqct. Wqc bszmcb fctc cjsccoulpmd qzto zlo pmebbd, fuwq zmm wqc
zrrcztzlsc ex gntlubqco pemo. Wqc fcupqw ex wqc ulbcsw fzb actd tcizthzgmc, zlo,
wzhulp zmm wqulpb ulwe selbuoctzwuel, U senmo qztomd gmzic Ynruwct xet qub eruluel
tcbrcswulp uw.

Wqc xmzp ub: ruseSWX{5NG5717N710L_3A0MN710L_357GX9XX}

Paso 2. Se ingresa a la pagina https://www.dcode.fr/monoalphabetic-substitution
en el apartado Alphabetic substitution ciphertext ingresa desde Q hasta la llave
Paso 3. Knowing the substitution alphabet
Se ingresa lo de arriba , despues le presionamos descrypt automatically y nos dara la bandera

## **Referencias**
https://www.dcode.fr/monoalphabetic-substitution