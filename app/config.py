import os
import yaml

# Remove log from tensorflow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

config = None


def loadConfig():
    global config
    config = yaml.safe_load(open("./config.yml"))
    return config


def reload():
    loadConfig()


def getConfig():
    if (config == None):
        return loadConfig()
    return config
