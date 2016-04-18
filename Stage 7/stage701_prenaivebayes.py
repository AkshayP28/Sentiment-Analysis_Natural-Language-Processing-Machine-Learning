dictionaryBi = {}
dictionaryUni = {}
def convertToDictionaryBi():
    text_file = open('C:\Users\hp\Desktop\NLP\positivebigramCount.txt', 'r')
    for line in text_file:
        tempVar=line.split()
        dictionaryBi[tempVar[0]+" "+tempVar[1]]=tempVar[2]

    
def convertToDictionaryUni():
    text_file = open('C:\Users\hp\Desktop\NLP\positiveWordCount.txt', 'r')
    for line in text_file:
        tempVar=line.split()
        dictionaryUni[tempVar[0]]=tempVar[1]

    
def updateUnigramCount():
    for word in dictionaryBi.keys():
        tempVar=word.split()
        value=int(dictionaryUni[tempVar[0]])
        value-=int(dictionaryBi[word])
        dictionaryUni[tempVar[0]]=str(value)
        value=int(dictionaryUni[tempVar[1]])
        value-=int(dictionaryBi[word])
        dictionaryUni[tempVar[1]]=str(value)

        
    
def convertToTextFileUni():
    text_file = open('C:\Users\hp\Desktop\NLP\Final Code\Stage 7\unigramWordCount.txt', 'w')
    for word in dictionaryUni.keys():
        text_file.write(word+" "+dictionaryUni[word])
        


convertToDictionaryBi()
convertToDictionaryUni()
updateUnigramCount()
convertToTextFileUni()
