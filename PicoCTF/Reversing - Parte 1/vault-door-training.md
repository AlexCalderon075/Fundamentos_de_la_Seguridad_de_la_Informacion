## **Descripcion**
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](https://challenge-files.picoctf.net/c_fickle_tempest/379ca32f89b74c70403ef5b6515ae2f1d2405e66735347b70bc2ef8063084688/VaultDoorTraining.java)

## **Solucion**
picoCTF{w4rm1ng_Up_w1tH_jAv4_000wYdiGTvt}

## **Notas adicionales**
Paso 1. - Examinamos el código fuente en Java que nos dan, la flag viene hard codeada 
`cat VaultDoorTraining.java`                                                                                                                       
`import java.util.*;`

`class VaultDoorTraining {`
    `public static void main(String args[]) {`
        `VaultDoorTraining vaultDoor = new VaultDoorTraining();`
        `Scanner scanner = new Scanner(System.in);` 
        `System.out.print("Enter vault password: ");`
        `String userInput = scanner.next();`
        `String input = userInput.substring("picoCTF{".length(),userInput.length()-1);`
        `if (vaultDoor.checkPassword(input)) {`
            `System.out.println("Access granted.");`
        `} else {`
            `System.out.println("Access denied!");`
        `}`
   `}`

    `// The password is below. Is it safe to put the password in the source code?`
    `// What if somebody stole our source code? Then they would know what our`
    `// password is. Hmm... I will think of some ways to improve the security`
    `// on the other doors.`
    `//`
    `// -Minion #9567`
    `public boolean checkPassword(String password) {`
        `return password.equals("w4rm1ng_Up_w1tH_jAv4_000wYdiGTvt");`
    `}`
`}`
Paso 2.- Instalamos Java en Kali, caso de no tenerlo
sudo apt install default-jdk
Paso 3.- Compilamos el código en Java
javac VaultDoorTraining.java
Paso 4.- Ejecutamos el código en Java, lo probamos con la flag
java VaultDoorTraining

## **Referencias**
[picoCTF 2019 writeup [47] - Reverse Engineering - vault-door-training](https://www.youtube.com/watch?v=pBeAmDuYdn0&pp=ygUbcGljb2N0ZiB2YXVsdCBkb29yIHRyYWluaW5n "picoCTF 2019 writeup [47] - Reverse Engineering - vault-door-training")
