""" Program to find word counts of the positive and negative classes and to find vocabulary size """

positiveTotalbigramCount=0
negativeTotalbigramCount=0
    
         
""" Function to sort the words in both classes """
def sortBigrams():
    posbiReviews = open('C:\Users\hp\Desktop\NLP/Final Code/posbireviews.txt', 'r')
    negbiReviews = open('C:\Users\hp\Desktop\NLP/Final Code/negbireviews.txt', 'r')
    sortedPosbiReviews = open('C:\Users\hp\Desktop\NLP\sortedPosbiReviews.txt', 'w')
    sortedNegbiReviews = open('C:\Users\hp\Desktop\NLP\sortedNegbiReviews.txt', 'w')
    for line in sorted(posbiReviews):
        sortedPosbiReviews.write(line)
    for line in sorted(negbiReviews):
        sortedNegbiReviews.write(line)
        
""" Function to find the count of each bigram in both classes """
def bigramCount():
    sortedPosbiReviews = open('C:\Users\hp\Desktop\NLP\sortedPosbiReviews.txt', 'r')
    sortedNegbiReviews = open('C:\Users\hp\Desktop\NLP\sortedNegbiReviews.txt', 'r')
    positivebigramCount = open('C:\Users\hp\Desktop\NLP\positivebigramCount.txt', 'w')
    negativebigramCount = open('C:\Users\hp\Desktop\NLP\\negativebigramCount.txt', 'w')
    prevBigram=""
    count=0
    global positiveTotalbigramCount
    global negativeTotalbigramCount
    for line in sortedPosbiReviews:
        positiveTotalbigramCount+=1
        if prevBigram=="":
            prevBigram=line
            count=1
        elif line.lower()==prevBigram.lower():
            count+=1
        else:
            positivebigramCount.write(prevBigram.rstrip()+" "+str(count)+"\n")
            prevBigram=line
            count=1

    for line in sortedNegbiReviews:
        negativeTotalbigramCount+=1
        if prevBigram=="":
            prevBigram=line
            count=1
        elif line.lower()==prevBigram.lower():
            count+=1
        else:
            negativebigramCount.write(prevBigram.rstrip()+" "+str(count)+"\n")
            prevBigram=line
            count=1



""" Function to create two text files with bigrams associated to the two classes """
def splitClassesBi(file_name):
    bigrams = open('C:\Users\hp\Desktop\NLP\\bigramVocab.txt', 'r')
    reviews = open(file_name, 'r')
    posbireviews = open('C:\Users\hp\Desktop\NLP/Final Code/posbireviews.txt', 'w')
    negbireviews = open('C:\Users\hp\Desktop\NLP/Final Code/negbireviews.txt', 'w')
    flag = ''
    for line in bigrams:
        if len(line.split()) == 2:
            reviews = open('C:\Users\hp\Desktop\NLP\\reviewsEdited.txt', 'r')
            for line2 in reviews:
                blocks = line2.split()
                if blocks[0] == '+':
                    flag = '+'
                elif blocks[0] == '-':
                    flag = '-'
                for i in range(1,len(blocks)-1) :
                    possible_bigram = blocks[i] + " " + blocks[i+1]
                    var1 = line.lower()
                    var2 = possible_bigram.lower()
                    var2 = var2.replace(',','')
                    var2 = var2.replace('.','')
                    var2 = var2.replace('!','')
                    var3 = var1[:-1]
                    if var2 == var3 and flag == '+':
                        posbireviews.write(line)
                    elif var2 == var3 and flag == '-':
                        negbireviews.write(line)
                flag = ''
                    

sortBigrams()


