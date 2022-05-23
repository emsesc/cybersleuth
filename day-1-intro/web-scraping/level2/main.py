import urllib.request
import re

url = "www.google.com"

# A simple function that uses the pattern to "parse" the string we want
def getWord(pattern, html):
  result = re.findall(pattern, html)
  return result[0]

# This is code that gets the HTML version of the website.
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")

# Use getWord() to scrape the part of the website that you want!

  
  