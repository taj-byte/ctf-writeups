# heap_0:Binary easy  
Are overflows just a stack concern?  
Download the source [here](heap_0.c).  
Additional details will be available after launching your challenge instance.  

# Solution  
バイナリ、ソースコードが渡される。  
$ nc tethys.picoctf.net 55928  

Welcome to heap0!  
I put my data on the heap so it should be safe from any tampering.  
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.  

Heap State:  
+-------------+----------------+  
[*] Address   ->   Heap Data     
+-------------+----------------+  
[*]   0x5aa3ec26c2b0  ->   pico  
+-------------+----------------+  
[*]   0x5aa3ec26c2d0  ->   bico  
+-------------+----------------+  

1. Print Heap:		(print the current state of the heap)  
2. Write to buffer:	(write to your own personal block of data on the heap)  
3. Print safe_var:	(I'll even let you look at my variable on the heap, I'mconfident it can't be modified)  
4. Print Flag:		(Try to print the flag, good luck)  
5. Exit  

Enter your choice: 2  
Data for buffer: picopicopicopicopicopicopicopicopico  

1. Print Heap:		(print the current state of the heap)  
2. Write to buffer:	(write to your own personal block of data on the heap)  
3. Print safe_var:	(I'll even let you look at my variable on the heap, I'm confident it can't be modified)  
4. Print Flag:		(Try to print the flag, good luck)  
5. Exit  

Enter your choice: 3

Take a look at my variable: safe_var = pico  

1. Print Heap:		(print the current state of the heap)  
2. Write to buffer:	(write to your own personal block of data on the heap)  
3. Print safe_var:	(I'll even let you look at my variable on the heap, I'm confident it can't be modified)  
4. Print Flag:		(Try to print the flag, good luck)  
5. Exit  

Enter your choice: 4

YOU WIN
picoCTF{...}

# 基礎知識  
ヒープ（Heap memory）  
プログラム実行時に動的に確保されるメモリ領域  

malloc(size)  
メモリの動的確保を行う関数　（size変数分メモリを確保する）  

strcmp(X,Y)  
XとＹを比較する  

scanf("フォーマット指定子", &変数);  
ユーザーの入力を変数に格納する  

strncpy(*x,*y,z)  
文字列を指定した長さまでコピーする  
*x=コピー先の配列ポインタ *y=コピー元の文字列 z=コピーする最大文字数  

# 考えたこと  
scanfを使ってるから、バッファオーバーフローが使えると思った。  
mallocが同じ関数内に連続で並んでることから確信。  
バッファのサイズから入力できる文字数を調べたが、よくわからなかった  