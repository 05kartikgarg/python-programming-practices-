#13.Write a python program to check result of student(pass or fail).
total_marks=0
hindi=float(input("Enter the marks of Hindi out of 100:"))
english=float(input("Enter the marks of English out of 100:"))
maths=float(input("Enter the marks of Maths out of 100:"))
social_science=float(input("Enter the marks of Social Science out of 100:"))
science=float(input("Enter the marks of Science out of 100:"))
total_marks+=hindi+english+maths+social_science+science
per=total_marks*(100/500)
if per>0 and per<=33:
    print("FAIL")
elif per>33 and per<=100:
    print("PASS")
