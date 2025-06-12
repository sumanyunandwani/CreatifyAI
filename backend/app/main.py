"""
Main entry point for the FastAPI application.
This application scrapes product data, generates a script, and creates a video ad.

Returns:
    FastAPI app: The FastAPI application instance.
"""
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from scrapper import scrape_product
from generator import generate_script
from video import generate_video


app = FastAPI()

app.mount("/videos", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "videos")), name="videos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate_ad(url: str = Form(...)):
    """
    Generates a video ad based on the provided product URL.

    Args:
        url (str): The URL of the product page to scrape.

    Returns:
        dict: A dictionary containing the URL of the generated video.
    """
    data = {}
    while len(data.get("images", [])) != 5:
        data = scrape_product(url)
    script = generate_script(data)
    video_path = generate_video(data, script)
    return {
        "video_url": str(video_path)
    }

if __name__ == "__main__":
    """
    Main entry point for running the FastAPI application.
    This will start the server using Uvicorn.
    """
    import uvicorn
    uvicorn.run(app)