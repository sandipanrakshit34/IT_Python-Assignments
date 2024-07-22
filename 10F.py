class F:
    def __init__(self,in1):
        if in1 is not None:
            if type(in1) != str:
                in1 = str(in1)
            self.in1 = in1
    def __sub__(self,other):
        rs = ''
        for c in self.in1:
            if c not in other.in1:
                rs += c
        return rs
    
s1 = F(input('Enter a string: '))
s2 = F(input('Enter a string: '))
s3 = s1 - s2
print(s3)
print(F(5)-F(3))