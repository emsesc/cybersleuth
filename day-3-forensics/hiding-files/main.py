# HIDING the PDF file in the PICTURE
with open("panda.jpeg", "ab") as imageFile:
  with open("gru.pdf", "rb") as pdfFile:
    data = pdfFile.read()
    pdfFile.close()
    # We just read the "binary" contents of the PDF file
  imageFile.write(data)
  # Now, we're appending the PDF file to the IMAGE file
  imageFile.close()

# https://gchq.github.io/CyberChef/#recipe=Extract_Files(false,false,false,true,false,false,false,true)
# Does the image look the same before and after? If you look at the "inside" data of the image, what's different?

# PDF file header: 25 50 44 46
with open("panda.jpeg", 'rb') as newFile:
  data = newFile.read()
  # Using the find() method, we found the index of WHERE the PDF file is located!
  index = data.find(b'\x25\x50\x44\x46')
  # We now specifically take out the portion of the IMAGE file that is actually the PDF
  data = data[index:-1]
  newFile.close()
  with open("extracted.pdf", "wb") as extractedFile:
    extractedFile.write(data)
    # We write the PDF file's data to a new file
    extractedFile.close()
    