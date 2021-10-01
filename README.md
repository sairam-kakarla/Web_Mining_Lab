# Web Mining Lab 
Repository to store assignments done for Web Mining Course(CSE3024) 
- - - -
__Libraries Required__
- bs4(Beautiful)   
  ``` pip install bs4 ```  
  or  
  ``` python3 -m pip install bs4```  
- tabulate  
 ``` pip install tabulate```  
 or  
 ``` python3 -m pip install tabulate```
- - - -
## Lab1 ✔️
Explore Basics of request module, understand HTTP and HTTPS Request and Response Objects.  
[Implementation](/lab1.py)
## Lab2 ✔️
- Explore [VIT Chennai Website](https://chennai.vit.ac.in/), display the list of faulty and their corresponding title.
- Explore [GRT Jewel](https://www.grtjewels.com/), display ornament information, classified according thier category.

[Implementation](/lab2.py)  
## Lab3 ✔️
1. Explore [VIT Website](https://www.vit.ac.in)
   1. Print Title
   1. Print all anchor tags with class "nav-link"
1. Explore [VIT Faculty Website](https://vit.ac.in/school/allfaculty/site/computer-applications)
   1. Display all faculty names and there research algorithms
   1. Find the social media handles present in the page.
   1. List out the DOM hierarchy.  
   Used this [DFS Search Implementation](https://github.com/sairam-kakarla/Web_Mining_Lab/blob/0da597414ba04b219d74a16c3bc59a1ad406721f/lab3.py#L8-L16) for listing DOM elements in this entire course.
1. Explore [SERMITSIAQ](https://sermitsiaq.ag/english).
   1. Find all items with class "menu" and print its children by their class.
   1. Find all items with "menu" in its id.
   1. Find all items with tag "article".
   1. List DOM hierarchy of the page.
1. Explore [BATIMES](https://www.batimes.com.ar)
   1. List items of class “ nav-item text-uppercase
px-0”
   1. Find the element with its text content containing “Matías Lammens”.
   1. List all images in the page.
   1. List DOM hierarchy of the page.  
  
  
[Implementation](/lab3.py)  

## Lab4 ✔
Implement a Baic webcrawler to crawl [VIT Website](https://vit.ac.in)  
Implement URL Frontier and perform BFS  
Implement URL filter to fiter out files like(images,doc,pdf)  
[Implementation](/lab4.py)

## Lab5 ✅
Implement algorithm to create inverse document posting list to index the documents.  
Part of Search Engine Construction.  
[Implementation](/lab5.py)

## Lab6 ✅
Implemented HITS Algorithm for hud and authority ranking, developed by Jon Kleinberg.
Given an adjacency matrix,number of iterations generate the authority score and hub score for each node.
There could be self loops and multiple links among the same pair of nodes(like weighted).  
[Implementation](/lab6.py)  
[References](https://en.wikipedia.org/wiki/HITS_algorithm#Algorithm)

## Lab7 ✅
Implemented the Page Rank algorithm. Given an adjacency matrix, number of iterations, damping factor
generated the outlink Vector, pagerank Vector for each node.
There could be self loops and multiple links among the same pair of nodes.  
[Implementation](/lab7.py)  
[References](https://en.wikipedia.org/wiki/PageRank#Damping_factor)
   

