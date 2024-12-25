from random import *
def generate_password(length,name):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&','*']
    if length <= 5 and length > 0:
        n=length
        pwd_chars=[choice(letters) for i in range(0,n//2)]
        for j in range(n//2,n-1):
            pwd_chars.append(randint(0,9))
        pwd_chars.append(choice(symbols))
        password = ""
        for character in pwd_chars:
            character=str(character)
            password+=character
        return password
    elif length>0:
        symbols = ['!', '#', '$', '%', '&','*']
        password=""
        n=length

        if length>len(name)+1:
            password+=name.lower()
            pwd_chars = []
            for j in range(len(name) // 2, n - 6):
                pwd_chars.append(str(randint(0, 9)))
            pwd_chars.append(choice(symbols))
            for character in pwd_chars:
                character = str(character)
                password += character
            return password

        else:
            for i in range(0,len(name)//2 ) :
                password += name[i]
            pwd_chars=[]
            for j in range(len(name)//2,n-1):
                pwd_chars.append(str(randint(0,9)))
            pwd_chars.append(choice(symbols))
            for character in pwd_chars:
                character=str(character)
                password+=character
            return password

    else:
        print("Enter valid password length")

if __name__=="__main__":
    name = input("Enter your name : ")
    length = int(input("Enter length of the password to be formed "))
    password = generate_password(length,name)
    print(f"Password : {password}")


