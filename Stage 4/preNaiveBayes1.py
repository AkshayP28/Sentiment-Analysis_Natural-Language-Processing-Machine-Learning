""" Program to find word counts of the positive and negative classes and to find vocabulary size """

positiveTotalWordCount=0
negativeTotalWordCount=0
vocabularyWordCount=0

""" Function to sort the words in both classes """
def sortWords():
    positiveReviews = open('C:/Users/hp/Desktop/NLP/positiveReviews.txt', 'r')
    negativeReviews = open('C:/Users/hp/Desktop/NLP/negativeReviews.txt', 'r')
    sortedPositiveReviews = open('C:/Users/hp/Desktop/NLP/sortedPositiveReviews.txt', 'w')
    sortedNegativeReviews = open('C:/Users/hp/Desktop/NLP/sortedNegativeReviews.txt', 'w')
    for line in sorted(positiveReviews):
        sortedPositiveReviews.write(line)
    for line in sorted(negativeReviews):
        sortedNegativeReviews.write(line)
        
""" Function to find the count of each word in both classes """
def wordCount():
    sortedPositiveReviews = open('C:/Users/hp/Desktop/NLP/sortedPositiveReviews.txt', 'r')
    sortedNegativeReviews = open('C:/Users/hp/Desktop/NLP/sortedNegativeReviews.txt', 'r')
    positiveWordCount = open('C:/Users/hp/Desktop/NLP/positiveWordCount.txt', 'w')
    negativeWordCount = open('C:/Users/hp/Desktop/NLP/negativeWordCount.txt', 'w')
    prevWord=""
    count=0
    global positiveTotalWordCount
    global negativeTotalWordCount
    for word in sortedPositiveReviews:
        positiveTotalWordCount+=1
        if prevWord=="":
            prevWord=word
            count=1
        elif word==prevWord:
            count+=1
        else:
            positiveWordCount.write(prevWord.rstrip()+" "+str(count)+"\n")
            prevWord=word
            count=1

    for word in sortedNegativeReviews:
        negativeTotalWordCount+=1
        if prevWord=="":
            prevWord=word
            count=1
        elif word==prevWord:
            count+=1
        else:
            negativeWordCount.write(prevWord.rstrip()+" "+str(count)+"\n")
            prevWord=word
            count=1

""" Function to find total number of features in the vocabulary """        
def vocabularyCount():
    vocabulary = open('C:/Users/hp/Desktop/NLP/reducedVocabulary.txt', 'r')
    global vocabularyWordCount
    for word in vocabulary:
         vocabularyWordCount+=1   

""" Function to create two text files with words associated to the two classes """
def splitClasses(file_name):
    reviews = open(file_name, 'r')
    positiveReviews = open('C:/Users/hp/Desktop/NLP/positiveReviews.txt', 'w')
    negativeReviews = open('C:/Users/hp/Desktop/NLP/negativeReviews.txt', 'w')
    flag='start'
    for line in reviews:
        for word in line.split():
            if flag=='start':
                if word=='+':
                    flag='positive'
                    continue
                elif word=='-':
                    flag='negative'
                    continue
            elif flag=='positive':
                positiveReviews.write(word+'\n')
            elif flag=='negative':
                negativeReviews.write(word+'\n')
        flag='start'


#splitClasses()
sortWords()
wordCount()
vocabularyCount()
print positiveTotalWordCount,"\n"
print negativeTotalWordCount,"\n"
print vocabularyWordCount,"\n"