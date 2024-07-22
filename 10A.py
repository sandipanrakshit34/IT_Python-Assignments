class A:
    def __init__(self):
        print("class A object created")
    def show(self):
        print("Showing class A")
    def __repr__(self):
        return "I am a class A object"
    def __del__(self):
        print("Class A object deleted")

a = A()
a.show()
print(a)
print(dir(a))
del a