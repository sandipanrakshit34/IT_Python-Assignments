str = input("enter your mail ID: ")
str_split1 =str.split("@")
str_split2 =str_split1[1].split(".")
print(str_split1[0],str_split2[0].upper())