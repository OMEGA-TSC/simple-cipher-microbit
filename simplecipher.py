class encrypt:

    def __init__(self): 
        hex_table = "0123456789ABCDEF"
        base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        self.base64_table = base64_table
        self.hex_table = hex_table
        
    def hex(self, text: str):
        ch = []
        for c in text:
            ch.append(int(ord(c) / 16))
            ch.append(ord(c) % 16)
        res = "".join(self.hex_table[ch[i]] for i in range(len(ch)))
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
    
    def base64(self, text: str):
        bytes = text.encode("utf-8")
        res = []
        for i in range(0, len(bytes), 3):
            buf = bytes[i:i+3]
            if len(buf) < 3:
                buf += b"\x00" * (3 - len(buf))
            values = [
            (buf[0] & 252) >> 2,
            ((buf[0] & 3) << 4) | ((buf[1] & 240) >> 4),
            ((buf[1] & 15) << 2) | ((buf[2] & 192) >> 6),
            buf[2] & 63
            ]
            values = [v + 64 for v in values]
            chars = [self.base64_table[v - 64] for v in values]
            res.extend(chars)
        res = [c if c != "A" else "=" for c in res]
        return "".join(res)
    
class decrypt:

    def __init__(self):
        hex_table = "0123456789ABCDEF"
        base64_table = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, "a": 26, "b": 27, "c": 28, "d": 29, "e": 30, "f": 31, "g": 32, "h": 33, "i": 34, "j": 35, "k": 36, "l": 37, "m": 38, "n": 39, "o": 40, "p": 41, "q": 42, "r": 43, "s": 44, "t": 45, "u": 46, "v": 47, "w": 48, "x": 49, "y": 50, "z": 51, "0": 52, "1": 53, "2": 54, "3": 55, "4": 56, "5": 57, "6": 58, "7": 59, "8": 60, "9": 61, "+": 62, "/": 63, "=": 64}        
        self.base64_table = base64_table
        self.hex_table = hex_table

    def hex(self, text: str):
        n = []
        for c in text:
            n.append(self.hex_table.index(c))
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
    
    def base64(self, text: str):
        dec_chars = []
        buf1, buf2, buf3 = 0, 0, 0
        for i in range(0, len(text), 4):
            a = self.base64_table[text[i]]
            b = self.base64_table[text[i + 1]]
            c = self.base64_table[text[i + 2]]
            d = self.base64_table[text[i + 3]]
            buf1 = (a << 2) | (b >> 4)
            buf2 = ((b & 0b1111) << 4) | (c >> 2)
            buf3 = ((c & 0b11) << 6) | d
            if text[i+2] != "=":
                dec_chars.append(buf1)
                dec_chars.append(buf2)
            if text[i+3] != "=":
                dec_chars.append(buf3)
        res = "".join([chr(b) for b in dec_chars])
        return res