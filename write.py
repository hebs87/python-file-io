# Write to a file - access mode of 'w' means we want to write, instead of read
# Append to file - access mode of 'a' means append
f = open('newfile.txt', 'a')
# Variable containing list of strings
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
# Variable using the .join method to join the list of strings using the specified character (can be anything, even line breaks)
text = ' '.join(lines)
# writelines() enables us to join multiple strings
f.writelines(text)
f.close()