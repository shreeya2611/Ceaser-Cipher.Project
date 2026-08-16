def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
choice = input("Type E for encryption or D for decryption: ").upper()

if choice == "E":
    print("Encrypted message:", encrypt(message, shift))

elif choice == "D":
    print("Decrypted message:", decrypt(message, shift))

else:
    print("Invalid choice")