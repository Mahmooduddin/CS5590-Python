#Ask user to enter sentence, split the sentence with whitespace
string = input("Enter a sentence: ").split(' ')
#assign the sentence as set
string_set = set(string)
#sort the string and join whitespace between words.
print(' '.join(sorted(string_set)))