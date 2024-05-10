import string
import random
pass_len = int(input("Enter the length of password you would like to enter: "))
print("Choose characters from the following \n 1.Letters\n 2.Digits\n 3.Special symbols\n 4.Exit")
charlist =""
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        charlist = charlist + string.ascii_letters
    elif choice == 2:
        charlist = charlist + string.digits
    elif choice == 3:
        charlist = charlist + string.punctuation
    elif choice == 4:
        break
    else:
        print("Invalid option select in between (1-4)")

gen_password = []
for i in range(pass_len):
    rand_chars = random.choice(charlist)
    gen_password.append(rand_chars)

print("The generated random password is:"+"".join(gen_password))