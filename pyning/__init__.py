from os import path

import yaml

from pyning.tail_recursion.exponent import *
from pyning.tail_recursion.exponent_test import *

log_file_path = path.join(path.dirname(path.abspath(__file__)), "logging.yaml")

with open(log_file_path, "r") as file:
    config = yaml.safe_load(file.read())
    logging.config.dictConfig(config)
