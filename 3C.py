a = eval(input("Enter the value of a: "))
b = eval(input("Enter the value of b: "))
c = eval(input("Enter the value of c: "))

if a!=0:
    d = b*b-4*a*c
    if d==0:
        r1=r2=(-b)/(2*a)
        print("Roots are real and equal\nRoots are: ",r1,r2)
    elif d>0:
        r1 = (-b+(d)**0.5)/(2*a)
        r2 = (-b-(d)**0.5)/(2*a)
        print("Roots are real and unequal\nRoots are: ",round(r1,2),round(r2,2))
    else:
        r1 = (-b+(d)**0.5)/(2*a)
        r2 = (-b-(d)**0.5)/(2*a)
        r1=complex(round(r1.real,2),round(r1.imag,2))
        r2=complex(round(r2.real,2),round(r2.imag,2))
        print("Roots are not real and not equal\nRoots are: ",r1,r2)
else:
    print("Roots are imaginary")