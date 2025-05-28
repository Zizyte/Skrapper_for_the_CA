
import requests
import bs4


base_url = "https://xkcd.com/"
url = "https://xkcd.com/1"

while "#" not in url:

    # PART 1 - Request and Soupify -----
    # requests the Web page
    response = requests.get(url)
    # Parse the page to make it easy to use
    soup = bs4.BeautifulSoup(response.content, "html.parser")

    # PART 2 - Find the url of the image ---------
    image_element = soup.select("#comic img")[0]
    image_source = image_element["src"]
    image_source = "https:" + str(image_source)

    # Get the name of the file
    image_name = image_source.split("/")[-1]

    # PART 3 - Download the Comic
    response = requests.get(image_source)

    with open("Comics.py/" + image_name, "wb") as file:
        file.write(response.content)

    # PART 4 Find the next page
    next_anchor = soup.select(".comicNav a[rel=next]")[0]
    next_href = next_anchor["href"]
    url = base_url + str(next_href)
    print(url)
