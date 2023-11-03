from bs4 import BeautifulSoup
import requests

urls = [
    "https://em.iq.com/player.html?id=19rr7rfpmo&sh_pltf=4&partnerCode=playbux",
    "https://em.iq.com/player.html?id=zuu0rf9wpl&sh_pltf=4&partnerCode=playbux"
]

text_to_find = "Playback error. Please try again later, or report the issue to us."  # Specify the text you want to find

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if text_to_find in soup.get_text():
        print(f"Text '{text_to_find}' found in the response from URL: {url}")
    else:
        print(f"Text '{text_to_find}' not found in the response from URL: {url}")
