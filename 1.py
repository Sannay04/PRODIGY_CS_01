def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar cipher.

    Args:
        text: The text to encrypt or decrypt.
        shift: The shift value (integer).
        mode: 'encrypt' or 'decrypt'.

    Returns:
        The encrypted or decrypted text.
    """

    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift if mode == 'encrypt' else ord(char) - start - shift) % 26 + start)
        else:
            shifted_char = char
        result += shifted_char
    return result

def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter the text to encrypt: ")
            try:
                shift = int(input("Enter the shift value (integer): "))
            except ValueError:
                print("Invalid shift value. Please enter an integer.")
                continue
            encrypted_text = caesar_cipher(text, shift, 'encrypt')
            print("Encrypted text:", encrypted_text)

        elif choice == '2':
            text = input("Enter the text to decrypt: ")
            try:
                shift = int(input("Enter the shift value (integer): "))
            except ValueError:
                print("Invalid shift value. Please enter an integer.")
                continue
            decrypted_text = caesar_cipher(text, shift, 'decrypt')
            print("Decrypted text:", decrypted_text)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()