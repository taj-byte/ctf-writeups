# RPS:Binary Medium  
Here's a program that plays rock, paper, scissors against you.   I hear something good happens if you win 5 times in a row. The program's source code with the flag redacted can be downloaded [here](RPS.c).  

Additional details will be available after launching your challenge instance.  

# Solution  
ソースコードが渡される。   
(for _ in $(seq 5); do echo 1; echo rock paper scissors; done; echo 2) | nc saturn.picoctf.net 49853  
1  
rock paper scissors  
1  
rock paper scissors  
1  
rock paper scissors  
1  
rock paper scissors  
1  
rock paper scissors  
2  
Welcome challenger to the game of Rock, Paper, Scissors  
For anyone that beats me 5 times in a row, I will offer up a flag I found  
Are you ready?  
Type '1' to play a game  
Type '2' to exit the program  


Please make your selection (rock/paper/scissors):  
You played: rock paper scissors  
The computer played: paper  
You win! Play again?  
Type '1' to play a game  
Type '2' to exit the program  


Please make your selection (rock/paper/scissors):  
You played: rock paper scissors  
The computer played: paper  
You win! Play again?  
Type '1' to play a game  
Type '2' to exit the program  


Please make your selection (rock/paper/scissors):  
You played: rock paper scissors  
The computer played: paper  
You win! Play again?  
Type '1' to play a game  
Type '2' to exit the program  


Please make your selection (rock/paper/scissors):  
You played: rock paper scissors  
The computer played: paper  
You win! Play again?  
Type '1' to play a game  
Type '2' to exit the program  


Please make your selection (rock/paper/scissors):  
You played: rock paper scissors  
The computer played: paper  
You win! Play again?  
Congrats, here's the flag!  
picoCTF{50M3_3X7R3M3_1UCK_C85AF58A}  
Type '1' to play a game  
Type '2' to exit the program  

# 基礎知識  
シェルスクリプトのfor構文  
例：iを５回出力する
for i in `seq 5`  
do  
    echo i  
done  

strstr  
指定した文字列（*haystack）の中に、部分一致する文字列（*needle）があるか調べる  
char *strstr(const char *haystack, const char *needle);  

今回の場合  
strstr(player_turn, loses[computer_turn])  
＊player_turnの文字列にcomputer_turnが負ける文字あれば真になる  
# 考えたこと  
とりあえず、５連勝すれば良いことがわかった
コードを読むと１秒間に５連勝する必要があると考えた
しかし、手動では厳しいためECHOコマンドを使ってやろうと思ったが、最初に５回表示させるだけで終わった。（よくよく考えれば５回同じ内容を出力したいのだからループさせれば良いだけだった）
ここで、やりたいことはわかったが実現方法が思い浮かばなかったので[@kusano_kのwriteup](https://qiita.com/kusano_k/items/9eefb46db2dfdf8de922)を閲覧した
記載どうり実行したところ無事にflagを獲得できた

# 反省点
注目したポイントが間違っていたことに気づいた。
今回、１秒間に５回勝つことに注目したが、strstrが１番重要なポイントであることに解答後に気づいた。
なぜなら、じゃんけんの出す手を入力するところにrock/paper/scissorsすべてを記載すれば必ず勝てるからだ。
コードをもっと注意深く読めば気づけただけに悔しい。