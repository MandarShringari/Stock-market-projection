import requests

def search_stocks(query, limit=5):
    url = "https://query2.finance.yahoo.com/v1/finance/search"
    params = {
        "q": query,
        "quotesCount": limit,
        "newsCount": 0,
        "listsCount": 0
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0"
    }

    response = requests.get(url, params=params, headers=headers)

    # If Yahoo blocks or fails, avoid crashing:
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return []

    try:
        data = response.json()
    except Exception:
        print("Yahoo returned non-JSON:", response.text)
        return []

    quotes = data.get("quotes", [])
    results = []

    for q in quotes:
        results.append({
            "symbol": q.get("symbol"),
            "name": q.get("shortname") or q.get("longname"),
            "exchange": q.get("exchDisp"),
            "type": q.get("quoteType")
        })

    return results[:limit]
print(search_stocks("app"))