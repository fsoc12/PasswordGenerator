import secrets
import string
import sys

def generate_password(length, use_lower, use_upper, use_digits, use_special):
    """Generate truly random password using cryptographically secure RNG"""
    char_pool = ''
    if use_lower: char_pool += string.ascii_lowercase
    if use_upper: char_pool += string.ascii_uppercase
    if use_digits: char_pool += string.digits
    if use_special: char_pool += "!@#$%&*_+-=?"
    
    # Ensure at least one character from each selected category
    password = []
    if use_lower: password.append(secrets.choice(string.ascii_lowercase))
    if use_upper: password.append(secrets.choice(string.ascii_uppercase))
    if use_digits: password.append(secrets.choice(string.digits))
    if use_special: password.append(secrets.choice("!@#$%&*_+-=?"))
    
    # Fill remaining length
    remaining = length - len(password)
    password.extend(secrets.choice(char_pool) for _ in range(remaining))
    
    # Shuffle for random order
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def print_banner():
    """Display text banner"""
    print("=" * 55)
    print("|           SECURE PASSWORD GENERATOR           |")
    print("-" * 55 + "\n")

def main():
    """Main application function"""
    print_banner()
    
    # Password length
    while True:
        try:
            length = int(input("Enter password length (minimum 12): "))
            if length < 12:
                print("! Security recommendation: minimum 12 characters")
                continue
            break
        except ValueError:
            print("Error: please enter a valid number")
    
    # Character categories
    print("\nSelect character categories to include:")
    use_lower = input("  Lowercase letters (a-z)? [y/n]: ").lower() == 'y'
    use_upper = input("  Uppercase letters (A-Z)? [y/n]: ").lower() == 'y'
    use_digits = input("  Digits (0-9)? [y/n]: ").lower() == 'y'
    use_special = input("  Special characters (!@#$%&*)? [y/n]: ").lower() == 'y'
    
    # Validation
    if not any([use_lower, use_upper, use_digits, use_special]):
        print("\nError: you must select at least one character category!")
        sys.exit(1)
    
    # Generate password
    password = generate_password(length, use_lower, use_upper, use_digits, use_special)
    
    # Display result
    print("\n" + "=" * 55)
    print(" GENERATED PASSWORD ".center(55, '#'))
    print("=" * 55)
    print(f"\n{password}\n")
    print("=" * 55)
    print(f"Length: {len(password)} characters | Entropy: ~{length*5} bits")
    print("=" * 55)

if __name__ == "__main__":
    main()