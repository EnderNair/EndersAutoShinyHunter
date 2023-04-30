import cv2
import numpy as np
import os
import pyautogui
import time

image_path = "./Gen3ShinySprites"

def compare_images(screen_image, image_path):
    """
    Compare the screen image with the image at image_path and return the result.
    """
    print(f"Comparing {image_path}...")

    # Load the image at image_path
    image = cv2.imread(image_path, 0)

    # Resize the image to a smaller size
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

    # Convert the screen image to grayscale
    screen_image = cv2.cvtColor(screen_image, cv2.COLOR_BGR2GRAY)

    # Resize the screen image to a smaller size
    screen_image = cv2.resize(screen_image, (0, 0), fx=0.5, fy=0.5)

    # Perform the image comparison and return the result
    res = cv2.matchTemplate(screen_image, image, cv2.TM_CCOEFF_NORMED)
    return res[0][0]


def main():
    # Get a list of all the shiny sprites in the Gen3ShinySprites directory
    image_paths = []
    for file in os.listdir("./Gen3ShinySprites"):
        if file.endswith(".png"):
            image_path = os.path.join("./Gen3ShinySprites", file)
            image_paths.append(image_path)

    while True:
        # Capture the screen image
        screen_image = np.array(pyautogui.screenshot())

        # Loop through each shiny sprite image and compare it to the screen image
        for image_path in image_paths:
            res = compare_images(screen_image, image_path)
            if res > 0.8:
                print(f"Shiny found: {image_path}")
                # Add code here to do something when a shiny is found

        # Wait a short period of time before checking the screen again
        time.sleep(0.1)

if __name__ == "__main__":
    main()
