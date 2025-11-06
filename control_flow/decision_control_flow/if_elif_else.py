mathematics = int(input("enter marks for mathematics?"))
english = int(input("enter average_marks for english"))
kiswahili = int(input("enter marks for kiswahili"))
science = int(input("enter marks for science"))

total = mathematics + english + kiswahili + science

average_marks = total/4 # 40

if average_marks>20 and average_marks<30:
    print("average grade is D-")
elif average_marks>=30 and average_marks<=40:
    print("average grade is D")

elif average_marks>=40 and average_marks<=50:
    print("average grade is D+")
elif average_marks>50 and average_marks<=60:
    print("average grade is C")
elif average_marks>60 and average_marks<70:
    print("average grade is B")
elif average_marks>70 and average_marks<80:
    print("average grade is B+")
elif average_marks>80 and average_marks<100:
    print("average grade is A")
else:
    print("try again")