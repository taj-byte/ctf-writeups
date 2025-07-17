# flag_leak:bynary Medium  
Story telling class 1/2  

Additional details will be available after launching your challenge instance.  
Download the source [here](flag_leak.c)  

# Solution  
バイナリ、ソースコードが渡される。  
Tell me a story and then I'll tell you one >> %36$p、%37$p、%38$p、%39$p、%40$p,%41$p,%42$p,%43$p,%44$p,%45$p  
Here's a story -   
0x6f636970、0x7b465443、0x6b34334c、0x5f676e31、0x67346c46,0x6666305f,0x3474535f,0x395f6b63,0x30366635,0x7d373136  

# 考えたこと  
readflag(flag, FLAGSIZE);の結果がスタックポインタに積まれていることがGDBでわかった。
printf(story);からFSBが使えることが分かるので、0x6f636970という記述がでるまで%n$pを繰り返し行った。結果36番目に出てきたのでここからFLAGに復号できると考えた。chyberchefでFROM　HEXを行い、Swap endiannessでリトルエンディアンに整えることでFLAGを取得できた。