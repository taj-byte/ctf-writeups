# PIE_TIME_2:Binary Medium  
Can you try to get the flag? I'm not revealing anything anymore!!  

Additional details will be available after launching your challenge instance.  

# 考えたこと    
printf関数にデータがそのまま入っていたので、fsbが狙えると思った　　
それ自体はうまく行ったが、PIEが有効なため実行時のメイン関数の位置がわからなかった。　　
一旦、実行時のアドレスの調査をやめて、WIN関数とのオフセットを調べた　　
結果、オフセットが215で有ることはわかった　　
しかし、メイン関数のアドレスが結局わからず諦めた　　
ただ、まだ理屈が理解出来ていないので今回は詳細を省きます
teturou様のwriteupを参考にし、自分でも試したところ同じように解けました  　　
[参考にしたwriteup](https://zenn.dev/tetsurou/articles/6fe4d41a3f6f48#hash-only-1---100pt) 　　