def project(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            code = ord(char) + shift_amount
            if char.islower():
                if code > ord('z'):
                    code -= 26
                elif code < ord('a'):
                    code += 26
            elif char.isupper():
                if code > ord('Z'):
                    code -= 26
                elif code < ord('A'):
                    code += 26
            encrypted_text += chr(code)
        else:
            encrypted_text += char
    return encrypted_text

def project_decrypt(text, shift):
    return project(text, -shift)

def main():
    print("Caesar Cipher Algorithm")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").upper()
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'E':
        encrypted_text = project(text, shift)
        print(f"Encrypted message: {encrypted_text}")
    elif choice == 'D':
        decrypted_text = project_decrypt(text, shift)
        print(f"Decrypted message: {decrypted_text}")
    else:
        print("Invalid choice! Please choose 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
