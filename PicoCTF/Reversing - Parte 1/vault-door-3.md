## **Descripcion**
This vault uses for-loops and byte arrays.The source code for this vault is here: [VaultDoor3.java](https://challenge-files.picoctf.net/c_fickle_tempest/caeef81009d61675ffc5fd38029a53105102ceafab8248d48f73aa4e96ea0cb6/VaultDoor3.java)
## **Solucion**
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_f66133}

## **Notas adicionales**
Paso1. Examinamos el código fuente en Java que se nos da
Paso2. Modificamos el programa en Java para revertir el anagrama con el codigo proporcionado del maestro
```
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
      //  System.out.print("Enter vault password: ");
     //   String userInput = scanner.next();
    //String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
    if (vaultDoor.checkPassword()) {
        System.out.println("Access granted.");
    } else {
        System.out.println("Access denied!");
        }
    }
    // -Minion #2671
    public boolean checkPassword() {
        String password = "jU5t_a_s1mpl3_an4gr4m_4_u_f66133";
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String flag = new String(buffer);
        System.out.println(flag);
        return true;
    }
}
```
y obtenemos la bandera.
## **Referencias**
[picoCTF 2019 writeup [49] - Reverse Engineering - vault-door-3](https://www.youtube.com/watch?v=B5y2spPIXj0&pp=ygUUcGljb2N0ZiB2YXVsdCBkb29yIDM%3D "picoCTF 2019 writeup [49] - Reverse Engineering - vault-door-3") 