from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find(name="a", string="Kroger acknowledges that its bet on robotics went too far")
# print(article_tag.getText())

article_text = article_tag.getText()
article_link = article_tag.get("href")                    # find the <a> inside the span
article_upvote = soup.find(name="span", class_="score").getText()

print(article_text)
print(article_link)
print(article_upvote)




















# # import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.p)
#
# # all_anchor_tag = soup.find_all(name="a")
# # print(all_anchor_tag)
# #
# # for tag in all_anchor_tag:
# #     print(tag.getText())
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
# # heading_2 = soup.find(name="h3", class_="heading")
# # print(heading_2.name)
#
# # company_url = soup.select_one(selector="#name")
# # print(company_url)
#
# headings = soup.select(".heading")
# print(headings)






