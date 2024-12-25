def addition():
    more=True
    sum=0
    while(more):
        print("Add a number ")
        num=int(input())
        sum+=num
        print("Enter \n1 To continue \n2 to exit")
        choice = int(input())
        if choice==1:
            continue
        elif choice==2:
            more=False
        else:
            print("Enter valid choice")
    print(f"Sum is {sum}")

def subtraction():
    more=True
    diff=0
    while(more):
        print("Subtract a number ")
        num=int(input())
        diff-=num
        print("Enter \n1 To continue \n2 to exit")
        choice = int(input())
        if choice==1:
            continue
        elif choice==2:
            more=False
        else:
            print("Enter valid choice")

    print(f"Answer of subtraction is {diff}")


def multiplication():
    more = True
    multiply = 1
    while (more):
        print("Multiply a number ")
        num = int(input())
        multiply *= num
        print("Enter \n1 To continue \n2 to exit")
        choice = int(input())
        if choice == 1:
            continue
        elif choice == 2:
            more = False
        else:
            print("Enter valid choice")

    print(f"Multiplication of all the numbers is {multiply}")

def division():
    more = True
    div=None
    num1=int(input("Num 1 : "))
    div=num1
    while (more):
        num2=int(input("Another Num : "))
        div=div/num2
        print("Enter \n1 To continue \n2 to exit")
        choice = int(input())
        if choice == 1:
            continue
        elif choice == 2:
            more = False
        else:
            print("Enter valid choice")

    print(f"Division of all the numbers is {div}")

def calculator():
    again=True
    while(again):
        print("Enter choice : ")
        print("1. To add numbers ")
        print("2. To subtract numbers ")
        print("3. To multiply numbers ")
        print("4. To divide numbers" )
        print("5. To exit")
        choice = int(input("Enter choice : "))

        if choice == 1:
            addition()
        elif choice==2:
            subtraction()
        elif choice==3:
            multiplication()
        elif choice==4:
            division()
        elif choice==5:
            again=False
        else:
            print("Enter valid choice")

if __name__=="__main__":
    calculator()

