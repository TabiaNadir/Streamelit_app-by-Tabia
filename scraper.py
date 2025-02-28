import requests
from bs4 import BeautifulSoup

def get_tourist_places(city):
    search_url =f"https://en.wikipedia.org/wiki/{city.replace(' ', '_')}"
    response = requests.get(search_url)

    if response.status_code != 200:
        return["No data found. Please check the city name."]
    
    soup =BeautifulSoup(response.text, "html.parser")
    places = []
    for li in soup.select("div.mw-parser-output ul li"):
        text = li.get_text()
        if "Park" in text or "Museum" in text or "Monument" in text:
            places.append(text)
    return places[:5]        