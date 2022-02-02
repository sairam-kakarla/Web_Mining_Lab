"""
Page Clustering Algorithm
Author:[Lakshmi Sairam Kakarla]
Description:[Implementation of the K-Means Clustering]
"""
import sys

import numpy
import tabulate
import numpy as np

def eucliedianDistance(vector_a, vector_b):
    """Given two vectors represented using list, returns the eucliedian Distance between the
    vectors"""
    return np.round(np.sqrt(np.sum((vector_a-vector_b)**2,axis=1)),4)

def KMeans(docs_vector,k_no,num_iter):
    row=docs_vector.shape[0]
    column=docs_vector.shape[1]
    if(row<k_no):
        print("The number of clusters are less than the number of documents")
        sys.exit(1)
    # Select randomly k documents as centroids of k clusters.
    centroid=np.array([docs_vector[np.random.randint(0,row)] for i in range(k_no) ])
    classfication=dict()
    for i in range(num_iter):
        temp_clusters={k:[] for k in range(len(centroid))}
        temp_centroid=[]
        for j in range(row):
            node_distances=eucliedianDistance(centroid,docs_vector[j])
            temp_clusters[np.argmin(node_distances)].append(j)
            classfication[j]=np.argmin(node_distances)
        for k in range(len(centroid)):
            if len(temp_clusters[k])>1:
                temp_centroid.append(np.round(np.sum(docs_vector[temp_clusters[k]],axis=0)/len(temp_clusters[k]),4).tolist())
            elif len(temp_clusters[k])==1:
                temp_centroid.append(docs_vector[temp_clusters[k][0]].tolist())
        centroid=np.asarray(temp_centroid,float)
    print(tabulate.tabulate([[str(i+1),centroid[i].tolist()] for i in range(len(centroid))],headers=["Cluster","Centroid"],tablefmt="fancy_grid"))
    print(tabulate.tabulate([["DOC-"+str(i+1),str(classfication[i]+1)] for i in classfication.keys()],headers=["DOC","Cluster"],tablefmt="fancy_grid"))



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

def getDocVectorRep(datasetM:list,content_wordsM:list)->numpy.matrix:
    vector_rep=[]
    for i in datasetM:
        doc_vector=[0]*len(content_wordsM)
        for j in range(len(content_wordsM)):
            if content_wordsM[j] in i:
                doc_vector[j]+=i.count(content_wordsM[j])
        vector_rep.append(doc_vector)
    return np.array(vector_rep)

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
                distanceMatrix[i][j]=np.round(np.sqrt(np.sum((doc_vector_rep[i]-doc_vector_rep[j])**2)),4)
    print("Inital Distance Matrix")
    print(tabulate.tabulate([["DOC-"+str(k+1),*i] for k,i in enumerate(distanceMatrix)],headers=[" ",*["DOC-"+str(i+1) for i in range(len(datasetM))]],tablefmt="fancy_grid"))
    print("NUMBER OF CLUSTER 5")
    KMeans(doc_vector_rep, 7, 25)

