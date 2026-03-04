import configparser
import os

def read_config_file(section, key):
    config = configparser.ConfigParser()
    working_dir = os.path.dirname(os.path.abspath(__file__))
    TARGET_PATH = os.path.join(working_dir, '../config.properties')
    config.read(TARGET_PATH)
    return config.get(section, key)