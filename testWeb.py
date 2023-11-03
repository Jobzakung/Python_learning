import requests

def find_text_on_web_page(urls, search_text):
    for url in urls:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract the HTML content
            html_content = response.text

            # Check if the search text is present in the HTML content
            if search_text in html_content:
                print("The text '{}' was found on the web page: {}".format(search_text, url))
            else:
                print("The text '{}' was not found on the web page: {}".format(search_text, url))
        else:
            print("Failed to retrieve the web page {}. Error code: {}".format(url, response.status_code))

# Example usage
urls = [
    "https://em.iq.com/player.html?id=19rr7rfpmo&sh_pltf=4&partnerCode=playbux",
    "https://em.iq.com/player.html?id=zuu0rf9wpl&sh_pltf=4&partnerCode=playbux"
]
search_text = "Playback error. Please try again later, or report the issue to us."

find_text_on_web_page(urls, search_text)
