from requests import Session
from bs4 import BeautifulSoup
from time import sleep


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                         ' AppleWebKit/537.36 (HTML, like Gecko)'
                         ' Chrome/111.0.0.0 Safari/537.36'}

work = Session()

work.get('https://quotes.toscrape.com/', headers=headers)
response = work.get('https://quotes.toscrape.com/login', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

token = soup.find('form').find('input').get('value')
data = {'csrf_token': token, 'username': "login", 'password': "password"}
work.post('https://quotes.toscrape.com/login',
          headers=headers, data=data, allow_redirects=True)


result = soup.find_all('span', class_='text')
author = soup.find_all('small', class_='author')

"""условия для оствновки цикла
    if len(result) =! 0:
        ...
    else:
        break"""