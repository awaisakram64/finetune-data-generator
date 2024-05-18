import os
import argparse

def preprocess_data(input_dir, output_dir):
    """
    Preprocess raw data files by performing necessary cleaning steps and saving the processed data.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(input_dir, filename), 'r') as file:
                content = file.read()
                processed_content = clean_content(content)
                with open(os.path.join(output_dir, filename), 'w') as out_file:
                    out_file.write(processed_content)

def clean_content(content):
    """
    Clean the content by performing necessary text preprocessing steps.
    For example, removing extra whitespace, converting to lowercase, etc.
    """
    # Example cleaning steps (customize as needed)
    content = content.strip()  # Remove leading/trailing whitespace
    content = ' '.join(content.split())  # Remove extra spaces
    content = content.lower()  # Convert to lowercase
    return content

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocess raw data files.")
    parser.add_argument('--input', type=str, required=True, help="Directory containing raw data")
    parser.add_argument('--output', type=str, required=True, help="Directory to save processed data")

    args = parser.parse_args()

    preprocess_data(args.input, args.output)
