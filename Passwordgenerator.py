import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please enter a positive integer for the password length.")
                continue

            password = generate_password(length)
            print(f"Generated Password: {password}")

            break  # Exit the loop after successfully generating a password

        except ValueError:
            print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
