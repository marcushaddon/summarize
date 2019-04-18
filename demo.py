"""Demonstrate summarization."""

from src.summarize import summarize

text = None

with open('resources/ex.txt', 'r') as infile:
    text = infile.read()


print("ORIGINAL TEXT:\n\n")
print(text + "\n--------------\n\n")

summary = summarize(text)



