#Write a program that takes a string as input, and counts the frequency of each word in the string, there might
#be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
#highest-frequency word

def count(word):
    #if the word contains . then we can ignore that by taking upto last position
    if word[-1] == ".":
       word = word[0:len(word) -1] 


    #if word already in dictionary, append the value count
    if word in dict1:
        dict1[word] += 1

    #if word isnt in dictionary, keep the value count a 1
    else:
        dict1.update({word: 1})


#taking the input
sentence = input("Enter the sentence \n")

#declaring an empty dictionary
dict1 = {}
#splitting the input
word_list = sentence.split()


#sending each word to count function to build dictionary
for word in word_list:
    count(word)


#printing the frequency of each word
for words  in dict1:
    print ("Number of Times", words, "in sentence :", dict1[words])

#printing the word with highest frequency in the dictionary and also printing the frequency
#first max uses get function to get key with highest values, second max just gets the highest value from dictionary
print("the highest frequency word is", max(dict1, key=dict1.get),":",max(dict1.values()))
max()


""" Use Case 1
Input : dree kashmir g20 g20 kashmir kashmir g20
Output : the highest frequency word is kashmir : 3

Here highest frequency word is kashmir and it occurs 3 times

"""

""" Use Case 2
Input: mobile samsung apple lg sony google vivo micromax micromax lg motorola micromax
Output :  the highest frequency word is micromax : 3

Here the word micromax occurs maximum times,so output shows key = micromax, value =3
"""