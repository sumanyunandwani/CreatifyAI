"""
Generates a script for a video ad based on product data.
"""
import openai
import os

os.environ["OPENAI_API_KEY"] = ""  # Replace with your actual OpenAI API key

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_script(data):
    """
    Generates a concise video ad script based on product data.
    This function uses OpenAI's GPT model to create a script that highlights the unique features and benefits of a product.

    Args:
        data (dict): A dictionary containing product data, including 'url' and 'title'.

    Returns:
        str: A concise video ad script suitable for a 15-second video.
    """
    messages=[
        {
            "role": "system", 
            "content": "You are a creative scriptwriter for video ads. "
            "Your task is to create engaging and concise scripts based "
            "on product data."
        }, 
        {
        "role": "user",
        "content": f"Generate Short Proffesional Video Ad Script: {data['url']} whose summary: {data['title']}. Engaging, concise, suitable for 15-second. Focus on product's unique features & benefits. Exactly 5 senteces with atmost 7 words each."
    }]
    
    # Uncomment the following lines to make an API call to OpenAI
    # response = client.chat.completions.create(
    #     model="gpt-4.1",
    #     messages=messages
    # )
    # return response['choices'][0]['message']['content']

    # For testing purposes, we will read from a local file instead of making an API call
    with open("C:/Users/suman/OneDrive/Documents/Github/CreatifyAI/backend/app/response.txt", encoding='utf-8') as f:
        sample_response = f.read()
    return sample_response
