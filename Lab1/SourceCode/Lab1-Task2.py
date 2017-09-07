string = str(input('Enter a string:')) # Ask user to enter string.
string=string.replace(' ','') # Replace ' ' with ,
if set(string) >= set('abcdefghijklmnopqurstuvwxyz'): # Use if condition to check if the string contains all letters of alphabets.
  print('String contains all letters of alphabet.') # If true, print string contains all letters of alphabet.
else:  # use else condition if false
  print('String does not contains all letters of alphabet.') # Print string does not contain all letters of alphabets.