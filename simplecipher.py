class encript:

    def __init__(self): 
        hex_ch = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        self.hex_ch = hex_ch
        
    def hex(self, text: str):
        ch = []
        for c in text:
            ch.append(int(ord(c) / 16))
            ch.append(ord(c) % 16)
        res = "".join(self.hex_ch[ch[i]] for i in range(len(ch)))
        return res
    
    def caesar(self, text: str, shift: int):
        res = ""
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                res += chr((ord(char) + shift - 65) % 26 + 65)
            elif char.islower():
                res += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                res += char
        return res
    
class decrypt:

    def __init__(self):
        hex_ch = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        self.hex_ch = hex_ch

    def hex(self, text: str):
        n = []
        for c in text:
            n.append(self.hex_ch.index(c))
        res = "".join(chr(((n[i] * 16) + n[i+1])) for i in range(0,len(n),2))
        return res
    
    def caesar(self, text: str, shift: int):
        shift = (shift - (shift * 2))
        res = ""
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                res += chr((ord(char) + shift - 65) % 26 + 65)
            elif char.islower():
                res += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                res += char
        return res