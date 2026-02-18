## **Descripcion**
#### Description

Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_atlas/6/challenge.zip)

`ssh -p 61562 ctf-player@atlas.picoctf.net`Using the password `6dd28e9b`. Accept the fingerprint with `yes`, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!
## **Solucion**
Se metio al servidor 
```
Alexander_Calderon-picoctf@webshell:~$ ssh -p 61562 ctf-player@atlas.picoctf.net
ctf-player@atlas.picoctf.net's password: 
Permission denied, please try again.
ctf-player@atlas.picoctf.net's password: 
Permission denied, please try again.
ctf-player@atlas.picoctf.net's password: 
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 450
Lower! Try again.
Enter your guess: 350
Lower! Try again.
Enter your guess: 278
Lower! Try again.
Enter your guess: 260
Lower! Try again.
Enter your guess: 235
Lower! Try again.
Enter your guess: 200
Higher! Try again.
Enter your guess: 215
Higher! Try again.
Enter your guess: 220
Lower! Try again.
Enter your guess: 218
Higher! Try again.
Enter your guess: 219
Congratulations! You guessed the correct number: 219
Here's your flag: picoCTF{g00d_gu355_de9570b0}
Connection to atlas.picoctf.net closed.
```
picoCTF{g00d_gu355_de9570b0}
## **Notas adicionales**
Se trato de encontrar el numero del 1 al 100.



