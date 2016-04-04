""" Program to train the Naive Bayes Model """

from preNaiveBayes1 import *
import math
import pickle


def naiveBayes():
    positiveWordCount = open('C:/Users/hp/Desktop/NLP/positiveWordCount.txt', 'r')
    negativeWordCount = open('C:/Users/hp/Desktop/NLP/negativeWordCount.txt', 'r')
    vocabulary = open('C:/Users/hp/Desktop/NLP/reducedVocabulary.txt', 'r')
    pickleFilePositive = open('C:/Users/hp/Desktop/NLP/pickleFilePositive.pkl', 'wb')
    pickleFileNegative = open('C:/Users/hp/Desktop/NLP/pickleFileNegative.pkl', 'wb')
    wordPositiveProbabilities = {}
    tempList=[]

    for line in positiveWordCount:
        tempList=line.split()
        tempVar=(float(tempList[1])+1)/(positiveTotalWordCount + vocabularyWordCount)
        wordPositiveProbabilities[tempList[0]]=math.log(tempVar, 2)

    wordPositiveProbabilities["+"] = 1 
    wordPositiveProbabilities["-"] = 1
        
    pickle.dump(wordPositiveProbabilities, pickleFilePositive)
    pickleFilePositive.close()
    
    wordNegativeProbabilities = {}
    tempList=[]
    for line in negativeWordCount:
        tempList=line.split()
        tempVar=(float(tempList[1])+1)/(negativeTotalWordCount + vocabularyWordCount)
        wordNegativeProbabilities[tempList[0]]=math.log(tempVar, 2)
        
    for word in vocabulary:
        if word not in wordPositiveProbabilities.keys():
            tempVar=float(1.0/(positiveTotalWordCount + vocabularyWordCount))
            var=math.log(tempVar, 2)
            wordPositiveProbabilities[word] = var
        if word not in wordNegativeProbabilities.keys():
            tempVar=float(1.0/(negativeTotalWordCount + vocabularyWordCount))
            wordNegativeProbabilities[word] = math.log(tempVar, 2)
    print wordNegativeProbabilities["fantastic"]

    wordNegativeProbabilities["+"] = 1
    wordNegativeProbabilities["-"] = 1
    pickle.dump(wordNegativeProbabilities, pickleFileNegative)
    pickleFileNegative.close()    
    
    pickle_read = open('C:/Users/hp/Desktop/NLP/pickleFilePositive.pkl', 'r')
    d=pickle.load(pickle_read)

naiveBayes()