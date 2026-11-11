import secrets
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):

    characters = ""
    password = []

    if use_uppercase:
        characters += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))

    if use_lowercase:
        characters += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))

    if use_numbers:
        characters += string.digits
        password.append(secrets.choice(string.digits))

    if use_symbols:
        symbols = "!@#$%^&*()-_=+"
        characters += symbols
        password.append(secrets.choice(symbols))

    if not characters:
        return None

    if length < len(password):
        return None

    for _ in range(length - len(password)):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


print("=" * 45)
print("          PYTHON PASSWORD GENERATOR")
print("=" * 45)

try:
    length = int(input("\nEnter password length: "))

    if length < 1 or length > 128:
        print("Error: Password length must be between 1 and 128.")
        raise SystemExit

    uppercase = input("Include uppercase? (y/n): ").lower() == "y"
    lowercase = input("Include lowercase? (y/n): ").lower() == "y"
    numbers = input("Include numbers? (y/n): ").lower() == "y"
    symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(
        length,
        uppercase,
        lowercase,
        numbers,
        symbols
    )

    if password:
        print("\n" + "=" * 45)
        print("GENERATED PASSWORD:")
        print("=" * 45)
        print(password)
        print("\nPassword Length:", len(password))
        print("Password Status: Generated Successfully")
        print("=" * 45)

    else:
        print("\nError: Select at least one character type")
        print("or increase the password length.")

except ValueError:
    print("\nError: Please enter a valid number.")
