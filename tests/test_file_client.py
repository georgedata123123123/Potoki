from with_client import text_client,open_without
import json
import os



import logging.config
from logging import getLogger

with open("logging.conf") as file:
    config = json.load(file)

logging.config.dictConfig(config)
logger = getLogger()
logging.info("logging is working!")


def test_read_from_file():

    test_data = '123'
    with open('testfile_15415.txt', 'a') as f_o:
        f_o.write(test_data)
    assert text_client('testfile_15415.txt', 'r') == test_data


def test_without_with():

    test_data = 'a\nb\nc\n'
    with open('testfile_15415.txt', 'a') as f_o:
        f_o.writelines(test_data)
    assert open_without('testfile_15415.txt') == test_data