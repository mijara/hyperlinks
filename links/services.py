import requests
from bs4 import BeautifulSoup


def link_metadata(url):
    response = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(response.text, features="html.parser")

    metas = soup.find_all('meta')

    metadata = {
        'title': soup.title.text.strip(),
        'keywords': None,
        'description': None,
        'theme-color': None,
    }

    for meta in metas:
        if 'name' not in meta.attrs or 'content' not in meta.attrs:
            continue

        if meta.attrs['name'] in metadata:
            metadata[meta.attrs['name']] = meta.attrs['content']

    return metadata


if __name__ == '__main__':
    print(link_metadata('http://www.facebook.com'))
