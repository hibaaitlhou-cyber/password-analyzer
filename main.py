import sys
from analyzer import analyze_password
from feedback import generate_feedback

def main():
    print("========================================")
    print("      PASSWORD STRENGTH ANALYZER        ")
    print("========================================")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        # Get input from the user
        password = input("Enter a password to analyze: ")
        
        # Check if the user wants to exit
        if password.lower() in ['exit', 'quit']:
            print("Exiting...")
            break
            
        if not password:
            print("Please enter a valid password.")
            continue

        # 1. Analyze the password using our Phase 1 logic
        results = analyze_password(password)
        
        # 2. Generate feedback using our Phase 2 logic
        feedback = generate_feedback(results)
        
        # 3. Display the results
        print("\n--- Analysis Results ---")
        print(f"Strength : {feedback['strength']}")
        print(f"Score    : {feedback['score']}/5")
        
        # If there are messages, print them out as a bulleted list
        if feedback['messages']:
            print("\nSuggestions for improvement:")
            for msg in feedback['messages']:
                print(f"  - {msg}")
        else:
            print("\nExcellent! Your password meets all basic criteria.")
        
        print("-" * 40 + "\n")

if __name__ == "__main__":
    main()
