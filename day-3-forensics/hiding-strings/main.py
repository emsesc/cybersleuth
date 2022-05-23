def readImage():
  # This is a simple function that prints out the binary data of the image
  with open("picture.jpeg", "rb") as myFile:
    data = myFile.read()
    print(data)
    myFile.close()

# We append the "secret message" to the end of this picture file
with open("picture.jpeg", "a") as myFile:
  myFile.write("This is a very secret message...")
  myFile.close()

readImage()

# https://gchq.github.io/CyberChef/
# Try looking at what the picture looks like BEFORE and AFTER you append a message
# Try looking at what the picture's binary information looks like BEFORE and AFTER you append a message