import json

from openai import OpenAI


def text_to_unified_json(text, prompt_path, openai_api_key, model="gpt-4-1106-preview"):

    with open(prompt_path, "r") as p:
        prompt = p.read()
        prompt = prompt + "\n\n" + f"medical document input: {text}\noutput:"
    
    with OpenAI(api_key=openai_api_key) as client:
        response = client.chat.completions.create(
                model=model,
                response_format={"type": "json_object"},
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0
            )
    
    output = response.choices[0].message.content
    output = output.split("<json>\n")[-1].split("\n</json>")[0]
    
    return json.loads(output)