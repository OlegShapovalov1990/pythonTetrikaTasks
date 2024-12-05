import requests
from bs4 import BeautifulSoup
import csv


url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

category_links = soup.find_all('a', href=True)

animal_counts = {chr(i): 0 for i in range(ord('А'), ord('Я') + 1)}

for link in category_links:
    href = link['href']

    if href.startswith('/wiki/Категория:'):
        first_letter = href.split(':')[1][0]

        if first_letter in animal_counts:
            animal_counts[first_letter] += 1

with open('beasts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for letter, count in animal_counts.items():
        writer.writerow([letter, count])

print("Файл beasts.csv успешно создан.")
