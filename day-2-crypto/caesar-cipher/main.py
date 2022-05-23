# This is a Caesar Cipher decoder

print("Welcome to the Caesar Cipher decoder!\n")
print("="*20)

# Let's ask the user what text they want to decipher and how many times the letters were shifted FORWARD.
encoded = input("Type in the text encoded using the Caesar Cipher: ")
shifts = int(input("Type in how many times the letters were shifted forward: "))

decoded = ""

# We are looping through the encoded string from the user, character by character.
for char in encoded:
  if char.isalpha():
    # We only want to shift the character IF it is part of the alphabet.
    if char.islower():
      # Find the position of the character in the alphabet
      charPos = ord(char) - ord("a")
      # Shift the letter BACKWARD. We use modulus division because we do not want a value greater than 26.
      newPos = (charPos - shifts) % 26
      # Find the ascii value of the letter
      newDec = newPos + ord("a")
      # Convert to ascii (letter form)
      newChar = chr(newDec)
      decoded += newChar
    else:
      # We are doing the same thing here, except with uppercase letters
      charPos = ord(char) - ord("A")
      newPos = (charPos - shifts) % 26
      newDec = newPos + ord("A")
      newChar = chr(newDec)
      decoded += newChar
  else:
      decoded += char

print("="*20)
print("\nYour decoded message is: " + decoded)