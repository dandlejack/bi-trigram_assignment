fileName = "format.txt";
lines = [line.rstrip('\n') for line in open(fileName)];
dicUnigram = {};
dicBigram = {};
dicTrigram = {};
unigram = [];
bigram = [];
bigramCalProb =[];
trigram=[];
wr = open("Bigram.txt","w");
wr.write("-------------Bigram-----------------\n");
wr.write("  N  | N-1  |  Probability \n");
wr.write("------------------------------------\n");
wrTri = open("Trigram.txt","w");
wrTri.write("-------------Trigram-----------------\n");
wrTri.write("  N  | N-2,N-1  |  Probability \n");
wrTri.write("------------------------------------\n");
for row in lines:
    i=0;j=0;k=0
    keep_word = row.split(" ");
    keepword_lenght = len(keep_word);
#Unigram
    while k<keepword_lenght:
        arr=[]
        arr.append(keep_word[k])
        unigram.append(keep_word[k]);
        dicUnigram[arr[0]] = unigram.count(arr[0])
        k+=1
#BiGram
    while(i<keepword_lenght-1):
        arr=[];
        arr.append((keep_word[i],keep_word[i+1]))
        bigram.append((keep_word[i],keep_word[i+1]))
        dicBigram[arr[0]] = bigram.count(arr[0])
        i += 1;
#TriGram
    while(j<keepword_lenght-2):
        arr = [];
        arr.append((keep_word[j],keep_word[j+1],keep_word[j+2]))
        trigram.append((keep_word[j],keep_word[j+1],keep_word[j+2]))
        dicTrigram[arr[0]] = trigram.count(arr[0])
        j+=1
#BiGram Prob
l=0;bigramLen = len(bigram);
while l<bigramLen:
    biwithword = bigram[l],bigram[l][0]
    ProbOfBi = dicBigram[bigram[l]]/dicUnigram[bigram[l][0]];
    roundProbBi = "%.4f "% ProbOfBi
    stringBi = "%s | %s | " % biwithword
    stringBi += "".join(roundProbBi);
    stringBi += "\n"
    wr.write(stringBi);
    l+=1;
#TriGram Prob
m=0;s=0;trigramLen = len(trigram);
while m<trigramLen:
    if trigram[m][0] == '<s>' and bigram[s][1] == '</s>':
        s+=1;
        ProbOfTri = dicTrigram[trigram[m]]/dicBigram[bigram[s]];
    else :
        ProbOfTri = dicTrigram[trigram[m]]/dicBigram[bigram[s]];
    Triwithword = trigram[m],bigram[s];
    StrTri = "%s | %s | " % Triwithword;
    StrTri += "".join(str(ProbOfTri));
    StrTri += "\n";
    wrTri.write(StrTri);
    s+=1;
    m+=1;
wr.closed;
wrTri.closed;
