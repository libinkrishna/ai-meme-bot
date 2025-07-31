import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_meme_caption(image):
    api_key = os.getenv("OPENAI_API_KEY")
    print("Loaded API Key:", api_key)  # TEMP DEBUG
    client = OpenAI(api_key=api_key)

    prompt = "Generate a short, funny meme caption for a random image."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a witty meme caption generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=50
        )
        caption = response.choices[0].message.content.strip()
        return caption
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
