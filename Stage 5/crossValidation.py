""" Program to perform Cross Vaildation """
from itertools import izip
from removeStopWords import *
from preNaiveBayes1 import *
from createVocabulary import *
from naiveBayes import *

accuracy = open("C:/Users/hp/Desktop/NLP/crossValidation/accuracy.txt", "w")


def splitReviews():
    reviews = open('C:/Users/hp/Desktop/NLP/reviewsEdited.txt', 'r')
    positiveSentences = open('C:/Users/hp/Desktop/NLP/positiveSentences.txt', 'w')   
    negativeSentences = open('C:/Users/hp/Desktop/NLP/negativeSentences.txt', 'w')         
    for line in reviews:
        for word in line.split():
            if word=="+":
                positiveSentences.write(line)
            elif word=="-":
                negativeSentences.write(line)
            else:
                break
                
#def createMixed():
#    positiveSentences = open('C:/Users/hp/Desktop/NLP/positiveSentences.txt', 'r')   
#    negativeSentences = open('C:/Users/hp/Desktop/NLP/negativeSentences.txt', 'r') 
#    mixedReviews = open('C:/Users/hp/Desktop/NLP/mixedReviews.txt', 'w')
#    for line1, line2 in zip(positiveSentences, negativeSentences):
#        mixedReviews.write("{0}\n{1}".format(line1.strip(),line2.strip()))
        
 
def sent():
     op = open("C:/Users/hp/Desktop/NLP/mixedReviews.txt", "w")
     with open("C:/Users/hp/Desktop/NLP/positiveSentences.txt", "r") as textfile1, open("C:/Users/hp/Desktop/NLP/negativeSentences.txt", "r") as textfile2: 
         for x, y in izip(textfile1, textfile2):
             x = x.strip()
             y = y.strip()
             op.write("{0}\n{1}".format(x, y))
             op.write("\n")
         for x in textfile2:
             op.write(x)
         for x in textfile1:
             op.write(x)
             
def createFolds():
    op = open("C:/Users/hp/Desktop/NLP/mixedReviews.txt", "r")
    fold1 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold1.txt", "w")
    fold2 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold2.txt", "w")
    fold3= open("C:/Users/hp/Desktop/NLP/crossValidation/fold3.txt", "w")
    fold4 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold4.txt", "w")
    fold5 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold5.txt", "w")
    fold6 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold6.txt", "w")
    fold7 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold7.txt", "w")
    fold8 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold8.txt", "w")
    fold9 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold9.txt", "w")
    fold10 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold10.txt", "w")
    lineNumber=1
    for line in op:
        if lineNumber<=51:
            fold1.write(line)
            lineNumber+=1
        elif lineNumber<=102:
            fold2.write(line)
            lineNumber+=1
        elif lineNumber<=153:
            fold3.write(line)
            lineNumber+=1
        elif lineNumber<=204:
            fold4.write(line)
            lineNumber+=1
        elif lineNumber<=255:
            fold5.write(line)
            lineNumber+=1
        elif lineNumber<=306:
            fold6.write(line)
            lineNumber+=1
        elif lineNumber<=357:
            fold7.write(line)              
            lineNumber+=1
        elif lineNumber<=409:
            fold8.write(line)
            lineNumber+=1
        elif lineNumber<=460:
            fold9.write(line)
            lineNumber+=1
        else:
            fold10.write(line)
            lineNumber+=1
            
            
def nFoldValidation(testNumber):
    fold1 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold1.txt", "r")
    fold2 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold2.txt", "r")
    fold3= open("C:/Users/hp/Desktop/NLP/crossValidation/fold3.txt", "r")
    fold4 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold4.txt", "r")
    fold5 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold5.txt", "r")
    fold6 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold6.txt", "r")
    fold7 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold7.txt", "r")
    fold8 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold8.txt", "r")
    fold9 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold9.txt", "r")
    fold10 = open("C:/Users/hp/Desktop/NLP/crossValidation/fold10.txt", "r")
    training = open("C:/Users/hp/Desktop/NLP/crossValidation/training.txt", "w")
    test = open("C:/Users/hp/Desktop/NLP/crossValidation/test.txt", "w")

    fold1_contents=fold1.read()    
    fold2_contents=fold2.read()
    fold3_contents=fold3.read()
    fold4_contents=fold4.read()
    fold5_contents=fold5.read()
    fold6_contents=fold6.read()
    fold7_contents=fold7.read()
    fold8_contents=fold8.read()
    fold9_contents=fold9.read()
    fold10_contents=fold10.read()
    if testNumber==10:
        training.write(fold1_contents+fold2_contents+fold3_contents+fold4_contents+fold5_contents+fold6_contents+fold7_contents+fold8_contents+fold9_contents)
        test.write(fold10_contents)
    elif testNumber==9:
        training.write(fold1_contents+fold2_contents+fold3_contents+fold4_contents+fold5_contents+fold6_contents+fold7_contents+fold8_contents+fold10_contents)
        test.write(fold9_contents)
    elif testNumber==8:
        training.write(fold1_contents+fold2_contents+fold3_contents+fold4_contents+fold5_contents+fold6_contents+fold7_contents+fold9_contents+fold10_contents)
        test.write(fold8_contents)
    elif testNumber==7:
        training.write(fold1_contents+fold2_contents+fold3_contents+fold4_contents+fold5_contents+fold6_contents+fold9_contents+fold8_contents+fold10_contents)
        test.write(fold7_contents)
    elif testNumber==6:
        training.write(fold1_contents+fold2_contents+fold3_contents+fold4_contents+fold5_contents+fold9_contents+fold7_contents+fold8_contents+fold10_contents)
        test.write(fold6_contents)
    elif testNumber==5:
        training.write(fold1_contents+fold2_contents+fold3_contents+fold4_contents+fold9_contents+fold6_contents+fold7_contents+fold8_contents+fold10_contents)
        test.write(fold5_contents)
    elif testNumber==4:
        training.write(fold1_contents+fold2_contents+fold3_contents+fold9_contents+fold5_contents+fold6_contents+fold7_contents+fold8_contents+fold10_contents)
        test.write(fold4_contents)
    elif testNumber==3:
        training.write(fold1_contents+fold2_contents+fold9_contents+fold4_contents+fold5_contents+fold6_contents+fold7_contents+fold8_contents+fold10_contents)
        test.write(fold3_contents)
    elif testNumber==2:
        training.write(fold1_contents+fold9_contents+fold3_contents+fold4_contents+fold5_contents+fold6_contents+fold7_contents+fold8_contents+fold10_contents)
        test.write(fold2_contents)
    elif testNumber==1:
        training.write(fold9_contents+fold2_contents+fold3_contents+fold4_contents+fold5_contents+fold6_contents+fold7_contents+fold8_contents+fold10_contents)
        test.write(fold1_contents)

def performValidation(file_name):
    pickleFilePositive = open('C:/Users/hp/Desktop/NLP/pickleFilePositive.pkl', 'r')
    pickleFileNegative = open('C:/Users/hp/Desktop/NLP/pickleFileNegative.pkl', 'r')
    positiveDictionary=pickle.load(pickleFilePositive)
    negativeDictionary=pickle.load(pickleFileNegative)    
    test = open("C:/Users/hp/Desktop/NLP/crossValidation/test.txt", "r")
    probabiltyPositiveProduct=0
    probabiltyNegativeProduct=0
    actualClass=""
    predictedClass=""
    correctPredictions=0
    incorrectPredictions=0
    #print negativeDictionary["very"]
    for line in test:
        if line[0]=="+":
            actualClass="+"
            for word in line.split():
                    if word not in positiveDictionary.keys():
                        tempVar=float(1.0/(positiveTotalWordCount + vocabularyWordCount))
                        var=math.log(tempVar, 2)
                        probabiltyPositiveProduct+=var
                    elif word not in negativeDictionary.keys():  
                        tempVar=float(1.0/(negativeTotalWordCount + vocabularyWordCount))
                        var=math.log(tempVar, 2)
                        probabiltyNegativeProduct+=var
                    else:
                        probabiltyPositiveProduct+=positiveDictionary[word]
                        probabiltyNegativeProduct+=negativeDictionary[word]
            
            if probabiltyPositiveProduct<probabiltyNegativeProduct:
                predictedClass="+"
            else:
                predictedClass="-"
            if predictedClass==actualClass:
                correctPredictions+=1
            else:
                incorrectPredictions+=1
            probabiltyPositiveProduct=1
            probabiltyNegativeProduct=1

        elif line[0]=="-":
            actualClass="-"
            for word in line.split():
                    if word not in positiveDictionary.keys():
                        tempVar=float(1.0/(positiveTotalWordCount + vocabularyWordCount))
                        var=math.log(tempVar, 2)
                        probabiltyPositiveProduct+=var
                    elif word not in negativeDictionary.keys():  
                        tempVar=float(1.0/(negativeTotalWordCount + vocabularyWordCount))
                        var=math.log(tempVar, 2)
                        probabiltyNegativeProduct+=var
                    else:
                        probabiltyPositiveProduct+=positiveDictionary[word]
                        probabiltyNegativeProduct+=negativeDictionary[word]
            
            if probabiltyPositiveProduct<probabiltyNegativeProduct:
                predictedClass="+"
            else:
                predictedClass="-"
            if predictedClass==actualClass:
                correctPredictions+=1
            else:
                incorrectPredictions+=1
                
            probabiltyPositiveProduct=1
            probabiltyNegativeProduct=1
    
    testedAccuracy=(correctPredictions/float(correctPredictions+incorrectPredictions)*100)
    accuracy.write(str(testedAccuracy)+"\n")               
                

def averageAccuracy():
    sumOfAccuracies=0.0
    
    for line in accuracy:
           sumOfAccuracies+=float(line)
           
    print sumOfAccuracies/10
    
removeStopWords()
""""""
createVocabulary()
sortVocabulary()
reduceVocabulary()
""""""
splitClasses('C:/Users/hp/Desktop/NLP/reviewsEdited.txt')
sortWords()
wordCount()
vocabularyCount()
""""""
naiveBayes()
""""""
splitReviews()
#createMixed()
sent()
createFolds()


#   test 1
nFoldValidation(1)

splitClasses('C:/Users/hp/Desktop/NLP/crossValidation/training.txt')
sortWords()
wordCount()
naiveBayes()
performValidation('C:/Users/hp/Desktop/NLP/crossValidation/test.txt')

#   test 2
nFoldValidation(2)

splitClasses('C:/Users/hp/Desktop/NLP/crossValidation/training.txt')
sortWords()
wordCount()
naiveBayes()
performValidation('C:/Users/hp/Desktop/NLP/crossValidation/test.txt')

#   test 3
nFoldValidation(3)

splitClasses('C:/Users/hp/Desktop/NLP/crossValidation/training.txt')
sortWords()
wordCount()
naiveBayes()
performValidation('C:/Users/hp/Desktop/NLP/crossValidation/test.txt')

#   test 4
nFoldValidation(4)

splitClasses('C:/Users/hp/Desktop/NLP/crossValidation/training.txt')
sortWords()
wordCount()
naiveBayes()
performValidation('C:/Users/hp/Desktop/NLP/crossValidation/test.txt')

#   test 5
nFoldValidation(5)

splitClasses('C:/Users/hp/Desktop/NLP/crossValidation/training.txt')
sortWords()
wordCount()
naiveBayes()
performValidation('C:/Users/hp/Desktop/NLP/crossValidation/test.txt')

#   test 6
nFoldValidation(6)

splitClasses('C:/Users/hp/Desktop/NLP/crossValidation/training.txt')
sortWords()
wordCount()
naiveBayes()
performValidation('C:/Users/hp/Desktop/NLP/crossValidation/test.txt')

#   test 7
nFoldValidation(7)

splitClasses('C:/Users/hp/Desktop/NLP/crossValidation/training.txt')
sortWords()
wordCount()
naiveBayes()
performValidation('C:/Users/hp/Desktop/NLP/crossValidation/test.txt')

#   test 8
nFoldValidation(8)

splitClasses('C:/Users/hp/Desktop/NLP/crossValidation/training.txt')
sortWords()
wordCount()
naiveBayes()
performValidation('C:/Users/hp/Desktop/NLP/crossValidation/test.txt')

#   test 9
nFoldValidation(9)

splitClasses('C:/Users/hp/Desktop/NLP/crossValidation/training.txt')
sortWords()
wordCount()
naiveBayes()
performValidation('C:/Users/hp/Desktop/NLP/crossValidation/test.txt')

#   test 10
nFoldValidation(10)

splitClasses('C:/Users/hp/Desktop/NLP/crossValidation/training.txt')
sortWords()
wordCount()
naiveBayes()
performValidation('C:/Users/hp/Desktop/NLP/crossValidation/test.txt')

#   average accuracy
accuracy.close()
accuracy = open("C:/Users/hp/Desktop/NLP/crossValidation/accuracy.txt", "r")
averageAccuracy()