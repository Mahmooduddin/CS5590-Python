str = "avfc1234"
letters=0
digit=0
others=0
for i in str:
    if i.isalpha():
        print('String contains all letters of alphabet')
        letters += 1
    else:
        print('String contains ')
        others=0
print("letters",letters)
print("digits",digit)


