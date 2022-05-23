import urllib.request
import re

baseUrl = "https://triplethreat.emilychen10.repl.co"

# Create an array of the three HTML files we must get words from.
urls = ["/part1.html", "/part2.html", "/part3.html"]

string = ""

# A simple function that uses the pattern to "parse" the string we want
def getWord(pattern, html):
  result = re.findall(pattern, html)
  return result[0]

# Let's loop through the urls to concatenate all the words!
for url in urls:
  response = urllib.request.urlopen(baseUrl + url)
  html = response.read().decode("utf-8")

  # It gives us a full HTML file, so let's parse the word
  newWord = getWord("<body>(.*)</body>", html)
  print("String: " + newWord)
  # Appending the word
  string += newWord
  print("New string: " + string)

# Finally, let's access the secret page with the three words together
htmlFlag = urllib.request.urlopen(baseUrl + "/" + string + ".html")
flag = htmlFlag.read().decode("utf-8")
flag = getWord("<b>(.*)</b>", flag)

print("="*20)
print("FOUND THE FLAG! " + flag)


  
  