from lxml import html
import requests

page = requests.get('https://www.allrecipes.com/')
tree = html.fromstring(page.content)

print(tree)
