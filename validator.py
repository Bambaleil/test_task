import os
from config import ConfigLoader

class Validator:
    """A class for validating input data."""

    def __init__(self, config_loader: ConfigLoader):
        """
        Initialize the validator with a ConfigLoader instance.

        :param config_loader: An instance of ConfigLoader.
        """
        self.config = config_loader

    def validate_args_length(self, args_length: int, expected_length: int) -> bool:
        """
        Validate the number of arguments passed to the script.

        :param args_length: The number of arguments provided.
        :param expected_length: The expected number of arguments.
        :return: True if the number of arguments is correct, False otherwise.
        """
        if args_length != expected_length:
            print(self.config.get("error_arguments").format(file_name=os.path.basename(__file__)))
            return False
        return True

    def validate_file_existence(self, config_file: str, text_file: str) -> bool:
        """
        Validate that the specified files exist.

        :param config_file: The path to the configuration file.
        :param text_file: The path to the text file.
        :return: True if both files exist, False otherwise.
        """
        if not (os.path.isfile(config_file) and os.path.isfile(text_file)):
            print(self.config.get("no_files_exist"))
            return False
        return True

    def validate_file_extensions(self, config_file: str, text_file: str) -> bool:
        """
        Validate that the specified files have the correct extensions.

        :param config_file: The path to the configuration file.
        :param text_file: The path to the text file.
        :return: True if both files have .txt extensions, False otherwise.
        """
        if not config_file.endswith(".txt"):
            print(self.config.get("error_file_extension").format(file_name=config_file))
            return False
        if not text_file.endswith(".txt"):
            print(self.config.get("error_file_extension").format(file_name=text_file))
            return False
        return True

    def valid_file_empty(self, text_file: str) -> bool:
        """
        Check if the specified file is empty.

        :param text_file: The path to the text file.
        :return: True if the file is not empty, False otherwise.
        """
        if os.stat(text_file).st_size == 0:
            print(self.config.get("file_empty").format(file_name=text_file))
            return False
        return True

    def validate_all(self, args_length: int, expected_length: int, config_file: str, text_file: str) -> bool:
        """
        Run all validations and return the result.

        :param args_length: The number of arguments provided.
        :param expected_length: The expected number of arguments.
        :param config_file: The path to the configuration file.
        :param text_file: The path to the text file.
        :return: True if all validations pass, False otherwise.
        """
        return (self.validate_args_length(args_length, expected_length) and
                self.validate_file_existence(config_file, text_file) and
                self.validate_file_extensions(config_file, text_file))