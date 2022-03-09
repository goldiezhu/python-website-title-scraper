from bs4 import BeautifulSoup
import requests
import csv
from csv import writer

with open('links_2.csv') as f:
    reader = csv.reader(f)
    links = []
    titles = []
    title_tags = ["title"]

    for row in reader:
        links.append(row)

    for link in links:
        response = requests.get(link[0])
        soup = BeautifulSoup(response.text, 'html.parser')
        title = print(soup.find_all(title_tags))
        title_1 = soup.find_all(title_tags)
        
        titles.append(title_1)
        #print(titles)
    
    with open('links_3.csv', 'a') as s:
        writer = csv.writer(s)
        writer.writerow(titles) 
        print("x")

