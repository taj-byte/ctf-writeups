# heap_only_1:bynary Medium  
Here is a binary that has enough privilege to read the content of the flag file but will only let you know its hash. If only it could just give you the actual content!  

Additional details will be available after launching your challenge instance.  

# Solution  
ssh接続して、flaghasherというファイルを分析する  
ctf-player@pico-chall$ ls -l  
total 20  
-rwsr-xr-x 1 root root 18312 Mar  6 03:44 flaghasher  
ctf-player@pico-chall$ ln -s /usr/bin/cat md5sum  
ctf-player@pico-chall$ export PATH=".:$PATH"  
ctf-player@pico-chall$ ./flaghasher  
Computing the MD5 hash of /root/flag.txt....   

picoCTF{...}  


# 基礎知識  
ハッシュ
任意の長さのデータを固定長の値（ハッシュ値）に変化させる関数（ハッシュ関数）を使って得られる値  

コマンド  
ls：ファイルやディレクトリを一覧表示する
例：ls　[オプション] [パス]  
オプション　−l：詳細を表示（権限、所有者、サイズ、日時など）  
ln：ファイルやディレクトリのリンクを作成する
例：ln　[オプション]　[対象ファイル]　[リンク名]  
オプション　−S：シンボリックリンクを作成する（パス情報だけを持つ特殊ファイル）  
export：シェル変数を環境変数として子プロセスに引き継がせる
例：export　[オプション] [変数名]  
type：指定したファイルやコマンドのパスや種類を表示する
例：type　[オプション]　[対象ファイル]

# 考えたこと    
フラグファイルの内容を読み取る権限があることがわかった  
なので、lsコマンドを使って権限を調べた  
flaghasherを実行したが、ハッシュ値が表示されるだけだった  
ghidraを使って、分析をおこなうとmd5sumがハッシュ化してるのがわかった     
catコマンドやgrepコマンドなどでハッシュ化する前の値を表示できたないか試したができなかった  

その後、特に進展なかったので諦めた  
teturou様のwriteupを参考にし、自分でも試したところ同じように解けました  
[参考にしたwriteup](https://zenn.dev/tetsurou/articles/6fe4d41a3f6f48#hash-only-1---100pt)  