file = open("textfile.txt",'r') # open textfile.txt
list=[] # define list
freq = 0 # define freq=0
string = file.readline() #read each entire line from the file
while string != "": # use while condition, to look for all lines in file and stop when lines get over
    for i in string.split(" "): # split the words
        list.append(i) # append word in list
        freq = freq + 1 # add 1 to freq
    string = file.readline() #read each entire line from the file
list_words = str(list) # define list_words, which contains list of all words
def word_freq(str1): # defining word_freq
    frequency = {} #define count(dictionary)
    words = str1.split() #split words
    for word in words:  #for loop
        if word in frequency: #if condition
            frequency[word] += 1 # word repeats add 1
        else:             # else condition
            frequency[word] = 1 # frequency of word remains 1
    return frequency # return frequency value
print(word_freq(list_words)) # print words and their frequencies (dictionary)
