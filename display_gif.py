from PIL import Image
import matplotlib.pyplot as plt

# Open the GIF
gif_path = "my_awesome.gif"

try:
    img = Image.open(gif_path)
    # Check if image is a GIF
    if img.format == "GIF":
        # Display the GIF using matplotlib
        plt.imshow(img)
        plt.axis('off') # Hide axes
        plt.show()
    else:
        print(f"Error: File '{gif_path}' is not a GIF.")

except FileNotFoundError:
    print(f"Error: File '{gif_path}' is not a GIF.")
except Exception as e:
    print(f"An error occurred: {e}")