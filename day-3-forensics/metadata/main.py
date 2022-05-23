from PIL import Image

image = Image.open("strangepic.png")
  
# Let's extract the metadata!
exifdata = image.getexif()
  
# Print out by looping through
for data in exifdata:
  print(exifdata.get(data))

# Done? Try exploring where this image is located: https://jimpl.com/

# Trick people by changing the metadata of a file: https://metaeditor.services.picvario.com/