# GifCreater
Required Packages

Pillow (PIL fork) - image processing and GIF creation
pip install pillow
Matplotlib - for displaying animations
pip install matplotlib

gif_maker.py
Purpose:
This script loads an existing GIF file (my_awesome.gif), extracts all its frames, and displays an animated version of the GIF using Matplotlib.

How it works:  
It opens the GIF file using PIL (Python Imaging Library).
Extracts all individual frames from the GIF (pil_img.n_frames gives the total number of frames).
Stores these frames in a list.
Uses Matplotlib to create a figure and animate the frames with ArtistAnimation.
Displays the animation in a window.

Key steps:  
Opens and reads the GIF.
Handles errors if the file isn't found or isn't a GIF.
Creates an animation object and displays it.

display_gif.py
Purpose:
This script generates a GIF (my_awesome.gif) from a folder containing image files (JPEG, PNG, BMP, GIF, etc.).

How it works:  
It scans a specified folder for image files with common image extensions.
Opens each image and appends it to a list of frames.
Saves these frames as an animated GIF using PIL's save() method.

Key steps:  
Uses glob to find image files.
Uses mimetypes to verify if files are images.
Opens images with PIL, copies them, and handles errors.
Creates an animated GIF with specified duration and loop settings.
