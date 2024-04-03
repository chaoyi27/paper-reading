import requests
from bs4 import BeautifulSoup

# arXiv论文的URL
url = 'https://arxiv.org/abs/2403.20328'  # 示例URL，请替换为您感兴趣的论文的URL

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 获取论文标题
title = soup.find('h1', class_='title mathjax').text.replace('\n', '').strip()
# 获取作者信息
authors = soup.find('div', class_='authors').text.replace('\n', ' ').replace('Authors:', '').strip()
# 获取摘要
abstract = soup.find('blockquote', class_='abstract mathjax').text.replace('\n', ' ').replace('Abstract:  ', '').strip()

print(f'Title: {title}')
print(f'Authors: {authors}')
print(f'Abstract: {abstract}')
