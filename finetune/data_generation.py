import json
import os
import argparse

def generate_jsonl(input_dir, output_file):
    data = []
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(input_dir, filename), 'r') as file:
                content = file.read()
                entries = process_content(content)
                data.extend(entries)

    with open(output_file, 'w') as out_file:
        for entry in data:
            out_file.write(json.dumps(entry) + '
')

def process_content(content):
    entries = []
    lines = content.split('
')
    for line in lines:
        if line.strip():
            entry = {
                'section': 'example_section',
                'content': line.strip()
            }
            entries.append(entry)
    return entries

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate JSONL files for fine-tuning GPT models.')
    parser.add_argument('--input', type=str, required=True, help='Directory containing processed data')
    parser.add_argument('--output', type=str, required=True, help='Output JSONL file')

    args = parser.parse_args()

    generate_jsonl(args.input, args.output)

