import configparser

def configureparser():
    configp = configparser.ConfigParser()
    configp.read("..\..\TestData\properties.ini")
    return configp