import books
from stats import count_words, lower_book

def get_book_text(filepath):
  with open(filepath, "r", encoding="utf-8") as f:
    return f.read()

count_words

def main():
  filepath = "books/frankenstein.txt"
  text = get_book_text(filepath)
  print(text)
  num_words = count_words(text)
  print(f"Found {num_words} total words")
  char_counts = lower_book(text)
  print(char_counts)

if __name__ == "__main__":
  main()