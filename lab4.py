import requests
from bs4 import BeautifulSoup as bs
import time
import re
from tabulate import tabulate
import warnings
###################################################
# Additional modules and libs needed
# 1 tabulate (for printing table can be replace with simple prints statements as well).
# pip install tabulate
# bs4 for parsing the documents and extracting the links
# pip install bs4
###################################################

warnings.filterwarnings("ignore")

# Basic Web Crawler with urlFrontier and Url Filter and Url look up.
# Ranking can be extended38.
# Document similarity as well.

# Filtering function
def vitURLFilter(url):
    # Document relative urls are ignored.
    local_url_match = re.match("^(https|http)://", url)
    # Add document filter
    doc_type_filter = re.search("(\.doc|\.pdf|\.png|\.jpg|\.jpeg|\.rar)$", url)
    if local_url_match is not None and doc_type_filter is None:
        return True
    return False


# URL Frontier FIFO Queue(element is a URL).
url = "https://www.vit.ac.in"
# FIFO queue to store the urls for BFS
# Initalized with the root url
urlFrontier = [url]

# to filter out already visited site, can use hashing for efficiency.
isSeenBucket = []

# Used to limit the execution time of the program. The urls visted decreases with the execution time.
maxExecutionTime = 200
startT = time.time()
total_url_count = 1
while len(urlFrontier) > 0 and time.time() - startT < maxExecutionTime:
    root_url = urlFrontier.pop(0)
    if root_url not in isSeenBucket:
        isSeenBucket.append(root_url)
        print(root_url)
        try:
            resp = requests.get(root_url, verify=False)
            if resp.status_code == 404:
                continue
            soup = bs(resp.text, "html.parser")
            resp.close()
            for i in soup.find_all("a", attrs={"href": True}):
                if vitURLFilter(i["href"]):
                    urlFrontier.append(i["href"])
                    total_url_count += 1
        # Need to investigate various error's
        except requests.exceptions.RequestException:
            print("[WARNING] " + root_url)
endTime = time.time() - startT
headers = ["Visited", "Collected", "Unvisited", "Time(seconds)"]
data = [[len(isSeenBucket), total_url_count, len(urlFrontier), endTime]]
print(tabulate(data, headers, tablefmt="fancy_grid"))
