import json
import unittest
import os
from config import ConfigLoader
from file_processor import FileProcessor
from validator import Validator

class TestFileProcessor(unittest.TestCase):

    def setUp(self):
        config_data = {
            "error_arguments": "Usage: python {file_name} <config_file> <text_file>",
            "error_file_extension": "Error: the file '{file_name}' must have a .txt extension",
            "valid_file": "Valid files",
            "no_files_exist": "The files are not in the root folder",
            "file_empty": "The {file_name} file is empty."
        }
        with open("test_config.json", "w") as f:
            json.dump(config_data, f)

        self.config = ConfigLoader(config_path="test_config.json")
        self.validator = Validator(config_loader=self.config)
        self.processor = FileProcessor(config_loader=self.config, validator=self.validator)

        with open("test_config.txt", "w") as f:
            f.write("a=z\nb=y\nc=x\n")

        with open("test_text.txt", "w") as f:
            f.write("abcabcabc\n")

    def tearDown(self):
        os.remove("test_config.txt")
        os.remove("test_text.txt")
        os.remove("test_config.json")

    def test_load_config(self):
        replacements = self.processor.load_config("test_config.txt")
        self.assertEqual(replacements, {"a": "z", "b": "y", "c": "x"})

    def test_replace_in_text(self):
        replacements = self.processor.load_config("test_config.txt")
        lines_with_replacements = self.processor.replace_in_text("test_text.txt", replacements)
        self.assertEqual(lines_with_replacements[0][0], "zyxzyxzyx")

    def test_process_files(self):
        self.processor.process_files("test_config.txt", "test_text.txt")


if __name__ == "__main__":
    unittest.main()
