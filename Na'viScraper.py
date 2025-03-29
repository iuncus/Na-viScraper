import requests
from bs4 import BeautifulSoup
import re

# main class that contains the scraper code
class Scraper:

    def extract(self, link, selection, type):
        # need to use different agent to circumvent block
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

        response = requests.get(link, headers = headers)

        if response.status_code != 200:
            print(response.status_code)
            return "Failed to retrieve page"

        
        soup = BeautifulSoup(response.text, "html.parser")
        sel_content = soup.select(selection)

        # choosing between extracting links and content based on argument
        if type == "link":
            sel_text = self.link_extractor(sel_content)
            return sel_text
        if type == "content":
            sel_text = self.content_extractor(sel_content)
            return sel_text

    # separate methods for extracting links and content
    def link_extractor(self, content):
        text = []
        if content:
            for i in content[0].find_all("span", class_ = "preview"):
                for link in i.find_all("a"):
                # remove session ID in url, doesn't seem to affect anything I just don't like them
                    temp = re.sub("\?PHPSESSID.*$", "", link.get("href"))
                    text.append(temp)
        return text

    def content_extractor(self, content):
        text = []
        if content:
            for i in content[0].find_all("div", class_ = "inner"):
                # some posts contain quotes as a child div which leads to duplicate data
                # remove them with .extract()
                for unwanted in i.find_all("blockquote"):
                    unwanted.extract()
                temp = i.get_text()
                text.append(temp)
        return text

forum_link = "https://forum.learnnavi.org/ninavi-niaw/"
# post_link = "https://forum.learnnavi.org/ninavi-niaw/tipangkxo-king/"

forum_select = "div#topic_container"
post_select = "div#forumposts"
scrape = Scraper()
links = []
link = ""
# links.append(post_link)
memory = "something"

index = 0
while link != memory:
    temp_link = forum_link + str(index)    
    # a memory to check for duplicates: break if detected as we've reached the end
    memory = link
    link = scrape.extract(temp_link, forum_select, "link")
    if link == memory:
        break
    links.extend(link)
    index += 35

# links.extend(scrape.extract(forum_link, forum_select, "link"))

with open("data/Na'viScraper/navi_link.txt", "w", encoding="utf-8") as myfile:
    for i in links:
        myfile.write(i)
        myfile.write("\n")
    myfile.flush()

print("the links are: ")
print(links)
print(len(links))

scraped_text = []


# WORKING CONTENT SCRAPER
# ----------------------------------------
# max_post = 5000
# for link in links:
#     post_content = ""
#     for i in range(0, max_post, 20):
#         temp_link = link + str(i)
#         memory = post_content
#         post_content = scrape.extract(temp_link, post_select, "content")
#         if post_content == memory:
#             break
#         print(post_content)
#         scraped_text.extend(post_content)


for link in links:
    post_content = ""
    i = 0
    while memory != post_content:
        temp_link = link + str(i)
        memory = post_content
        post_content = scrape.extract(temp_link, post_select, "content")
        if post_content == memory:
            break
        print(post_content)
        scraped_text.extend(post_content)
        i += 20

# print(scraped_text)
    # scraped_text.append(scrape.extract(i, con_select, "content"))
    # scraped_text.append("\n")
    # print(i)



# with open("data/Na'viScraper/navi_post.txt", "w", encoding="utf-8") as myfile:
with open("data/navi_post.tsv", "w", encoding="utf-8") as myfile:
    for i in scraped_text:
        myfile.write(i)
        myfile.flush()

