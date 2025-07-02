# PIE TIME:Binary easy
Can you try to get the flag? Beware we have PIE!  
Additional details will be available after launching your challenge instance.  

Download the source [here](PIE_TIME.c).  

# Solution  
バイナリ、ソースコードが渡される。  
$ nc rescued-float.picoctf.net 54602  
Address of main: 0x5cec56a3133d  
Enter the address to jump to, ex => 0x12345: 5CEC56A312A7  
Your input: 5cec56a312a7  
You won!  
picoCTF{...}  

基礎知識  
PIE（Position Independent Executable（位置非依存実行ファイル））  
実行時にメモリ上のどこに配置されても動作するように作られたバイナリのこと。  

解法  
今回は、WIN関数を呼び出す必要があるが、PIEのため実行時のアドレスが毎回違う。  
だが、静的な状態の互いのアドレスの間隔は同じ。  
だから、実行時のMAIN関数のアドレスからWIN関数との間隔分減算すれば、WIN関数のアドレスを導き出せる  

使用ツール  
Ghidra