class encrypt:

    def __init__(self): 
        hex_ch = "0123456789ABCDEF"
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
    
    def shuffle(self, text: str):
        res = ""
        for c in range(len(text)):
            buf = ""
            if c % 2 != 0:
                buf = text[c]
                buf += res
                res = buf
            else:
                res += text[c]
        return res  
    
    def ascii(self, text: str):
        res = ""
        for i in range(len(text)):
            res += str(ord(text[i]))
            if i < (len(text) - 1):
                res += ":"
        return res
    
class decrypt:

    def __init__(self):
        hex_ch = "0123456789ABCDEF"
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
    
    def shuffle(self, text: str):
        chars = list(text)
        res = ""
        if len(chars) % 2 != 0:
            for c in range((int(len(chars) / 2) + 1)):
                buf = ""
                if c < (int(len(chars) / 2)):
                    buf += chars[((len(chars) - 1) - c)]
                    buf += res 
                    res = buf
                buf = chars[c]
                buf += res
                res = buf
        else:
            for c in range(int(len(chars) / 2)):
                buf = ""
                buf += chars[c]
                buf += res 
                res = buf
                buf = chars[((len(chars) - 1) - c)]
                buf += res
                res = buf    
        return res  
    
    def ascii(self, text: str):
        res = ""
        chars = text.split(":")
        for c in chars:
            res += chr(int(c))
        return res