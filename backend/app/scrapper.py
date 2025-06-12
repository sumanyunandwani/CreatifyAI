import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_image(url):
    """
    Downloads an image from a given URL and saves it to a local directory.
    The image is saved in a directory named 'images' located in the same directory as this script.
    If the directory does not exist, it will be created.

    Args:
        url (str): The URL of the image to download.

    Returns:
        str: The local path where the image is saved, or None if the download fails.
    """
    # Ensure the images directory exists
    save_dir = os.path.join(os.path.dirname(__file__), 'images')

    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            filename = os.path.basename(urlparse(url).path)
            if not filename:
                filename = "image.jpg"
            save_path = os.path.join(save_dir, filename)
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return save_path
    except Exception as e:
        print(f"Failed to download {url}: {e}")
    return None

def scrape_product(url):
    """
    Scrapes product information from a given URL.
    This function retrieves the product title and images from the webpage.

    Args:
        url (str): The URL of the product page to scrape.

    Returns:
        dict: A dictionary containing the product title, a list of image paths, and the URL.
    """
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, 'html.parser')

    # Title
    title = soup.title.string.strip() if soup.title else "Product"

    # Image extraction
    image_tags = soup.find_all('img')
    images = []

    for tag in image_tags:
        src = tag.get('src') or tag.get('data-src')
        if src:
            full_url = urljoin(url, src)
            if any(x in full_url.lower() for x in ['product', 'image', 'media']):
                images.append(full_url)

    # Deduplicate and limit to top 5
    unique_images = list(dict.fromkeys(images))[:5]


    images_path_list = [download_image(img) for img in unique_images if img]

    return {
        "title": title,
        "images": images_path_list,
        "url": url
    }