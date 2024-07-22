basic_pay = eval(input("Enter the basic pay of the employee: "))

AGP = 0.5 * basic_pay
merged_basic = basic_pay + AGP

DA = 0.5 * merged_basic
HRA = 0.15 * merged_basic

total_salary = merged_basic + DA + HRA

print("Total Salary: ", format(total_salary,'.2f'))
