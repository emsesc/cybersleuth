import zipfile, itertools

# We have received intel that the hacker group has increased the level of security on their zipfiles! They have made their o's into 0's and e's into 3's. Also, we know that they added 3 numbers at the end.

fileName = "strangeZip.zip"

numbers = "0123456789" # Combinations out of these numbers!
lockedFile = zipfile.ZipFile(fileName)

with open("words.txt", "r") as wordList:
  # Let's OPEN and then LOOP through the word list 
  for line in wordList:
    # Let's loop through all possible combinations of the numbers
    for combo in itertools.product(numbers, repeat = 3):
      password = line.strip("\n").replace("e", "3").replace("o", "0") + ''.join(combo)
      # Here, we replace the e's and the o's, along with appending the combination of numbers at the end
      print("Trying: " + password)
      # We want to remove the "newline" from the line in the file
      try:
        lockedFile.extractall(pwd = password.encode())
        print("-"*20)
        print("Found our password: " + password)
        # If we are SUCCESSFUL in extracting the file, let's exit the ENTIRE program and print out the password.
        exit(0)
      except Exception as e:
        print(e)
        pass