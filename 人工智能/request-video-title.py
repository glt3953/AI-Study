import requests
from bs4 import BeautifulSoup

#url = 'https://v.qq.com/x/cover/mzc00200rw5zn5u.html'
url =  'https://v.qq.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

titles = []
for page in range(1, 11):
    param = {
        'list_id': 2168901,
        'tid': 168,
        'pver_id': 1,
        'bfid': 168,
        'p': page,
        'num': 20
    }
    response = requests.get(url, params=param, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    lis = soup.find_all('li', class_='cover_item cl')
    for li in lis:
        title = li.find('p', class_='figure_title').text
        titles.append(title)

print(titles)
