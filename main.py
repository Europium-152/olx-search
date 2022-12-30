from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
import typer


def number(text: str) -> float:
    text = text.replace("Negociável", "")
    text = text.replace("Sob orçamento", "")
    text = text.replace("€", "")
    text = text.replace(".", "")
    text = text.replace(",", ".")

    if text == '':
        return -1

    return float(text)


def get_ads(search: str, contains: str=None, count: int=5, price_from: int=0) -> None:

    search_terms = [key for key in map(lambda x: x.strip(), search.lower().split(" ")) if key != '']
    search_string = "q-" + "-".join(search_terms)

    search_URL = f"https://www.olx.pt/d/ads/{search_string}/?search%5Border%5D=filter_float_price:asc&search%5Bfilter_float_price:from%5D={int(price_from)}"

    http_request_response = requests.get(search_URL)
    html_text = http_request_response.text

    soup = BeautifulSoup(html_text, 'lxml')

    listings = soup.find_all('div', attrs={"data-cy": "l-card"})

    # Extract listing information into lists
    names = [BeautifulSoup(str(ad), 'lxml').find('h6').text for ad in listings]
    prices = [number(BeautifulSoup(str(ad), 'lxml').find('p', attrs={"data-testid": "ad-price"}).text) for ad in listings]
    link_prefix = "https://www.olx.pt"
    links = [link_prefix + BeautifulSoup(str(ad), 'lxml').find('a')['href'] for ad in listings]

    # Create data structure
    @dataclass
    class AD:
        name: str
        price: float
        link: str

    ads = [AD(name, price, link) for name, price, link in zip(names, prices, links)]

    # Remove ads that do not contain mandatory terms
    if contains is not None:
        name_contains = lambda name, contains: contains.replace(" ", "").lower() in name.replace(" ", "").lower()
        right_ads = list(filter(lambda ad: name_contains(ad.name, contains), ads))
    else:
        right_ads = ads

    # Remove ads with no price set
    right_ads = list(filter(lambda ad: ad.price != -1, right_ads))

    # Resort the ads because of "top" ads
    sorted_ads = sorted(right_ads, key=lambda ad: ad.price)

    if count < len(sorted_ads):
        answer = sorted_ads[:count]
    else:
        print(f"Could not find {count} ads that met the search criteria. Possible solutions:")
        print("* Reduce the number of displayed ads")
        print("* Increase the minimum search price to avoid wrong ads")
        print("* Use more restrictive name requirements")
        answer = sorted_ads

    print(f'\nShowing cheapest {len(answer)} ads based on search terms: {search_terms}')
    print(f'Search URL was: "{search_URL}"')
    if contains != '':
        print(f'Showing only ads that contain "{contains}"')

    print("")

    for ad in answer:
        print(f'{ad.price}€: {ad.name}\n"{ad.link}"\n')

if __name__ == '__main__':
    typer.run(get_ads)
