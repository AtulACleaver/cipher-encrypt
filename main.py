def encrypted(string, shift):
    ciper = ''
    for char in string:
        if char == ' ':
            ciper = ciper + char
        elif char.isupper():
            ciper = ciper + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            ciper = ciper + chr((ord(char) + shift - 97) % 26 + 97)
    return ciper


text = input("Text: ")
s = int(input("Enter the shift key: "))

print(f"The original is : {text}")
print("the encrypted message is :", encrypted(text, s))
