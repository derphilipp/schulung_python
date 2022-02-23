import configparser
import logging

config = configparser.ConfigParser()

config.read("config.ini")
level_from_file = config["DEFAULT"]["LOGLEVEL"]
logging.basicConfig(level=level_from_file)

logging.error("ERROR EINTRAG")
logging.warning("WARNING EINTRAG")
logging.info("INFO EINTRAG")
logging.debug("DEBUG EINTRAG")
