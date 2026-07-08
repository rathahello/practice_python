import random
import string

def generate_password():
    print("\n--- 🔑 Password Generator ---")
    while True:
        try:
            length = int(input("Enter password length (min 4): "))
            if length < 4:
                print("Password must be at least 4 characters long.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Combine different character sets
    all_chars = (
        string.ascii_letters + string.digits + "!@#$%^&*"
    )

    # Ensure the password has a mix of characters by using choices
    password = "".join(random.choices(all_chars, k=length))
    print(f"Generated Password: {password}")