import requests
import os
import ctypes
import sys
import glob

# Replace the text below with your unsplash developer access key
ACCESS_KEY = 'YOUR_UNSPLASH_ACCESS_KEY'

# Copy and Paste the folder path of your to the quotes below
TARGET_FOLDER = r'C:\Users\YourUsername\Pictures\ArchitectureWallpapers'

# Replace the text below with your wallpaper theme of choice. If you don't want a theme, just leave it blank (QUERY = '')
# Themes can be anything like Misty Waterfalls, Black and White F1, Fine Dining Plates, Colorful Rural Landscape, AI Generated, Modern Sci Fi....
QUERY = 'Architecture'

def download_image():
    url = f'https://api.unsplash.com/photos/random?query={QUERY}&client_id={access_key}'
    response = requests.get(url)

    if response.status_code == 200:
        # record relevant information from api call
        data = response.json()
        width, height = get_screen_resolution()
        image_url = data['urls']['raw'] + f"&w={width}&h={height}&fit=crop"
        image_id = data['id']
        
        # download image
        filename = f"{image_id}.jpg"
        filepath = os.path.join(TARGET_FOLDER, filename)

        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            with open(filepath, 'wb') as file:
                file.write(image_response.content)
            print(f"Downloaded {filename}")
            return filepath
        else:
            print(f"Failed to download image: {image_response.status_code}")
    else:
        print(f"Failed to get image data: {response.status_code}")
    
    return None

def set_wallpaper(filepath):
    # Set as desktop background using the Windows API
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, filepath, 0)

def clean_old_images(KEEP_LATEST = 5):
    # this function keeps only recent photos in the file, to keep it from getting too big
    
    # sort the wallpapers by age
    files = glob.glob(os.path.join(TARGET_FOLDER, "*.jpg"))
    files.sort(key = os.path.getmtime, reverse = True)
    
    # delete everything except the 5 newest
    for file in files[KEEP_LATEST:]:
        os.remove(file)

def get_screen_resolution():
    # adjust screen resolution of the image to fit your scree
    user32 = ctypes.windll.user32
    screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screen_size


if __name__ == '__main__':
    # if we are able to successfully run download_image(), then set wallpaper
    filepath = download_image()
    if filepath:
        set_wallpaper(filepath)
        clean_old_images()
    else:
        sys.exit(1)
