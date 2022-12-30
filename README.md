# olx-search

Search for the cheapest ads on https://www.olx.pt!

Features:
*Fast intuite CLI interface
*Sort by cheapest ads above a given price point to avoid clutter
*Broad search based on key terms
*Filter only ads that meet you exact criteria

Example usage:
```bash
$> python .\main.py --help

 Usage: main.py [OPTIONS] SEARCH

┌─ Arguments ──────────────────────────────────────────────────────────────────────────────────┐
│ *    search      TEXT  [default: None] [required]                                            │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
┌─ Options ────────────────────────────────────────────────────────────────────────────────────┐
│ --contains          TEXT     [default: None]                                                 │
│ --count             INTEGER  [default: 5]                                                    │
│ --price-from        INTEGER  [default: 0]                                                    │
│ --help                       Show this message and exit.                                     │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
```

```bash
$> python .\main.py "RTX 3060 ti" --contains 3060ti --price-from 200 --count 2


Showing cheapest 2 ads based on search terms: ['rtx', '3060', 'ti']
Search URL was: https://www.olx.pt/d/ads/q-rtx-3060-ti/?search%5Border%5D=filter_float_price:asc&search%5Bfilter_float_price:from%5D=200
Showing only ads that contain 3060ti

280.0 €: RTX - 3060Ti EVGA 8GB GDDR6
https://www.olx.pt/d/anuncio/rtx-3060ti-evga-8gb-gddr6-IDHwpzn.html

320.0 €: Placa Gráfica Zotac Gaming  RTX 3060 Ti 8GB GDDR6 Twin Edge OC LHR
https://www.olx.pt/d/anuncio/placa-grfica-zotac-gaming-rtx-3060-ti-8gb-gddr6-twin-edge-oc-lhr-IDHmlTP.html
```


