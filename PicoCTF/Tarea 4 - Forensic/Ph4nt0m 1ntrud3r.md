## **Descripcion**
A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag. To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder! Find the PCAP file here [Network Traffic PCAP file](https://challenge-files.picoctf.net/c_verbal_sleep/45a9df82c8f05fd74b8547d157ae6b1be6ba783a2bad55c6f8c664e4609d88ac/myNetworkTraffic.pcap) and try to get the flag.
## **Solucion**
picoCTF{1t_w4snt_th4t_34sy_tbh_4r_f318db22}

## **Notas adicionales**
Nota hay dos formas pero se usara tshark
Paso 1  ponemos este comando y nos saldra esto 
```
┌──(kali㉿kali)-[~/Documents/Fundamentos8A/pi]
└─$ tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4"
    6   0.001804  192.168.0.2 → 192.168.1.2  TCP 52 [TCP Retransmission] 20 → 80 [SYN] Seq=0 Win=8192 Len=12 [TCP PDU reassembled in 6]
   11   0.002819  192.168.0.2 → 192.168.1.2  TCP 52 [TCP Retransmission] 20 → 80 [SYN] Seq=0 Win=8192 Len=12
   12   0.003036  192.168.0.2 → 192.168.1.2  TCP 44 [TCP Retransmission] 20 → 80 [SYN] Seq=0 Win=8192 Len=4
   14   0.002367  192.168.0.2 → 192.168.1.2  TCP 52 [TCP Retransmission] 20 → 80 [SYN] Seq=0 Win=8192 Len=12
   17   0.001388  192.168.0.2 → 192.168.1.2  TCP 52 [TCP Retransmission] 20 → 80 [SYN] Seq=0 Win=8192 Len=12
   19   0.002586  192.168.0.2 → 192.168.1.2  TCP 52 [TCP Retransmission] 20 → 80 [SYN] Seq=0 Win=8192 Len=12
   20   0.002045  192.168.0.2 → 192.168.1.2  TCP 52 [TCP Retransmission] 20 → 80 [SYN] Seq=0 Win=8192 Len=12

```
 Paso 2: se agrega ahora esto es por lo tiempo
```
 ┌──(kali㉿kali)-[~/Documents/Fundamentos8A/pi]
└─$ tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e frame.time
2025-03-05T22:32:03.856929000-0500
2025-03-05T22:32:03.857944000-0500
2025-03-05T22:32:03.858161000-0500
2025-03-05T22:32:03.857492000-0500
2025-03-05T22:32:03.856513000-0500
2025-03-05T22:32:03.857711000-0500
2025-03-05T22:32:03.857170000-0500
```

Paso 3: Este es el de los datos
```
┌──(kali㉿kali)-[~/Documents/Fundamentos8A/pi]
└─$ tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e frame.time -e tcp.segment_data    
2025-03-05T22:32:03.856929000-0500      657a46305833633063773d3d
2025-03-05T22:32:03.857944000-0500      4d7a45345a4749794d673d3d
2025-03-05T22:32:03.858161000-0500      66513d3d
2025-03-05T22:32:03.857492000-0500      587a4d3063336c6664413d3d
2025-03-05T22:32:03.856513000-0500      63476c6a62304e5552673d3d
2025-03-05T22:32:03.857711000-0500      596d68664e484a665a673d3d
2025-03-05T22:32:03.857170000-0500      626e52666447673064413d3d


```

Paso 4: para la cuarta columna
```
┌──(kali㉿kali)-[~/Documents/Fundamentos8A/pi]
└─$ tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e frame.time -e tcp.segment_data | sort -k4
2025-03-05T22:32:03.856513000-0500      63476c6a62304e5552673d3d
2025-03-05T22:32:03.856929000-0500      657a46305833633063773d3d
2025-03-05T22:32:03.857170000-0500      626e52666447673064413d3d
2025-03-05T22:32:03.857492000-0500      587a4d3063336c6664413d3d
2025-03-05T22:32:03.857711000-0500      596d68664e484a665a673d3d
2025-03-05T22:32:03.857944000-0500      4d7a45345a4749794d673d3d
2025-03-05T22:32:03.858161000-0500      66513d3d
```

Paso 5: ejecutando esto ya nos dara la bandera..
```
tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e frame.time -e tcp.segment_data | sort -k4 | awk '{print $6}' | xxd -p -r | base64 -d
```

## **Referencias**
picoCTF 2025 - [ Forensic ] - Ph4nt0m 1ntrud3r - https://www.youtube.com/watch?v=_YKC5Smffeg