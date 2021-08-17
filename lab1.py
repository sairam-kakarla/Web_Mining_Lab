import requests


# Function which takes the text of the Response object's body(response.text) and find the external link in them.
def getLinks(text_response):
    start = 0
    urlscount = 0
    urlset = set()
    while (start != -1):
        start_link = text_response.find("<a href=", start)
        if (start_link != -1):
            start_quote = text_response.find('"', start_link)
            end_quote = text_response.find('"', start_quote + 1)
            start = end_quote
            if (start_quote < end_quote):
                ext_link = text_response[start_quote + 1:end_quote]
                if (ext_link != "#"):
                    print(ext_link)
                    urlscount += 1
                    urlset.add(text_response[start_quote + 1:end_quote])
        else:
            break
    print("Total ", urlscount, " links are present in the given url")
    print("Total ", len(urlset), " unique links are present in the given url")


url = "https://chennai.vit.ac.in/"
# verify is set to False so that the SSL certificate of https site is not verfied by the clint(us).
resp = requests.get(url, verify=False)
print("Status Code: ", resp.status_code)
print("URL of the Response Object: ", resp.url)
print("Response Enconding: ", resp.encoding)
print("Request Headers: ", resp.request.headers)
print("Response Headers: ", resp.headers)
print("Time elapsed: ", resp.elapsed.total_seconds() * 1000, " ms")
print("List of Links present in ", resp.url)
getLinks(resp.text)
