from setuptools import setup, find_packages

setup(
    name='finetune-data-generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'jsonlines',
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'data_preprocessing=finetune.data_preprocessing:main',
            'data_generation=finetune.data_generation:main',
        ],
    },
)
