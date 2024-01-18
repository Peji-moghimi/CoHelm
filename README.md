# PDF to JSON Converter

## Overview
PDF to JSON Converter is a Python-based pipeline for extracting information from PDF documents and converting it into structured JSON format. This project leverages OpenAI's GPT models to interpret and structure data from PDF files, making it particularly useful for processing and analyzing document content programmatically.

## Features
- **PDF Text and Image Extraction**: Convert PDF documents into a combination of text and images.
- **Data Structuring**: Utilize AI models to parse and structure data into a unified JSON format.
- **Flexibility**: Easily adaptable for various types of PDF documents.

## Requirements
- Python 3.x
- OpenAI API key
- Additional Python libraries: `openai`, `pdf2image`, `os`, `json`, `pathlib`, `io`, `sys`

## Usage
- Place your PDF document in an accessible directory.
- Set up the prompt files for PDF extraction and JSON conversion as per your requirements.
- The resulting JSON file will be saved in the ../results/ directory.


# Docker Instructions

## Building the Docker Image
This command builds a Docker image named 'cohelm-app' from the Dockerfile in the current directory.
```docker build -t cohelm-app .```

## Running the Docker Container
This command runs the Docker container interactively.
It mounts the 'cohelm_output' directory to '/app/results' inside the container.
The container executes the 'main.py' script using Python, processing 'medical-record-<RECORD-NUMBER>.pdf'.
Replace 'YOUR_OPENAI_API_KEY_HERE' with your actual OpenAI API key, and the record number with the record number you'd like to process
```docker run -it --rm -v ./results:/app/results cohelm-app python ./scripts/main.py ./pdfs/medical-record-<RECORD_NUMBER_HERE>.pdf YOUR_OPENAI_API_KEY_HERE```

## Accessing the Output
After the Docker container has run, you can find the output files in the ./results directory.


## Configuration
- PDF Extraction Prompt: Edit pdf_extraction_prompt.txt to change how the AI interprets the PDF content.
- JSON Conversion Prompt: Modify `../prompts/text_to_json_schema_prompt.txt` to adjust the JSON structure.
## Project Structure
- pdf_to_text.py: Script for converting PDF files to text and images.
- text_to_unified_json.py: Script for converting text to a structured JSON format.
- main.py: Main executable script that integrates the entire pipeline.
- prompts/: Directory containing prompt files.
- results/: Directory where output JSON files are saved.