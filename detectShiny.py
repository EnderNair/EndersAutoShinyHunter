import cv2
import numpy as np

def detect_shiny(pokemon_names, screenshot):
    detected_pokemon = None
    max_val = 0
    threshold = 0.9  # Adjust this value based on the desired accuracy

    for pokemon_name in pokemon_names:
        template = cv2.imread(f"./Gen3ShinyEmerald/Shiny{pokemon_name}.png", cv2.IMREAD_UNCHANGED)
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val_current, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if max_val_current > threshold and max_val_current > max_val:
            max_val = max_val_current
            detected_pokemon = pokemon_name

    return detected_pokemon
