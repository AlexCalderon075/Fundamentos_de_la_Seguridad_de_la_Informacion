# BinHexa
## **Descripcion**

How well can you perfom basic binary operations?

Additional details will be available after launching your challenge instance.

nc titan.picoctf.net 51191

## **Solucion**
Se ingreso a nc titan.picoctf.net 51191

picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_675602ae}

`Alexander_Calderon-picoctf@webshell:~$ nc titan.picoctf.net 51191

Welcome to the Binary Challenge!"
Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.

Binary Number 1: 01001011
Binary Number 2: 11100101


Question 1/6:
Operation 1: '+'
Perform the operation on Binary Number 1&2.
Enter the binary result: 0100110000
Correct!

Question 2/6:
Operation 2: '&'
Perform the operation on Binary Number 1&2.
Enter the binary result: 01001011
Incorrect. Try again
Enter the binary result: 01000001
Correct!

Question 3/6:
Operation 3: '>>'
Perform a right shift of Binary Number 2 by 1 bits .
Enter the binary result: 1001.011

Incorrect input. Provide the right input
Enter the binary result: 11100101     
Incorrect. Try again
Enter the binary result:  01110010        
Correct!

Question 4/6:
Operation 4: '|'
Perform the operation on Binary Number 1&2.
Enter the binary result: 1111111100010000
Incorrect. Try again
Enter the binary result: 1110 1111    

Incorrect input. Provide the right input
Enter the binary result: 11101111
Correct!

Question 5/6:
Operation 5: '<<'
Perform a left shift of Binary Number 1 by 1 bits.
Enter the binary result: 10010110
Correct!

Question 6/6:
Operation 6: '*'
Perform the operation on Binary Number 1&2.
Enter the binary result: 100001100010111
Correct!

Enter the results of the last operation in hexadecimal: 4317

Correct answer!
The flag is: picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_675602ae}`

## **Notas adicionales**
Cuando se ingreso nc titan.picoctf.net 51191 
ahi se realizo una serie de  operaciones para obtener la bandera


## **Referencias**
https://www.rapidtables.com/calc/math/binary-calculator.html?num1=01001011&op=2&num2=11100101