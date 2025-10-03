import requests

class NewsAPI:
    """
    Class to fetch news headlines from NewsAPI
    """

    BASE_URL = "https://newsapi.org/v2/top-headlines"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_headlines(self, country="us", category=None, page_size=10):
        """
        Fetch top headlines.
        country: 2-letter country code (us, in, gb, etc.)
        category: business, entertainment, general, health, science, sports, technology
        page_size: number of articles
        """
        params = {
            "apiKey": self.api_key,
            "country": country,
            "pageSize": page_size
        }
        if category:
            params["category"] = category

        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            data = response.json()
            return data.get("articles", [])
        except Exception as e:
            print("Error:", e)
            return []
