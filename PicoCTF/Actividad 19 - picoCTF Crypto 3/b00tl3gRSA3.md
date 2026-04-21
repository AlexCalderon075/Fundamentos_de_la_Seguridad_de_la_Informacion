## **Descripcion**
Why use p and q when I can use more? Connect with nc fickle-tempest.picoctf.net 53422.
## **Solucion**

picoCTF{too_many_fact0rs_3023548}

## **Notas adicionales**
Aqui como se hizo en el  b00tl3gRSA2

Paso 1: Hacemos conexion a desde la terminal nc fickle-tempest.picoctf.net 53422

Paso 2  Nos saldra esta serie de numeros  en la terminal 
`c: 4006662290392073132079461020230759698469297636913155411515500361939685613253658285933730410595750196035165782561841970167847016161239774584290726498464721793093486787922945893023812154715603186233616106096132781859768845598786832807508200838656210874436335015472747552134667367569682241238205797042291558884994768880065373740316990741448064916`
`n: 11962757191381123474727888619327459849930865587648186997851126981384939960778319806191955099641153923815407643868774833379201199293037503943564912298000487477929149935085989630625128904056180818295780114100708969227629126081971781470008426579976374057603767839805308188998149834345134619688234839474343338319616245697131033416000791972907070513`
`e: 65537`

Paso 3. En la pagina de dcode.fr ahi veremos varios recuadros entonces  donde es C ponemos el c Value of the cipher message (Integer) C=
donde es el n va el n   Public Key value (Integer) N=
y al ultimo el e Public Key E (Usually E=65537) E= , pero tambien usaremos la calculadora de factorizacion para factorizar un numero de la serie de numeros  cuando lo tengamos es enumero se agregara a phi Intermediate value Phi (Integer) φ=, solo presionamos calcute y obtenemos la bandera..
## **Referencias**
https://www.dcode.fr/rsa-cipher
https://www.alpertron.com.ar/ECM.HTM