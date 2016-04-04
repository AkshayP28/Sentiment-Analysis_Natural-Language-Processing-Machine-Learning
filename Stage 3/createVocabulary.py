""" Program to create a text file containing all unique words havong a count of at least 2 """


""" Function to sort the vocabulary containing multiple instances of the same word """
def sortVocabulary():
    vocabulary = open('C:/Users/hp/Desktop/NLP/vocabulary.txt', 'r')
    sortedVocabulary = open('C:/Users/hp/Desktop/NLP/sortedVocabulary.txt', 'w')
    for line in sorted(vocabulary):
        sortedVocabulary.write(line)

""" Function to reduce the vocabulary to its final form"""        
def reduceVocabulary():
    vocabulary = open('C:/Users/hp/Desktop/NLP/sortedVocabulary.txt', 'r')
    reducedVocabulary = open('C:/Users/hp/Desktop/NLP/reducedVocabulary.txt', 'w')
    prevWord=""
    lastWrittenWord=""
    for word in vocabulary:
        if word==prevWord:
            if word==lastWrittenWord:
                continue
            else:
                reducedVocabulary.write(word)
                lastWrittenWord=word
        else:
            prevWord=word
               
""" Function to remove non-alphanumeric characters in a given word like apostrophe """
def removeNonAlpha(word):
    newWord=""
    for letter in word:
        if letter.isalpha():
            newWord+=letter
        else:
            continue
    return newWord

""" Function to create the initial multi-instance version of the vocabulary """
def createVocabulary():
    reviews = open('C:/Users/hp/Desktop/NLP/reviewsEdited.txt', 'r')
    vocabulary = open('C:/Users/hp/Desktop/NLP/vocabulary.txt', 'w')

    for line in reviews:
        for word in line.split():
            editedWord=removeNonAlpha(word)
            if len(editedWord)>0:
                vocabulary.write(editedWord+"\n")


createVocabulary()
sortVocabulary()
reduceVocabulary()