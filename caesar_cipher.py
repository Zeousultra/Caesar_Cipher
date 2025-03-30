# Enhanced Caesar Cipher Encryption/Decryption Tool

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice! Please enter 'e' to encrypt or 'd' to decrypt.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value: "))
    except ValueError:
        print("Shift value must be an integer.")
        return

    mode = 'encrypt' if choice == 'e' else 'decrypt'
    output = caesar_cipher(message, shift, mode)

    print(f"\n{'Encrypted' if mode == 'encrypt' else 'Decrypted'} Message: {output}")

if __name__ == "__main__":
    main()
