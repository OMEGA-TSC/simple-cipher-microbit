#Library made by Vilém Urbánek
class encript:

    def __init__(self): 
        hex_ch = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        self.hex_ch = hex_ch
        
    def hex(self, data):
        ch = []
        self.data = data
        for c in self.data:
            ch_num = ord(c)
            ch.append(int(ch_num / 16))
            ch.append(ch_num % 16)
        res = "".join(self.hex_ch[ch[i]] for i in range(len(ch)))
        return res
    
class decrypt:

    def __init__(self):
        hex_ch = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        self.hex_ch = hex_ch

    def hex(self, data):
        ch = []
        n = []
        self.data = data
        for c in self.data:
            n.append(self.hex_ch.index(c))
        for i in range(0,len(n),2):
            ch.append(((n[i] * 16) + n[i+1]))
        res = "".join(chr(ch[i]) for i in range(len(ch)))
        return res
