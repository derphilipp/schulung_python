import configparser

config = configparser.ConfigParser()

config["DEFAULT"]["LOGLEVEL"] = "ERROR"
with open("config.ini", "w") as configfile:
    config.write(configfile)
