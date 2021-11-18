"""
Naive Bayes Classification
Author:[Lakshmi Sairam Kakarla]
Description:[Document classification using Naive Bayes].
"""
'''
Corpus Representation
[["word-0",....,"word-k","Class"],
["word-0",....,"word-m","Class"]..]
'''
import tabulate

training_corpse = [["president", "nod", "for", "lokpal", "bill", "India"],
                   ["india", "scraps", "vvip", "chopper", "deal", "with", "agustawestland", "India"],
                   ["maldives", "president", "coming", "today", "Others"],
                   ["mdmk", "to", "be", "part", "of", "bjp", "led", "nda", "India"],
                   ["ex", "envoy", "hardeep", "puri", "joins", "bjp", "India"],
                   ["modi", "to", "address", "rally", "in", "panaji", "India"],
                   ["church", "not", "against", "modi", "bishop", "India"],
                   ["aap", "government", "wins", "confidence", "vote", "India"],
                   ["seemandhra", "bandh", "hits", "ap", "tn", "India"],
                   ["ramdev", "offers", "conditional", "support", "to", "modi", "India"],
                   ["aap", "retains", "jhaadu", "as", "its", "symbol", "India"],
                   ["violence", "mars", "poll", "in", "bangladesh", "Bangladesh"],
                   ["modi", "accepts", "ramdev", "terms", "for", "support", "India"],
                   ["bhutan", "king", "arrives", "on", "5", "day", "visit", "Others"],
                   ["sheikh", "hasina", "set", "to", "form", "govt", "again", "Bangladesh"],
                   ["four", "killed", "in", "postpoll", "violence", "in", "bangladesh", "Bangladesh"], ]
testing_corpse = [["sheikh", "hasina", "keeps", "home", "foreign", "affairs", "defence", "portfolios"],
                  ["hasina", "ready", "to", "protect", "democracy"],
                  ["agusta", "gets", "stay", "on", "india", "encashing", "bank", "guarantee"],
                  ["modi", "nervous", "over", "aaps", "emergence", "congress"],
                  ["united", "ap", "supporters", "burn", "copies", "of", "draft", "tbill"],
                  ["seemandhra", "mps", "ignore", "aicc","team"],
                  ["sena", "slams", "devyanis", "father", "for", "terming", "media", "casteist"],
                  ["evangelist", "benny", "hinns", "bangalore", "visit", "cancelled"],
                  ["mallika", "sarabhai", "joins", "aap"],
                  ["devyani", "khobragade", "leaves", "for", "india", "mea"],
                  ["deeply", "regret", "that", "india", "expelled", "our", "diplomat", "us"],
                  ["milkha", "singhs", "wife", "daughter", "join", "aap"],
                  ["baba", "ramdev", "to", "begin", "vote", "for", "modi", "yatra"],
                  ["bjp", "launches", "drive", "for", "donations", "to", "modi", "for", "pm", "fund"]
                  ]

# Question 2
total_unique_words=[]
for i in testing_corpse:
    for j in i:
        if j not in total_unique_words:
            total_unique_words.append(j)
for i in training_corpse:
    for j in i[:-1]:
        if j not in total_unique_words:
            total_unique_words.append(j)
print(total_unique_words)
print(len(total_unique_words))

training_unique_words=[]
for i in training_corpse:
    for j in i[:-1]:
        if j not in training_unique_words:
            training_unique_words.append(j)
print("\n|V| [%d]\n"%(len(training_unique_words)))


#Question 3
training_unique_class=[]
for i in training_corpse:
    if i[-1] not in training_unique_class:
        training_unique_class.append(i[-1])
Pclass=dict()
Ccount=dict()
for i in training_unique_class:
    count=0
    countc=0
    for j in training_corpse:
        if j[-1]==i:
            count+=1
            countc+=len(j[:-1])
    Ccount[i]=countc
    Pclass[i]=count/len(training_corpse)
for i in Pclass.keys():
    print("P(%s):[%f]"%(i,Pclass[i]))

#Question 4
print("\nSum of P(c):[%d]\n"%sum(Pclass.values()))

#question 5
WCcount=dict()
classWords=dict()
for i in training_unique_class:
    classWords[i]=[]
    WCcount[i]=dict()
for i in training_unique_class:
    for j in training_corpse:
        if j[-1]==i:
            classWords[i].extend(j[:-1])
for i in training_unique_class:
    for j in classWords[i]:
        WCcount[i][j]=classWords[i].count(j)

# Classification on testing data.
result_doc=[]
result=[]
for i in testing_corpse:
    t_class=""
    tp=-1
    for j in training_unique_class:
        P_class=Pclass[j]
        temp_V=len(training_unique_words)
        for k in i:
            if k not in training_unique_words:
                temp_V+=1
        for k in i:
            if k in classWords[j]:
                P_class*=(WCcount[j][k]+1)/(Ccount[j]+temp_V)
            else:
                P_class*=(1)/(Ccount[j]+temp_V)
        if P_class>tp:
            t_class=j
            tp=P_class
    result_doc.append(" ".join(i))
    result.append(t_class)

print(tabulate.tabulate([[result_doc[i],result[i]] for i in range(len(result))],headers=["Document","Predicted Class"],tablefmt="fancy_grid"))



