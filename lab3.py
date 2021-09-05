import re

import requests
from bs4 import BeautifulSoup as bs


# A recursive Function to List all the children in a Document, given an max depth for better control.
# Optionally variable spacing can be given.
def recursiveDOMList(tag, max_depth, spacing=0):
    if max_depth > 0:
        if spacing == 0:
            print("┌", tag.name)
        else:
            print("│    " * spacing + "├──", tag.name)
        for i in tag.findChildren(recursive=False):
            recursiveDOMList(i, max_depth - 1, spacing + 1)
    return


# Task 1
# url = "https://www.vit.ac.in"
# resp = requests.get(url, verify=False)
# soup = bs(resp.text, "html.parser")
# print("Title: "+soup.find("title").text)
# for i in soup.find_all("a",attrs={"class":"nav-link"}):
#     print(i.text)


# Task 2
# url = "https://vit.ac.in/school/allfaculty/site/computer-applications"
# resp = requests.get(url, verify=False)
# soup =  bs(resp.text, "html.parser")
## Task 2(a)
# for i in soup.find_all("h3",attrs={"class":"title2"}):
#     print(i.text,end="  ")
#     parent=i.parent;
#     list=[]
#     for j in parent.find_all("p",recursive=True):
#         list.append(j.text)
#     if len(list)>2:
#         print("["+list[2]+"]")
#     else:
#         print("{Not Available}")

## Task 2(b)
# social_media=["facebook","linkedin","twitter","instagram"]
# url = "https://vit.ac.in/school/allfaculty/site/computer-applications"
# resp = requests.get(url, verify=False)
# soup = bs(resp.text,"html.parser")
# for i in soup.find_all("a",attrs={"href":True}):
#     link=i.get("href")
#     for j in social_media:
#         if link.find(j)!=-1:
#             print(j,i.get("class"))

## Task 2(c)
# recursiveDOMList(soup.html,8)


## Task 3
url = "https://sermitsiaq.ag/english"
resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = bs(resp.text, "html.parser")
# Task 3(a)
# for i in soup.find_all(class_="menu"):
#     print("....................................................")
#     for j in i.find_all(class_="first leaf"):
#         print("[FirstLeaf] "+j.text)
#     for j in i.find_all(class_="leaf"):
#         print("[Leaf] "+j.text)
#     for j in i.find_all(class_="last leaf"):
#         print("[Last Leaf] "+j.text)

# Task 3(b)
# for i in soup.find_all(id=re.compile(r'menu')):
#     print("[Tag] "+i.name,"[Tag ID]",i["id"])

# Task 3(c)
# for i in soup.find_all("article"):
#     print(i)

# Task 3(d)
# recursiveDOMList(soup.html,7)


# Task 4
url = "https://www.batimes.com.ar"
resp = requests.get(url, verify=False)
soup = bs(resp.text, "html.parser")


# Task 4(a)
# for i in soup.find_all(class_="nav-item text-uppercase px-0"):
#     print(i)

# Task4(b)
def hasMK(tag):
    text_content = str(tag.find(text=True, recursive=False))
    if "Matías Lammens" in text_content:
        return True
    return False


for i in soup.find_all(hasMK):
    print(i)

# Task4(c)
# for i in soup.find_all("img",attrs={"src":True,"alt":True}):
#     print("...............................................")
#     print(i)
#     print("Image Source: ",i["src"])
#     print("Image Description: ",i["alt"])

# Task4(d)
# recursiveDOMList(soup.html,6)
