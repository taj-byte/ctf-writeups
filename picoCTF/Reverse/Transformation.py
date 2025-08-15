def decode_flag(encoded_flag: str) -> str:
    """暗号化されたフラグを復号化する"""
    decoded = []
    
    for char in encoded_flag:
        # 文字のコードポイントを取得
        code_point = ord(char)
        
        # 上位8ビット（元の1文字目）を取得
        char1 = chr(code_point >> 8)
        
        # 下位8ビット（元の2文字目）を取得  
        char2 = chr(code_point & 0xFF)
        
        decoded.extend([char1, char2])
    
    return ''.join(decoded)

# 使用例
encoded_flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽"
decoded = decode_flag(encoded_flag)
print(f"復号化結果: {decoded}")