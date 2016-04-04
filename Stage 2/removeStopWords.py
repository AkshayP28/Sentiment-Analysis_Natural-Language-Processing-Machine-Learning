""" Program to remov all stop-words from the reviews given a list of stop-words """

""" Function to check if a given word is a stop-word """
def checkIfStopWord(word):
    stopwords = open('C:\Users\hp\Desktop\NLP\stopwords.txt', 'r')
    for line in stopwords:
        for s_word in line.split():
            if word.lower() == s_word:
                return True
                break
    return False


""" Function to remove non-alphanumeric terms """
def removeNonAlpha(word):
    newWord=""
    for letter in word:
        if letter.isalpha() or letter=="+" or letter=="-":
            newWord+=letter
        else:
            continue
    return newWord

""" Main function to remove stop words """
def removeStopWords():
    reviews = open('C:/Users/hp/Desktop/NLP/data.txt', 'r')
    reviewsEdited = open('C:/Users/hp/Desktop/NLP/reviewsEdited.txt', 'w')

    editedLine=''
    for line in reviews:
        for word in line.split():
            if not checkIfStopWord(word):
                editedWord=removeNonAlpha(word)
                editedLine+=str(editedWord.lower())+" "
        reviewsEdited.write(editedLine+"\n")
        editedLine=''

removeStopWords()
