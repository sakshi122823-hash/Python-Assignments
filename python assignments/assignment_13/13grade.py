def display_grade(n):
    if n >= 75:
        print("passed with distingtion ")
    elif n >= 60:
        print("passed with first class")
    elif n >= 50:
        print("passed with second class")
    elif n <= 50:
        print("failed")
    else:
        print("invalid credentials")

grade = int(input("enter the marks : "))
if __name__=="__main__":
    display_grade(grade)









