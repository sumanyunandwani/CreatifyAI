from moviepy.editor import ImageClip, concatenate_videoclips, CompositeVideoClip, TextClip
import os

def split_script(script, max_chars=80):
    """
Splits a script into sentences based on periods, ensuring each sentence is trimmed of whitespace.


    Args:
        script (str): The script to be split into sentences.
        max_chars (int, optional): Maximum characters per sentence. Defaults to 80.

    Returns:
        list: A list of sentences, each trimmed of whitespace.
    """
    return [s.strip() for s in script.split('.') if s.strip()]

def generate_video(data, script):
    """
    Generates a video from the provided data and script.

    Args:
        data (dict): A dictionary containing product data, including images and title.
        script (str): The script to be used in the video.

    Returns:
        str: The filename of the generated video.
    """

    video_width, video_height = 1280, 720
    duration_per_image = 3  # seconds
    clips = []
    text_list = split_script(script)
    font_path = os.path.join(os.path.dirname(__file__), "ARIAL.TTF")

    for index in range(5):
        clip = ImageClip(data["images"][index]).set_duration(duration_per_image).resize((video_width, video_height))
        text_clip = (
            TextClip(
                text_list[index],
                fontsize=44,
                font=font_path,
                color='white',
                size=(video_width - 100, None),
                method='caption'
                )
                .set_duration(duration_per_image)
                .set_position('center')
                .fadein(0.5)
                .fadeout(0.5))

        composite = CompositeVideoClip([clip, text_clip])
        clips.append(composite)

    final = concatenate_videoclips(clips, method="compose")
    file_name = f"{get_video_path(data['title'])}.mp4"
    output = os.path.join(os.path.dirname(__file__), f"videos/{file_name}")
    final.write_videofile(output, fps=24)

    return file_name

def get_video_path(path):
    """
    Generates a sanitized video path from the given path.
    This function removes all special characters from the path and replaces spaces with underscores.
    It ensures that the resulting path is suitable for file naming.
    
    Args:
        path (str): The original path or title to be sanitized.

    Returns:
        str: A sanitized version of the path suitable for file naming.
    """
    # remove all special characters from the path
    return ''.join(e for e in path if e.isalnum() or e in (' ', '.', '_', '-')).replace(' ', '_')
