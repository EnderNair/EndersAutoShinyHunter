# Author: Adrian Madsen 4/29/2023
# This code rips all Shiny Pokemon Sprites from Gen 3 to a folder

import os
import requests
import time

# Generate URLs for shiny sprites
urls = []
for i in range(1, 151):
    url = f"https://www.pokencyclopedia.info/sprites/gen3/spr_firered-leafgreen_shiny/spr_frlg-S_{i:03}.png"
    urls.append(url)

# Create folder for storing sprite images
directory = './Gen3ShinySpritesFireLeaf'
if not os.path.exists(directory):
    os.makedirs(directory)

# Download and save shiny sprite images for Generation 3 Pokemon
print("Downloading and saving shiny sprite images for Generation 3 Pokemon...")
for url in urls:
    filename = os.path.join(directory, url.split('/')[-1])
    print(f"Downloading {url}...")
    try:
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        time.sleep(0.1)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
print("Download and save complete.")
 
