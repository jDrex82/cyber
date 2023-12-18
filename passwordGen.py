import random
import string

def generate_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_passwords(accounts_passwords):
    with open("passwords.txt", "w") as file:
        for account, password in accounts_passwords.items():
            file.write(f"{account}: {password}\n")

def main():
    accounts_passwords = {}
    continue_program = True

    while continue_program:
        account = input("Enter the account for which you want to generate a password (type 'quit' to exit): ")

        if account.lower() == 'quit':
            save = input("Do you want to save passwords to a text file? (yes/no): ")
            if save.lower() == 'yes':
                save_passwords(accounts_passwords)
                print("Passwords saved to passwords.txt")
            else:
                continue_program = False
        else:
            password = generate_password()
            accounts_passwords[account] = password

            print(f"\nAccount: {account}")
            print(f"Generated Password: {password}\n")

if __name__ == "__main__":
    main()
