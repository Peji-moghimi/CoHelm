import json

from openai import OpenAI


def text_to_json(text, prompt_path, openai_api_key):

    with open(prompt_path, "r") as p:
        prompt = p.read()
        prompt = prompt + "\n\n" + f"Input: {text}\nOutput:"
    
    with OpenAI(api_key=openai_api_key) as client:
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        
    output = response.choices[0].message.content
    output = output.split("<json>\n")[-1].split("\n</json>")[0]
    
    return json.loads(output)

guidelines = {
    "guidelines": {
        "Colorectal cancer screening": {
            "criteria": {
                "Patient has average-risk or higher": {
                    "criteria": {
                        "Age 45 years or older?": {
                            "condition met" : None, 
                            "evidence" : None
                        },
                        "No colonoscopy in past 10 years?": {
                            "condition met" : None, 
                            "evidence" : None
                        },
                    }
                },
                "High risk family history": {
                    "criteria": {
                        "Colorectal cancer diagnosed in one or more first-degree relatives of any age": {
                            "criteria": {
                                "Age 40 years or older": {
                                    "condition met?" : None, 
                                    "evidence" : None},
                                "Symptomatic (eg, abdominal pain, iron deficiency anemia, rectal bleeding)": {
                                    "condition met?" : None, 
                                    "evidence" : None}
                            }
                        },
                        "Family member with colonic adenomatous polyposis of unknown etiology": {
                            "condition met?" : None, 
                            "evidence" : None}
                    }
                },
                "Juvenile polyposis syndrome diagnosis": {
                    "criteria": {
                        "Age 12 years or older and symptomatic (Abdominal pain, Iron deficiency anemia, Rectal bleeding, Telangiectasia)": {
                            "condition met?": None, 
                            "evidence": None
                        },
                        "Age younger than 12 years and symptomatic (Abdominal pain, Iron deficiency anemia, Rectal bleeding, Telangiectasia)": {
                            "condition met?": None, 
                            "evidence": None
                        }
                    }
                }
            }
        }
    }
}

decision = {"decision" : {"approve?" : None, "rationale" : None, "additional information required?" : None}}

def create_json_schema(jsons, prompt_path, openai_api_key):

    with open(prompt_path, "r") as p:
        prompt = p.read()
        prompt = prompt + "\n\n" + f"Input: {jsons}\nOutput:"
    
    with OpenAI(api_key=openai_api_key) as client:
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
    
    output = response.choices[0].message.content
    output = output.split("<json>\n")[-1].split("\n</json>")[0]
    
    return json.loads(output)