# Algorithm to identify web hub.
# web search produces root set.
# all pages pointing to or being pointed from root set forms the larger base set
# IGNORE SELF LOOPS
# if A->B then there is recommendation for site B
# Hub: lot of outlinks
# Authorities will have mainly inlinks
#HITS algorithm developed by Kleinberg provided
# a  solution to find whether a website is hub or an authority or it is an intermediate
# HITS algorithm find score of a website as a hub and authority.
"""
Generate the Adjacency matrix from the network of pages.
1. init h(d)=a(d)=1 for all d webpages.
2. For all d: h(d)=Summation of a(y) where a(y) is the authority-score of the pages
   recommended by d.
3. For all d: a(d)=Summation of h(y) where h(y) is the hub-score of the pages
   recommending d.
"""

"""
Implemenation:
h=(h1,..hn) as a vector of hub,where hi is the hub-score of page di.
a=(a1,..an) as a vector of authority,where ai is the authority-score of page di.
h(d)=Summation a(y) for d->y can be written as:
     h=Aa.
a(d)=Summation h(y) for d<-y can be written as:
     a=ATh. AT=Transpose(A).
     
Algorithm:
   while convergence:
       h=Aa
       a=ATh
"""

"""
Since its recursive it may diverge,so Kleinberg suggested Normalization after every iteration.
 so 0<h(d),a(d)<=1
nom(score)=calc_score/sum_of_calc_score
"""
import tabulate
import time
def nomalize(score):
    total_sum=sum(score)
    for i in range(len(score)):
        score[i]/=total_sum
    return score

matrixNSL = [[0,0,1,0,0,0,0],
             [0,0,1,0,0,0,0],
             [1,0,0,1,0,0,0],
             [0,0,0,0,1,0,0],
             [0,0,0,0,0,0,1],
             [0,0,0,0,0,0,1],
             [0,0,0,1,1,0,0]]

matrixSL =  [[0,0,1,0,0,0,0],
             [0,1,1,0,0,0,0],
             [1,0,1,1,0,0,0],
             [0,0,0,1,1,0,0],
             [0,0,0,0,0,0,1],
             [0,0,0,0,0,1,1],
             [0,0,0,1,1,0,1]]

matrixQ3 =  [[0,0,1,0,0,0,0],
             [0,1,1,0,0,0,0],
             [1,0,1,2,0,0,0],
             [0,0,0,1,1,0,0],
             [0,0,0,0,0,0,1],
             [0,0,0,0,0,1,1],
             [0,0,0,2,1,0,1]]
matrix=matrixQ3
n = len(matrix)
iter = 25
print("%d iterations done in"%(iter),end=" ")
hubScore = [1]*n
authScore = [1]*n
hubScore=nomalize(hubScore)
authScore=nomalize(authScore)
startT=time.time_ns()
while iter-1>0:
    iter-=1
    for i in range(n):
        for j in range(n):
            if matrix[i][j]>=0:
                hubScore[i]+=matrix[i][j]*authScore[j]
    for i in range(n):
        for j in range(n):
            if matrix[i][j]>=0:
                authScore[j]+=matrix[i][j]*hubScore[i]
    authScore = nomalize(authScore)
    hubScore=nomalize(hubScore)

endT=time.time_ns()-startT
print("[%.4f]ms matrix size %d"%(endT*(10**-6),n**2))
print(tabulate.tabulate([["Hub Score",*hubScore],["Authorization Score",*authScore]],headers=["Score",*["D"+str(i) for i in range(n)]],tablefmt="fancy_grid",floatfmt=(None,*[".10f"]*n)))


