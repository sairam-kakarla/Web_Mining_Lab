import sys
import math
def readDocFromTxt(filename:str)->list:
    """Given the filename, return the documents stored in the file.
    Parses the document and splits them based on delimiter(\s)
    Limited to consider each line as an individual document."""
    docList=[]
    try:
        with open(filename,"r") as fileObj:
            docList=fileObj.readlines()
            fileObj.close()
    except IOError as e:
        print("ERROR:"+e.strerror)
        print("Program Terminated")
        sys.exit()
    for i in range(len(docList)):
        docList[i]=docList[i].replace(",","").replace(".","").replace("\n","").lower()
    return docList


def getNormDocVectorRep(datasetM:list,content_wordsM:list)->list:
    vector_rep=[]
    for i in datasetM:
        doc_vector=[0]*len(content_wordsM)
        for j in range(len(content_wordsM)):
            if content_wordsM[j] in i:
                doc_vector[j]+=1
        norm=math.sqrt(sum([i*i for i in doc_vector]))
        if norm!=0:
            for i in range(len(doc_vector)):
                doc_vector[i]=round(doc_vector[i]/norm,4)
        vector_rep.append(doc_vector)
    return vector_rep

if __name__=="__main__":
    dataset_filename="datasetM.txt"
    content_words_filename="content_wordsM.txt"
    datasetM=readDocFromTxt(dataset_filename)
    content_wordsM=readDocFromTxt(content_words_filename)
    doc_vector_rep=getNormDocVectorRep(datasetM,content_wordsM)
    print(doc_vector_rep)