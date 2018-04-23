plaintext = "abcde"
cipher = ""

for char in plaintext:
    # a = 97, z = 122   
    new_char = ord(char) + 3
    if new_char > 122:
        numbers_after_z = new_char - 122        
        new_char = 96 + numbers_after_z
    
    new_char = chr(new_char)
    cipher += new_char

print(cipher)