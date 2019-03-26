import requests
from bs4 import BeautifulSoup
# import bs4

def main():
    req = requests.get('https://medium.com/darshanbruno')
    html = BeautifulSoup(req.text, "lxml")
    anchors = html.find_all("a")
    csv = open('links.csv', 'w+')
    for a in anchors:
        csv.write("".join([a.get_text(), ": ", a.get("href"), "\n"]))
    csv.close()

if __name__ == '__main__':
    main()