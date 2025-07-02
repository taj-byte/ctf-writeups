# heap_1:binary Medium  
Can you control your overflow?   
Download the source [here](heap_1.c)  

Additional details will be available after launching your challenge instance.  

# Solution  
バイナリとソースコードが渡される  
Welcome to heap1!  
I put my data on the heap so it should be safe from any tampering.  
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.  

Heap State:  
+-------------+----------------+  
[*] Address   ->   Heap Data     
+-------------+----------------+  
[*]   0x5f5a321ba2b0  ->   pico  
+-------------+----------------+  
[*]   0x5f5a321ba2d0  ->   bico  
+-------------+----------------+  

1. Print Heap:		(print the current state of the heap)  
2. Write to buffer:	(write to your own personal block of data on the heap)  
3. Print safe_var:	(I'll even let you look at my variable on the heap, I'm confident it can't be modified)  
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
picoCTF{starting_to_get_the_hang_9e9243f9}  

# 基礎知識  
バッファオーバーフロー
プログラムが確保したメモリ領域（バッファ）を超えてデータを書き込んでしまう現象

# 考えたこと    
コードを読むと「input_data」と「safe_var」が近い距離で定義されているのでバッファオーバーフローが狙えると思った。また、check_winが起動したときにsafe_varにpicoが定義されていたらクリアできると考えた。
実行したところフラグを取得できた