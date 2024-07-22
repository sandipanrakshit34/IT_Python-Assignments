leapyear = filter(lambda x: ((x%400==0) or (x%100 != 0 and x%4 ==0)), range(2022,3001))
print(list(leapyear))