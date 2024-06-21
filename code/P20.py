def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if "A" <= char <= "Z":
            new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= char <= "z":
            new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            new_char = char
        encrypted_text += new_char
        print(f"{char} {new_char}")
    print(encrypted_text)


input_str = input().strip()
shift_amount = int(input().strip())

caesar_cipher(input_str, shift_amount)
