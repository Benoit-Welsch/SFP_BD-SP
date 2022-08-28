import yaml

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
