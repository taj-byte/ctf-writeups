# Local_target:bynary Medium  
Smash the stack  
Download the source [here](Local_target.c)     
Additional details will be available after launching your challenge instance  

# Solution  
バイナリ、ソースコードが渡される。  
nc saturn.picoctf.net 56202
Enter a string: 656565656565656565656565A

num is 65
You win!
picoCTF{l0c4l5_1n_5c0p3_fee8ef05}

# 基礎知識  
ASCII文字  
コンピュータが扱う文字コードの一種  

# 考えたこと
gets(input);という記述と変数を定義した場所が近かったのでバッファオーバーフローが狙えると思った  
NUMに６５を上書きできればFLAGを獲得できることがコードを読むと分かる  
最初は６５を直接バッファがあふれるまで行ったがうまく行かなかった。  
そこで、あふれる箇所に１を入力すると４９と表示されたのでASCII文字を入力する可能性を疑った。  
６５のASCII文字をしらべたとこAだとわかったので実行するとFLAGをを取得できた  
