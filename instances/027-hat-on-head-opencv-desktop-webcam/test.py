from PIL import Image
import numpy as np
import cv2  # For displaying or saving the result
import os
import sys

# support for importing custom library -- START
current_folder = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_folder, "../.."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
# support for importing custom library -- END

# Load the background image (as a NumPy array)
background_path = os.path.join(current_folder, "bg.png")  # Replace with your file path
background = cv2.imread(background_path, cv2.IMREAD_COLOR)
background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)  # Convert to RGB

# Load the overlay image (with transparency)
overlay_path = os.path.join(current_folder, "hat.png")  # Replace with your file path
overlay = Image.open(overlay_path).convert("RGBA")

# Convert the background to a PIL Image
background_pil = Image.fromarray(background)

# Specify the position for the overlay (top-left corner)
position = (50, 50)  # Adjust as needed

# Overlay the PNG onto the background
background_pil.paste(overlay, position, mask=overlay)

# Convert back to a NumPy array
result = np.array(background_pil)

# Display the result using OpenCV
result_bgr = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
cv2.imshow("Result", result_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
