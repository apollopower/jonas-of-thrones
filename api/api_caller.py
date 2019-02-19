from bs4 import BeautifulSoup
import urllib
import json

ROOT = "https://awoiaf.westeros.org"
HDR = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def cap_name(char_name):
    result = []
    name_arr = char_name.split(' ')
    for name in name_arr:
        result.append(name.capitalize())
    return ' '.join(result)

def get_GOT_char(char_name):
    # FILTER char name so it is capitalzed properly
    char_name = cap_name(char_name)
    char_name_url = char_name.replace(" ", "%20")
    char_wiki = ROOT + "/index.php/" + char_name_url
    # Send request for page
    req = urllib.request.Request(char_wiki, headers=HDR)
    # Page is set, and parsed with Beautiful Soup
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    # Obtain char main image data from parsed wiki page
    img = soup.find('tr').find('img')
    # Get full url to image. Depending on source, we set the image_url a specific way
    if "thumb" in img['src']:
        img_url = ROOT + img['src']
    elif "/images" in img['src']:
        img_url = ROOT + img['src']
    elif "," in img['srcset']:
        img_url = ROOT + img['srcset'].split(',')[1]
    else:
        img_url = ROOT + img['srcset']
    # If not a thumbnail, remove size chars from end of url,
    # if "png" in img_url:
        # img_url = img_url.split('png')[0] + 'png'
    if "thumb" not in img_url:
        img_url = img_url.split('jpg')[0] + 'jpg'
    # Remove  1st whitespace
    img_url = img_url.replace(' ', '', 1)
    # Return final image url
    return img_url