import requests
from bs4 import BeautifulSoup as bs
import warnings
warnings.filterwarnings("ignore")

#TASK ECOMMERCE
main_url="https://www.oriana.com/jewellery/gold-jewellery.html"
main_html_text=requests.get(main_url,verify=False).text
main_soup=bs(main_html_text,"html.parser")
sub_urls=[]
for i in main_soup.find_all("li",attrs={"class":"item"}):
    try:
        temp_child=i.findChild()
        if "?cat=" in temp_child["href"]:
            sub_urls.append((temp_child["href"],temp_child.text))
    except KeyError:
        continue

for i in sub_urls:
    print("Category: ",i[1].split(" ")[0])
    sub_url=i[0]
    sub_html_text=requests.get(sub_url,verify=False).text
    sub_soup=bs(sub_html_text,"html.parser")
    for item in sub_soup.find_all("a",attrs={"class":"product photo product-item-photo","href":True}):
        item_html_text=requests.get(item["href"],verify=False).text
        item_soup=bs(item_html_text,"html.parser")
        parent_tag=item_soup.find("div",attrs={"class":"product-header-main"})
        print("     %s"%parent_tag.findChild().text)
    print("\n")


# TASK VIT
# url="https://chennai.vit.ac.in/"
# html_text=requests.get(url,verify=False).text
# soup=bs(html_text,"html.parser")
# for i in soup.find_all("h3",attrs={"class":"item-title"}):
#     print(i.text,"["+i.find_next_sibling().text+"]")
#     print("\n")