datafile = open('C:/Users/Akshay-PC/Desktop/NLP/reviewsEdited.txt', 'r')
vocabBigram = open('C:/Users/Akshay-PC/Desktop/NLP/bigramVocab.txt', 'w')

dictv = dict()

for line in datafile:
    words = line.split()
    for i in range(1,len(words)-1):
        #if words[i] in dictv:
         #   dictv[words[i]] += 1
        #else:
         #   dictv[words[i]] = 1
        if (words[i] + " " + words[i+1]) in dictv:
            dictv[words[i] + " " + words[i+1]] += 1
        else:
            dictv[words[i] + " " + words[i+1]] = 1
            
            
count3vocab = [review for review in dictv if dictv[review] >= 2]

for review in count3vocab:
    vocabBigram.write(review + '\n') 
    for word in review.split():
        vocabBigram.write(word + '\n') 