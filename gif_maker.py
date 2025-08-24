import glob
import os
import mimetypes
from PIL import Image

def is_image(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith('image')

def make_gif_from_folder(frame_folder):
    # Gather all image files (jpg, jpeg, png, etc.) in the folder
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.gif']
    image_paths = []
    for ext in image_extensions:
        image_paths.extend(glob.glob(os.path.join(frame_folder, ext)))
    # Filter only valid image files
    image_paths = [f for f in image_paths if is_image(f)]

    if not image_paths:
        print("No images found in the specified folder.")
        return
    frames = []
    for image_path in sorted(image_paths):
        try:
            with Image.open(image_path) as img:
                frames.append(img.copy()) # Copy to avoid issues with closed files
        except Exception as e:
            print(f"Error opening {image_path}: {e}")

    if frames:
        # Save the frames as an animated GIF
        frames[0].save(
            "my_awesome.gif",
            format="GIF",
            append_images=frames[1:],
            save_all=True,
            duration=100,
            loop=0
        )
        print("GIF created successfully as 'my_awesome.gif'")
    else:
        print("No valid images could be opened.")

if __name__ == "__main__":
    # Replace with your actual folder path
    folder_path = r"C:\\Users\\name\\pictures"
    make_gif_from_folder(folder_path)

