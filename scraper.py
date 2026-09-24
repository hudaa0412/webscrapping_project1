import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin


URL = "https://www.amazon.in/"


def scrape_amazon():

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/153.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(
        URL,
        headers=headers,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    data = []

    h1_tags = soup.find_all("h1")

    for index, h1 in enumerate(h1_tags, start=1):

        title = h1.get_text(
            " ",
            strip=True
        )

        parent = h1.parent

        information = ""

        if parent:
            information = parent.get_text(
                " ",
                strip=True
            )

        link = ""

        anchor = h1.find("a")

        if anchor and anchor.get("href"):
            link = urljoin(
                URL,
                anchor["href"]
            )

        data.append({
            "id": index,
            "h1_header": title,
            "information": information,
            "url": link
        })

    df = pd.DataFrame(data)

    return df