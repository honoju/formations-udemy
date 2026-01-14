from pprint import pprint
import requests
from bs4 import BeautifulSoup
import re


def get_all_lyrics_urls() -> list[str]:
    LYRICS_WEBSITE_URL = "https://genius.com"
    next_page = '1'
    page = next_page
    lyrics_urls = []

    while next_page != None:
        r = requests.get(f"https://genius.com/api/artists/22451/songs?page={page}&sort=popularity")
        response = r.json().get("response")
        # pprint(response)
        songs = response.get("songs")
        if(len(songs) > 0):
            # pprint(songs)
            lyrics_paths = []
            for song in songs:
                lyrics_paths.append(song["path"])
            # pprint(lyrics_paths)
            lyrics_urls.extend([LYRICS_WEBSITE_URL+path for path in lyrics_paths])
            # pprint(lyrics_urls)
        next_page = response.get("next_page")
        try:
            page = next_page
        except:
            print("Page not found")

    pprint(lyrics_urls)
    print(len(lyrics_urls))

    return lyrics_urls

def get_words_from_all_lyrics():

    lyrics_urls = get_all_lyrics_urls()

    for url in lyrics_urls:
        html = requests.get(url).text

        soup = BeautifulSoup(html, "html.parser")

        lyrics_divs = soup.find_all(
            "div", attrs={"data-lyrics-container": "true"}
        )
        # pprint("\n\n ==== lyrics_divs \n\n")
        # pprint(lyrics_divs)

        for div in lyrics_divs:
            # Remove annotation links
            for tag in div.find_all("a", attrs={"href": "#about"}):
                # pprint("=== pre :\n {tag}")
                tag.decompose()
                # pprint("=== post :\n {tag}")

            for tag in div.find_all("div", attrs={"class": re.compile(r"^LyricsHeader")}):
                # pprint("=== pre1 :\n {tag}")
                tag.decompose()
                # pprint("=== post1 :\n {tag}")

            for tag in div.find_all("span", attrs={"class": re.compile(r"^Contributors")}):
                # pprint("=== pre2 :\n {tag}")
                tag.decompose()
                # pprint("=== post2 :\n {tag}")

        lyrics = "\n".join(
            div.get_text(separator="\n", strip=True)
            for div in lyrics_divs
        )

        lyrics = re.sub(r"\[.*?\](?:\s*\(x\s*\d+\))?\n?", "", lyrics).strip()

        print(lyrics)

# get_all_lyrics_urls()
get_words_from_all_lyrics()