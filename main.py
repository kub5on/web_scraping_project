from bs4 import BeautifulSoup
import pandas as pd
import os


def parse_local_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, 'lxml')
        return soup


path = "output/index.html"
soup = parse_local_html(path)

boxes = soup.select("div.year-card")

years = []
links = []

for box in boxes:
    years.append(box.find('h2').text)
    links.append(box.find('a')['href'])

df = pd.DataFrame({'years': years, 'links': links})
print(df)

df.to_csv('linki.csv', index=False)

lista = []
#
for link in links:
    link = f"output/{link}"
    soup = parse_local_html(link)
    year = soup.find('title').text
    nominowani = soup.select('.nominee')
    for nominee in nominowani:
        lista.append({
            "year": year,
            "link": link,
            "name": nominee.find('p').text
        })


df = pd.DataFrame(lista).drop_duplicates()
df.to_csv('nominowani.csv', index=False)
