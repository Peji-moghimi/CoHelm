import json
import os
import sys

from pdf_to_text import pdf_ingest_and_extract
from text_to_unified_json import text_to_unified_json


def main(pdf_path, openai_api_key):
    # Predefined prompt paths
    prompt_path_pdf_to_text = './prompts/pdf_extraction_prompt.txt'
    prompt_path_text_to_json = './prompts/text_to_json_schema_prompt.txt'
    results_dir = './results/'

    # Create the results directory if it doesn't exist
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # Extract text and images from PDF
    extraction_response = pdf_ingest_and_extract(pdf_path, prompt_path_pdf_to_text, openai_api_key)
    extracted_text = extraction_response

    # Convert the extracted text to unified JSON format
    json_output = text_to_unified_json(extracted_text, prompt_path_text_to_json, openai_api_key)

    # Save the JSON output to a file in the results directory
    result_file_path = os.path.join(results_dir, os.path.basename(pdf_path).split(".")[0] + '_result.json')
    with open(result_file_path, 'w') as outfile:
        json.dump(json_output, outfile, indent=4)

    print(f"Result saved to {result_file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <pdf_path> <openai_api_key>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    openai_api_key = sys.argv[2]

    main(pdf_path, openai_api_key)