# format_string_0:Binary easy  
Can you use your knowledge of format strings to make the customers happy?  

Download the source [here](format_string_0.c).  

Additional details will be available after launching your challenge instance.  

# Solution  
バイナリ、ソースコードが渡される。  

$ nc mimas.picoctf.net 54088  
Welcome to our newly-opened burger place Pico 'n Patty! Can you help the picky customers find their favorite burger?  
Here comes the first customer Patrick who wants a giant bite.  
Please choose from the following burgers: Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe  
Enter your recommendation: Gr%114d_Cheese  
Gr                                                                                                             4202954_Cheese  
Good job! Patrick is happy! Now can you serve the second customer?  
Sponge Bob wants something outrageous that would break the shop (better be served quick before the shop owner kicks you out!)  
Please choose from the following burgers: Pe%to_Portobello, $outhwest_Burger, Cla%sic_Che%s%steak  
Enter your recommendation: Cla%sic_Che%s%steak  
ClaCla%sic_Che%s%steakic_Che(null)  
picoCTF{...}  

# 基礎知識  
format_string_Attack（フォーマット文字列脆弱性）  
C言語 やそれに近い低レベル言語において発生する脆弱性で、printf 系関数にユーザー入力を直接渡すことで発生  
char name[100]; char name[100];  
scanf("%s", name); scanf("%s", name);  
printf(name); // 脆弱性がある printf("Hello, %s\n", name); // 安全  

# 考えたこと  
format_string_attackを狙おうと思った  
ただ、メニューが正しくないと発生しない仕組みだとわかったので混乱した  
ソースを見るとメニューにあることとバッファサイズが６４より大きいとフラグが得られると考えた  
メニューリストにフォーマット文字が含まれていたのでそれを入力したらフラグをゲットできた  
（フォーマット文字を入力した結果表示される文字列のサイズが６４バイトを超えることを狙った）  
