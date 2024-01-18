import base64
from io import BytesIO

from openai import OpenAI
from openai.types.chat import ChatCompletion
from pdf2image import convert_from_path


def pdf_to_base64(pdf_path):
    # Convert PDF to a list of images
    images = convert_from_path(pdf_path)

    base64_images = []

    for image in images:
        # Convert image to base64
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())

        # Add the base64-encoded image to the list
        base64_images.append(img_str.decode())

    return base64_images

def pdf_ingest_and_extract(pdf_path, prompt_path, openai_api_key):

    images = pdf_to_base64(pdf_path)
    with open(prompt_path, "r") as p:
        prompt = p.read()
    content = [{"type": "text", "text": prompt}]
    
    for i in images:
        content.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{i}"}})
    
    with OpenAI(api_key=openai_api_key) as client:
        response: ChatCompletion = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            max_tokens=4000,
            temperature=0
        )
        
    return response.choices[0].message.content