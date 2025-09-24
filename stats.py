def count_words(text):
  words = text.split()
  return len(words)

def lower_book(text):
  text = text.lower()
  counts = {}
  for char in text:
    counts[char] = counts.get(char, 0) + 1
  return counts