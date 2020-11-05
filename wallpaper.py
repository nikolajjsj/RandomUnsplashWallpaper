import requests
import urllib.parse as urlparse
from urllib.parse import parse_qs

# url for random photo from Unsplash
url = "https://source.unsplash.com/random/2560x1600"


def main():
    print("Fetching Unsplash wallpaper")
    res = requests.get(url)
    file_type = parse_qs(urlparse.urlparse(res.url).query)['fm'][0]
    file_name = "wallpaper" + "." + file_type
    file = open(file_name, "wb")
    file.write(res.content)
    file.close()
    print("Fetched wallpaper")


if __name__ == "__main__":
    main()
