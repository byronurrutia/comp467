# -
# Create a file called "ingest_this.txt"
# -
# type the following in:
# This script
# Is completely awesome
# Like professor chaja
# -
# Import file and print on the console and replace every vowel with the number '9'
# ex: "This" would be "Th9s"
# -
# Show code and console output in submission (copy/paste) is fine
f = open("ingest_this.txt", "r")
text = str(f.read())
text = text.replace("a","9");
text = text.replace("e","9")
text = text.replace("i","9")
text = text.replace("o","9")
text = text.replace("u","9")
print(text)