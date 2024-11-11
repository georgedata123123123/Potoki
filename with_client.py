#

import json
import os


import logging.config
from logging import getLogger

with open("logging.conf") as file:
    config = json.load(file)

logging.config.dictConfig(config)
logger = getLogger()
logging.info("logging is working!")


def open_without(filename):


    file = open(filename, 'r', encoding='utf-8')
    a = file.read()
    file.close()
    return a
    logging.info('Success!')


def text_client(file_name: str, opening_type: str):


    with open(file_name, opening_type, encoding='utf-8') as file:
        return file.read()



with os.scandir(".") as entries:
    for entry in entries:
        print(entry.name, "->", entry.stat().st_size, "bytes")
    logging.info("Success read with os")





