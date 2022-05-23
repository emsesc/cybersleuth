import zipfile
# Import the zipfile package so we can unzip zip files

fileName = "mysterious.zip"

# Specify which zip file we're using
lockedFile = zipfile.ZipFile(fileName)

with open("words.txt", "r") as wordList:
  # Let's OPEN and then LOOP through the word list 
  for line in wordList:
    password = line.strip("\n")
    print("Trying: " + password)
    # We want to remove the "newline" from the line in the file
    try:
      lockedFile.extractall(pwd = password.encode())
      print("-"*20)
      print("Found our password: " + password)
      # If we are SUCCESSFUL in extracting the file, let's break the loop and print out the password.
      break
    except Exception as e:
      print(e)
      pass
      