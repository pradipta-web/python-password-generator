# Python Password Generator 🔐

A Python-based password generator that creates secure random passwords using customizable length and character combinations.

This project is designed to help users generate strong passwords using uppercase letters, lowercase letters, numbers, and special characters.

## 🚀 Features

- **Secure Password Generation** – Uses Python's `secrets` module for cryptographically secure random generation.
- **Custom Password Length** – Generate passwords with a length of 1–128 characters.
- **Uppercase Letters** – Include uppercase characters (A-Z).
- **Lowercase Letters** – Include lowercase characters (a-z).
- **Numbers** – Include numeric characters (0-9).
- **Special Characters** – Include symbols such as @, #, $, and %.
- **Input Validation** – Handles invalid inputs and password configurations.

## 🛠️ Technologies Used

- Python 3
- secrets
- string

## 📋 Requirements

- Python 3.10 or later.
- Windows or Linux operating system.

## 📥 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/pradipta-web/python-password-generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-password-generator
   ```

3. Run the application:

   **Windows:**
   ```bash
   py main.py
   ```

   **Linux:**
   ```bash
   python3 main.py
   ```

## 💻 Usage

1. Run the Python application.
2. Enter your desired password length.
3. Choose which character types to include.
4. The application will generate a random password.
5. Copy the generated password and store it securely.

### Example Output

```text
=============================================
          PYTHON PASSWORD GENERATOR
=============================================

Enter password length: 16

Include uppercase? (y/n): y
Include lowercase? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

=============================================
GENERATED PASSWORD:
=============================================

aB7@kP9#mX2$vL5q

Password Length: 16
Password Status: Generated Successfully
=============================================
```

*Note: The generated password above is only an example.*

## 📚 Learning Objectives

This project helps improve practical knowledge of:

- Python programming.
- Random password generation.
- Cryptographically secure randomization.
- Python Standard Library.
- Input validation.
- Basic application development.

## 🔒 Security Notes

- Generated passwords should be stored securely.
- Avoid reusing the same password across multiple accounts.
- Never share your passwords with others.

## 👨‍💻 Author

**Pradipta Raditya**

GitHub: [@pradipta-web](https://github.com/pradipta-web)

---

*Built to explore Python programming and password security.*