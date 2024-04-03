import requests
from bs4 import BeautifulSoup

url = 'https://arxiv.org/abs/2403.20328'  # Replace this URL with your desired paper URL

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Get the paper title
title = soup.find('h1', class_='title mathjax').text.replace('\n', '').strip()
# Get the author information
authors = soup.find('div', class_='authors').text.replace('\n', ' ').replace('Authors:', '').strip()
# Get the abstract
abstract = soup.find('blockquote', class_='abstract mathjax').text.replace('\n', ' ').replace('Abstract:  ', '').strip()

# Extract the project website URL
# Assuming the project website link might have a consistent identifiable part in its href value
project_website = soup.find('a', href=lambda href: href and "leg-manip" in href)
project_website_url = project_website['href'] if project_website else "Project website not found"

print(f'Title: {title}')
print(f'Authors: {authors}')
print(f'Abstract: {abstract}')
print(f'Project Website URL: {project_website_url}')
