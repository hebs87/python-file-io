#re library for regular expressions
import re

#collections library - allows us to count the occurrences of words
import collections

#Read everything into a strig called text, use the read() method and have it all in lowercase
text = open('book.txt').read().lower()
# Use the re library's findall() method to read all the words in the file
# \w+ - \w denotes characters that are not whitespace, + denotes one or more, so we count anything with one or more chars that are not whitespace as a word
words = re.findall('\w+', text)
# Use Counter() method from our collections library and use most_common() to get the 10 most common words
print(collections.Counter(words).most_common(10))