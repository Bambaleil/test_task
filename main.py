import os
import sys

from config import ConfigLoader
from file_processor import FileProcessor
from validator import Validator

if __name__ == '__main__':
    config = ConfigLoader()
    validator = Validator(config_loader=config)
    processor = FileProcessor(config_loader=config, validator=validator)

    if len(sys.argv) != 3:
        print(config.get("error_arguments").format(file_name=os.path.basename(__file__)))
    else:
        config_file = sys.argv[1]
        text_file = sys.argv[2]
        processor.process_files(config_file=config_file, text_file=text_file)
