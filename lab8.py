"""
Page Clustering Algorithm
Author:[Lakshmi Sairam Kakarla]
Description:[Implementation of the K-Means Clustering]
"""
import sys
import tabulate

def eucliedianDistance(vector_a: list, vector_b: list) -> float:
    """Given two vectors represented using list, returns the eucliedian Distance between the
    vectors"""
    squaredSum = 0
    for i in range(len(vector_b)):
        squaredSum += (vector_a[i] - vector_b[i]) ** 2
    return round(squaredSum ** 0.5,4)

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

def getDocVectorRep(datasetM:list,content_wordsM:list)->list:
    vector_rep=[]
    for i in datasetM:
        doc_vector=[0]*len(content_wordsM)
        for j in range(len(content_wordsM)):
            if content_wordsM[j] in i:
                doc_vector[j]+=1
        vector_rep.append(doc_vector)
    return vector_rep

if __name__=="__main__":
    dataset_filename="datasetM.txt"
    content_words_filename="content_wordsM.txt"
    datasetM=readDocFromTxt(dataset_filename)
    content_wordsM=readDocFromTxt(content_words_filename)
    doc_vector_rep=getDocVectorRep(datasetM,content_wordsM)
    print(tabulate.tabulate([["DOC-"+str(k+1),*i] for k,i in enumerate(doc_vector_rep)],headers=["Doc ID",*content_wordsM],tablefmt="fancy_grid"))
    distanceMatrix=[]
    for i in range(len(datasetM)):
        distanceMatrix.append([0]*len(datasetM))
    for i in range(len(datasetM)):
        for j in range(len(datasetM)):
            if i==j:
                distanceMatrix[i][j]=0
            else:
                distanceMatrix[i][j]=eucliedianDistance(doc_vector_rep[i],doc_vector_rep[j])
    print("Inital Distance Matrix")
    print(tabulate.tabulate([["DOC-"+str(k+1),*i] for k,i in enumerate(distanceMatrix)],headers=[" ",*["DOC-"+str(i+1) for i in range(len(datasetM))]],tablefmt="fancy_grid"))


