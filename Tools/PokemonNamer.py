import os

# Load pokedex data into dictionary
pokedex = {}
with open('pokedex.txt') as f:
    for line in f:
        number, name = line.strip().split('\t')
        pokedex[number] = name

# Rename png files
directory = './Gen3ShinySpritesFireLeaf/'
for filename in os.listdir(directory):
    if filename.endswith('.png') and 'spr_rs-S_' in filename:
        number = filename[9:12]  # Extract pokedex number from filename
        if number in pokedex:
            name = 'Shiny' + pokedex[number] + '.png'
            os.rename(directory + filename, directory + name)
