# Lesson 03 Challenge Solutions
# Strings

# ⭐ Core: String explorer
sentence = "MicroPython on ESP32 is fun!"

print(f"Original:   {sentence}")
print(f"Length:     {len(sentence)}")
print(f"Uppercase:  {sentence.upper()}")
print(f"Lowercase:  {sentence.lower()}")
print(f"Starts: '{sentence[:11]}'")
print(f"Ends:   '{sentence[-4:]}'")
print(f"'ESP32' at index: {sentence.find('ESP32')}")
print(f"Word count (approx): {len(sentence.split())}")

# ⭐⭐ Extension: Username formatter
# Simulate input (hardcoded here since running on hardware without terminal)
first_name = "Maria"
last_name  = "Santos"
birth_year = 2010

current_year = 2025
age = current_year - birth_year

username = (first_name[0] + last_name).lower()
print(f"\nFirst name:  {first_name}")
print(f"Last name:   {last_name}")
print(f"Age:         {age}")
print(f"Username:    {username}")
print(f"Full name:   {first_name} {last_name}")
print(f"Initials:    {first_name[0]}.{last_name[0]}.")

# ⭐⭐⭐ Stretch: Caesar cipher (shift by 3)
def caesar_encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char   # Keep non-letters unchanged
    return result

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

message   = "Hello World"
encrypted = caesar_encrypt(message)
decrypted = caesar_decrypt(encrypted)

print(f"\nOriginal:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
print(f"Round-trip correct: {decrypted == message}")
