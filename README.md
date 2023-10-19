# olx-search

Search for the cheapest ads on https://www.olx.pt!

## Features:
* Fast intuitive CLI interface
* Sort by cheapest ads above a given price point to avoid clutter
* Broad search based on key terms
* String matching - only show ads that meet your criteria

## Installation
```bash
cd olx-search
pip install .
```

## Example usage:
```bash
$> olx-search --help
Usage: olx-search [OPTIONS] SEARCH

  Get OLX ads sorted by ascending price.

  Parameters ---------- search: str     Search string passed to OLX contains:
  str     Filter ads that contain the *contains* string, ignoring white spaces
  and capitalization. count: int     Number of ads to show price_from: int
  Lowest admissible price region: str     Region of Portugal where to search.
  Some options are {'lisboa', 'porto', 'leiria'}. Refer to the olx website for
  more.

Arguments:
  SEARCH  [required]

Options:
  --contains TEXT
  --count INTEGER       [default: 5]
  --price-from INTEGER  [default: 0]
  --region TEXT
  --help                Show this message and exit.
```

```bash
$> olx-search "RTX 3060 ti" --contains 3060ti --price-from 200 --count 2


Showing cheapest 2 ads based on search terms: ['rtx', '3060', 'ti']
Search URL was: "https://www.olx.pt/d/ads/q-rtx-3060-ti/?search%5Border%5D=filter_float_price:asc&search%5Bfilter_float_price:from%5D=200"
Showing only ads that contain "3060ti"

280.0€: RTX - 3060Ti EVGA 8GB GDDR6
"https://www.olx.pt/d/anuncio/rtx-3060ti-evga-8gb-gddr6-IDHwpzn.html"

320.0€: Placa Gráfica Zotac Gaming  RTX 3060 Ti 8GB GDDR6 Twin Edge OC LHR
"https://www.olx.pt/d/anuncio/placa-grfica-zotac-gaming-rtx-3060-ti-8gb-gddr6-twin-edge-oc-lhr-IDHmlTP.html"
```

## Requirements:
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
* [requests](https://pypi.org/project/requests/)
* [typer](https://typer.tiangolo.com/)


