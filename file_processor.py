import sys
from typing import Dict, List, Tuple
from config import ConfigLoader
from validator import Validator

class FileProcessor:
    """A class for processing files based on configuration and validation."""

    def __init__(self, config_loader: ConfigLoader, validator: Validator):
        """
        Initialize the file processor with a ConfigLoader and Validator.

        :param config_loader: An instance of ConfigLoader.
        :param validator: An instance of Validator.
        """
        self.config = config_loader
        self.validator = validator

    def load_config(self, config_file: str) -> Dict[str, str] | bool:
        """
        Load the configuration from a file into a dictionary.

        :param config_file: The path to the configuration file.
        :return: A dictionary with replacements or False if the file is empty.
        """
        replacements: Dict[str, str] = {}
        if self.validator.valid_file_empty(text_file=config_file):
            with open(config_file, 'r') as file:
                for line in file:
                    key, value = line.strip().split("=")
                    replacements[key] = value
            return replacements
        return False

    def replace_in_text(self, text_file: str, replacements: Dict[str, str]) -> List[Tuple[str, int]] | bool:
        """
        Replace text in a file based on the provided replacements dictionary.

        :param text_file: The path to the text file.
        :param replacements: A dictionary with replacements to apply.
        :return: A list of tuples with the modified line and the count of replacements, or False if the file is empty.
        """
        lines_with_replacements: List[Tuple[str, int]] = []
        if self.validator.valid_file_empty(text_file=text_file) and replacements:
            with open(text_file, "r") as file:
                for line in file:
                    original_line = line.strip()
                    modified_line = original_line
                    replacement_count = 0
                    for key, value in replacements.items():
                        modified_line, num_replacements = modified_line.replace(key, value), modified_line.count(key)
                        replacement_count += num_replacements
                    lines_with_replacements.append((modified_line, replacement_count))
            return lines_with_replacements
        return False

    def process_files(self, config_file: str, text_file: str) -> None:
        """
        Process the configuration and text files, applying replacements and printing the results.

        :param config_file: The path to the configuration file.
        :param text_file: The path to the text file.
        """
        if self.validator.validate_all(len(sys.argv), 3, config_file, text_file):
            replacements = self.load_config(config_file)
            lines_with_replacements = self.replace_in_text(text_file, replacements)
            if replacements and lines_with_replacements:
                sorted_lines = sorted(lines_with_replacements, key=lambda x: x[1], reverse=True)
                for line, _ in sorted_lines:
                    print(line)