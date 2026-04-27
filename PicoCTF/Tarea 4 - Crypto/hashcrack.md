## **Descripcion**
A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server? Access the server using `nc verbal-sleep.picoctf.net 53293`
## **Solucion**
picoCTF{UseStr0nG_h@shEs_&PaSswDs!_eb2f8459}

## **Notas adicionales**
Paso 1. Se hizo la conexion
`$ nc verbal-sleep.picoctf.net 53293`
`Welcome!! Looking For the Secret?`

`We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38`
`Enter the password for identified hash: password123`
`Correct! You've cracked the MD5 hash with no secret found!`

`Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3`
`Enter the password for the identified hash: letmein`
`Correct! You've cracked the SHA-1 hash with no secret found!`

`Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745`
`Enter the password for the identified hash: qwerty098`
Paso 2. Como se puede ver ahi serie de numeros hash aqui utilizamos una herramienta llamada
https://hashes.com/en/tools/hash_identifier se introducia la serie.
Paso 3. El resultado que nos daba ahora se lo pasabamos a https://crackstation.net/ y le presionamos a crack hashe y ahi nos dara la contraseña, como se puede ver se hace 3 veces al final te da la bandera.
## **Referencias**
https://crackstation.net/
https://hashes.com/en/tools/hash_identifier
