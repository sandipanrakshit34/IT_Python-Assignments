class InvalidInput(Exception):
    def __init__(self):
        print("Invalid input. Value of rotation is greater than length of list")
class EmptyList(Exception):
    def __init__(self):
        print("Invalid input . The list is empty")
def rotatelist(L,n=0):
    try:
        if(L==[]):
            raise EmptyList
        if abs(n)>len(L):
            raise InvalidInput
        if(n<0):
            return L[abs(n):]+L[:abs(n)]
        else:
            return L[-n:]+L[:-n]
        
    except EmptyList as e:
        print(e,end="")
        return L
L = input("Enter a list: ").split()
L= [int (i) for i in L]
n = int(input("Enter the number of rotaions: "))
rotated = rotatelist(L,n)
print("Original list: ",L)
print("Rotated list: ",rotated)






# class RotationError(Exception):
#     pass

# def rotateList(lst, rotations=0):
#     try:
#         if not lst:
#             raise RotationError("The list cannot be empty")

#         n = len(lst)
#         if abs(rotations) >= n:
#             raise RotationError("Number of rotations must be less than the number of elements in the list")

#         if rotations >= 0:
#             rotations = rotations % n
#             new_lst = lst[-rotations:] + lst[:-rotations]
#             rotation_type = "#Right Rotation"
#         else:
#             rotations = abs(rotations) % n
#             new_lst = lst[rotations:] + lst[:rotations]
#             rotation_type = "#Left Rotation"

#         print(f"{new_lst} {rotation_type}")
#         return new_lst
#     except Exception as e:
#         raise RotationError(str(e))

# try:
#     input_str = input("Enter the list and the number of rotations: ")
#     input_list, input_rotations = eval(input_str)
#     result = rotateList(input_list, input_rotations)
# except RotationError as e:
#     print(e)
# except SyntaxError:
#     print("Invalid input format. Please provide the list and rotations in the correct format.")