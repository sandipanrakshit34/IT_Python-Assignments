class invalidInput(Exception):
    def __init__(self):
        print('Invalid Input')

def wellBrackted(expr):
    try:
        if expr =='' or type(expr) != str:
            raise invalidInput
        b = []
        for c in expr:
            if c == '(':
                b.append(c)
            if c == ')':
                b.pop()
    except IndexError as e:
        print(e)
    except invalidInput as e:
        print(e)

    else:
        if len(b) == 0:
            return True
        else:
            return False
        
if __name__ == '__main__':
    expr = input('Enter an Expression: ')
    if wellBrackted(expr):
        print(expr,' is well formed')
    else:
        print(expr,' is not well formed')