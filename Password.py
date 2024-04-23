import random
import string

def generate_password(length):
    """
    Generates a random password of the specified length.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            print("Invalid input. Please enter a positive integer.")
            return
        generated_password = generate_password(password_length)
        print(f"Generated password: {generated_password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
