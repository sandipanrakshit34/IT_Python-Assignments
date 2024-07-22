# class A:
#     def __init__(self):
#         print("Class A object is created")
#     def show(self):
#         print("Showing class A")
#     def __repr__(self):
#         return "I am a class A object "
#     def __del__(self):
#         print("Class A object deleted")

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
        print(f"Class c object created with {self.val1}, {self.val2} and {self.val3}")
    def show(self):
        # super().show()
        print(f"Showing Class C with {self.val1}, {self.val2} and {self.val3}")
        

# a= A()
# a.show()
# print(a)
# print(dir(a))
# del a
# # print(a)

# b = B(10,20)
# b.show()

c  = C(100,200,300)
c.show()