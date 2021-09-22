# DICT Structure
# key(word):{frequency,Rpostinglist}
# RpostingList Structure
# [[docid1,index1,index2,...],[docid2,index1,index2,...],...]

# Removes the punctuation in the document
# and returns list of space seperated tokens
def parseAndRemovePunctuation(doc):
    parsed_doc = doc.split()
    i = 0
    while i < len(parsed_doc):
        if parsed_doc[i][len(parsed_doc[i]) - 1] == ".":
            parsed_doc[i] = parsed_doc[i][:len(parsed_doc[i]) - 1]
        elif parsed_doc[i][len(parsed_doc[i]) - 1] == ";":
            parsed_doc[i] = parsed_doc[i][:len(parsed_doc[i]) - 1]
        i += 1
    for i in range(len(parsed_doc)):
        parsed_doc[i] = parsed_doc[i].lower()
    return parsed_doc

def generateDict(doc1, doc2):
    inverseDocumentHash = dict()
    merge = doc1 + doc2
    for i in merge:
        inverseDocumentHash[i] = merge.count(i)
    return {k: [inverseDocumentHash[k]] for k in sorted(inverseDocumentHash)}


def generatePostingList(doc,word):
    plist=[]
    for i in range(len(doc)):
        if doc[i]==word:
            plist.append(i)
    return plist

def bindPosting(tfdict, doc1, doc2):
    for i in tfdict.keys():
        postinglistDoc1=generatePostingList(doc1,i)
        postinglistDoc2 = generatePostingList(doc2, i)
        if postinglistDoc1:
            tfdict[i].append([1,postinglistDoc1])
        if postinglistDoc2 :
            tfdict[i].append([2,postinglistDoc2])
    return tfdict

def displayIndexer(indexer):
    for i in indexer.keys():
        print("[%s %d] -> ["%(i,indexer[i][0]),end="")
        for j in indexer[i][1:]:
            print("DOCID[%d]"%(j[0]),end="->[")
            for k in j[1]:
                print("%d"%(k),end="->")
            print("-1]",end=",")
        print("]")

doc1 = "I did enact Julius Caesar I was killed i' the Capitol; Brutus killed me."
doc2 = "So let it be with Caesar. The noble Brutus hath told you Caesar was ambitious"
parsedDoc1 = parseAndRemovePunctuation(doc1)
parsedDoc2 = parseAndRemovePunctuation(doc2)
tfdict=generateDict(parsedDoc1, parsedDoc2)
indexer=bindPosting(tfdict,parsedDoc1,parsedDoc2)
displayIndexer(indexer)