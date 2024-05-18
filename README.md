# README

# Fine-Tune Data Generator

## Introduction
This project provides tools and scripts for generating JSONL files for fine-tuning GPT models. The goal is to create high-quality datasets that can be used to improve model performance on specific tasks.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/awaisakram64/finetune-data-generator.git
   cd finetune-data-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Preprocess raw data:
   ```bash
   python finetune/data_preprocessing.py --input data/raw --output data/processed
   ```

2. Generate JSONL files:
   ```bash
   python finetune/data_generation.py --input data/processed --output data/generated
   ```

## Contributing
Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

