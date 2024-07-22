class A:
    def __init__(self):
        print("class A object created")
    def show(self):
        print("Showing class A")
    def __repr__(self):
        return "I am a class A object"
    def __del__(self):
        print("Class A object deleted")

class B:
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
        print(f"Class B object created with {self.val1} and {self.val2}")
    def show(self):
        print(f"Showing Class B with {self.val1} and {self.val2}")

class E(A,B):
    def __init__(self, x=None, y=None):
        if x is None and y is None:
            print("Class E object created")
        if x is not None and y is not None:
            self.val1 = x
            self.val2 = y
            print(f"Class E object created with", self.val1, " and ", self.val2)
    def show(self):
        try:
            print("Showing Class E with", self.val1, " and ", self.val2)
        except AttributeError:
            print("Showing Class E")

e1 = E()
e2 =E(500,600)
e1.show()
e2.show()