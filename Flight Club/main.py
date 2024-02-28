from sheety import User

print("Welcome to the Flight Club")
f_name = input("What is your first name? ")
l_name = input("What is your last name? ")

email_1 = "email1"
email_2 = "email2"

while email_1 != email_2:
    email_1 = input("What is your email? ")
    if email_1 == "quit" or email_1 == "exit":
        exit()
    email_2 = input("Please verify your email: ")
    if email_2 == "quit" or email_2 == "exit":
        exit()

    print("OK. You're in the Flight Club!")

    user = User()
    user.add_new_row(f_name=f_name, l_name=l_name, email=email_1)