""" Program to train the Naive Bayes Model """

from stage70_prenaivebayes import *
import math
import pickle

vocabularyWordCount = 0

def poswordCount(biword):
    sortedPositiveReviews = open('C:\Users\hp\Desktop\NLP\sortedPositiveReviews.txt', 'r')
    count=0
    for word in sortedPositiveReviews:
        var = word
        var1 = var[:-1]
        if var1 == biword:
            count += 1
    return count

def negwordCount(biword):
    sortedNegativeReviews = open('C:\Users\hp\Desktop\NLP\sortedNegativeReviews.txt', 'r')
    count=0
    for word in sortedNegativeReviews:
        var = word
        var1 = var[:-1]
        if var1 == biword:
            count += 1
    return count


def vocabularyCount():
    global vocabularyWordCount
    vocabulary = open('C:\Users\hp\Desktop\NLP\\reducedVocabulary.txt', 'r')
    for word in vocabulary:
        vocabularyWordCount +=1
        

def naiveBayes():
    positivebigramCount = open('C:\Users\hp\Desktop\NLP\positivebigramCount.txt', 'r')
    negativebigramCount = open('C:\Users\hp\Desktop\NLP\\negativebigramCount.txt', 'r')
    pickleFilePositivebi = open('C:\Users\hp\Desktop\NLP\pickleFilePositiveBigram.pkl', 'wb')
    pickleFileNegativebi = open('C:\Users\hp\Desktop\NLP\pickleFileNegativeBigram.pkl', 'wb')
    bigramPositiveProbabilities = {}
    tempList=[]

    for line in positivebigramCount:
        tempList=line.split()
        tempVar=(float(tempList[2])+1)/(poswordCount(tempList[0]) + vocabularyWordCount)
        bigramPositiveProbabilities[tempList[0]+ " " +tempList[1]]=math.log(tempVar, 2)

        
    pickle.dump(bigramPositiveProbabilities, pickleFilePositivebi)
    pickleFilePositivebi.close()
    
    bigramNegativeProbabilities = {}
    tempList=[]
    for line in negativebigramCount:
        tempList=line.split()
        tempVar=(float(tempList[2])+1)/(negwordCount(tempList[0]) + vocabularyWordCount)
        bigramNegativeProbabilities[tempList[0]+ " " + tempList[1]]=math.log(tempVar, 2)
    
    bigramvocab = open('C:\Users\hp\Desktop\NLP\\bigramVocab.txt', 'r')
    for line in bigramvocab:
        if len(line.split()) == 2:
            if line not in bigramPositiveProbabilities.keys():
                tempList=line.split()
                tempVar=float(1.0/(poswordCount(tempList[0]) + vocabularyWordCount))
                var=math.log(tempVar, 2)
                bigramPositiveProbabilities[tempList[0]+ " " + tempList[1]] = var
            if line not in bigramNegativeProbabilities.keys():
                tempList=line.split()
                tempVar=float(1.0/(negwordCount(tempList[0]) + vocabularyWordCount))
                var = math.log(tempVar, 2)
                bigramNegativeProbabilities[tempList[0]+ " " + tempList[1]] = var

    
    pickle.dump(bigramNegativeProbabilities, pickleFileNegativebi)
    pickleFileNegativebi.close()    

vocabularyCount()
naiveBayes()
