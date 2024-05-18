import os
import unittest
from finetune.data_preprocessing import preprocess_data, clean_content

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        self.input_dir = 'tests/test_data/raw'
        self.output_dir = 'tests/test_data/processed'
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
        with open(os.path.join(self.input_dir, 'test.txt'), 'w') as f:
            f.write(' Example   content \nAnother line   ')

    def tearDown(self):
        for f in os.listdir(self.input_dir):
            os.remove(os.path.join(self.input_dir, f))
        os.rmdir(self.input_dir)
        for f in os.listdir(self.output_dir):
            os.remove(os.path.join(self.output_dir, f))
        os.rmdir(self.output_dir)

    def test_clean_content(self):
        content = ' Example   content \nAnother line   '
        expected = 'example content another line'
        self.assertEqual(clean_content(content), expected)

    def test_preprocess_data(self):
        preprocess_data(self.input_dir, self.output_dir)
        processed_file = os.path.join(self.output_dir, 'test.txt')
        self.assertTrue(os.path.exists(processed_file))
        with open(processed_file, 'r') as f:
            processed_content = f.read()
            self.assertEqual(processed_content, 'example content another line')

if __name__ == '__main__':
    unittest.main()
