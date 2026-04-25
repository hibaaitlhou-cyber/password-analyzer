# Password Strength Analyzer 🔒

A professional, Python-based CLI application that analyzes the strength of user passwords based on multiple security criteria and provides detailed feedback for improvement.

## 🚀 Features

- **Length Check**: Ensures passwords are at least 8 characters long.
- **Complexity Analysis**: Uses Regular Expressions (Regex) to detect:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- **Scoring System**: Rates passwords on a 0-5 scale.
- **Dynamic Feedback**: Provides exact instructions on how the user can improve their password if it is weak.

## 🛠️ Technology Stack

- **Language**: Python 3
- **Libraries**: `re` (Built-in Regex module), `sys`

## 📂 Project Structure

```text
password-analyzer/
│
├── main.py        # The entry point of the application (User Interface)
├── analyzer.py    # Core Regex logic for evaluating password complexity
└── feedback.py    # Generates a 0-5 score and user-friendly suggestions
```

## 💻 How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone <your-repository-url>
   ```
2. Navigate into the directory:
   ```bash
   cd password-analyzer
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## 👨‍💻 Author

Created by [Hiba Aitlhou] as a cybersecurity project to understand password entropy, brute-force vulnerabilities, and safe coding practices.
