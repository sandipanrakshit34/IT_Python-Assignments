class B:
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
        print(f"Class B object created with {self.val1} and {self.val2}")
    def show(self):
        print(f"Showing Class B with {self.val1} and {self.val2}")

class C(B):
    def __init__(self,val1,val2,val3):
        super().__init__(val1,val2)
        self.val3 = val3
        print(f"Class C object created with {self.val1}, {self.val2} and {self.val3}")
    def show(self):
        super().show()
        print(f"Showing Class C with {self.val1}, {self.val2} and {self.val3}")
        
class D(C):
    def __init__(self,val1,val2,val3,val4):
        super().__init__(val1,val2,val3)
        self.val4 = val4
        print(f"Class D object created with {self.val1}, {self.val2}, {self.val3} and {self.val4}")
    def show(self):
        super().show()
        print(f"Showing Class D with {self.val1}, {self.val2}, {self.val3} and {self.val4}")
# a= A()
# a.show()
# print(a)
# print(dir(a))
# del a
# # print(a)

# b = B(10,20)
# b.show

# c  = C(100,200,300)
# c.show()

d = D(1000,2000,3000,4000)
d.show()