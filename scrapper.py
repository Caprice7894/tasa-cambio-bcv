import requests
from bs4 import BeautifulSoup


def getDivisas():
    url = "https://www.bcv.org.ve"
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, "html.parser")
    res = soup.find_all('div', class_='centrado')
    return [_.text.strip().replace(',','.') for _ in res]

if __name__ == "__main__":
    print(getDivisas())
