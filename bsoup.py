from bs4 import BeautifulSoup


soup = BeautifulSoup("""<h1>Hello</h1><p>World</p>""", 'lxml')
print(soup.decode_contents())
