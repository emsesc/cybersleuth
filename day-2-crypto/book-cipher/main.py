# paragraph, sentence, word
# (1, 5, 31)
# (1, 9, 40)
# (1, 1, 6)
# (7, 4, 16)

# We want the user to be able to keep entering numbers to find the next word.
while True:
  print("To quit, type in 'q' at anytime.")
  pNum = input("Please enter the paragraph number: ")
  if (pNum == "q"):
    break
    # If the user enters the letter "q," we will stop asking for input.
  sNum = input("Please enter the sentence number: ")
  if (sNum == "q"):
    break
  wNum = input("Please enter the word number: ")
  if (wNum == "q"):
    break
  
  file = open("book.txt","r")
  book = file.read()
  # We are opening the book that we are pulling words from.
  
  punc = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''
  # The period "." is not included because we need it to differentiate between sentences!
  
  stripPunc = ""

  # We are removing punctuation from the book so we will receive words without commas, etc.
  for char in book:
      if char not in punc:
           stripPunc = stripPunc + char

  # Here, we are splitting the book based on how things are separated in paragraphs, sentences, and words.
  # The expression number - 1 gives the correct index of the paragraph, sentence, or word.
  p = stripPunc.split('\n\n')[int(pNum) - 1]
  s = p.split('. ')[int(sNum) - 1]
  w = s.split(' ')[int(wNum) - 1]
  
  print("At paragraph number " + pNum + ", sentence number " + sNum + ", and word number " + wNum + ", we found the word '" + w + "'")
  print("\n" + "="*20)
