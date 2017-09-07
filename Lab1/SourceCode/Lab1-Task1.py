freq={}  # defining freq (dictionary)
file=open('textfile.txt','r')  # open textfile.txt
string=file.readline()  # use readline to get next line of the file
for i in string.split(" "):  # split the words
   words=freq.keys()  # return list of all available keys in keys
   if i in words:  # use if condition
       freq[i]+=1  # if same word is available in words add 1
   else:  # else condition
        freq[i]=1  # the freq of word remain 1
print(freq)  # print freq{}