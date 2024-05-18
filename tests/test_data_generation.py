# Tests for data generation
import os
import json
import unittest
from finetune.data_generation import generate_jsonl

class TestDataGeneration(unittest.TestCase):

    def setUp(self):
        self.input_dir = 'tests/test_data/raw'
        self.output_file = 'tests/test_data/output.jsonl'
        os.makedirs(self.input_dir, exist_ok=True)
        with open(os.path.join(self.input_dir, 'test.txt'), 'w') as f:
            f.write('Example content Another line')

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        if os.path.exists(self.input_dir):
            for f in os.listdir(self.input_dir):
                os.remove(os.path.join(self.input_dir, f))
            os.rmdir(self.input_dir)

    def test_generate_jsonl(self):
        generate_jsonl(self.input_dir, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))
        with open(self.output_file, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 2)
            for line in lines:
                data = json.loads(line)
                self.assertIn('section', data)
                self.assertIn('content', data)

if __name__ == '__main__':
    unittest.main()

