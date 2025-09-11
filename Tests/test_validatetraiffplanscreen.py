import datetime
import os.path
import time

from PIL import Image, ImageChops
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from SeleniumAutomation.Configurations.configure import configureparser
from SeleniumAutomation.Utilities.resuablecomponents import *



def test_validatetitleimage(browserInstance):
    #driver = webdriver.Chrome()
    driver = browserInstance
    driver.implicitly_wait(5)
    config = configureparser()
    # expectedimagepath = imagepath("SeleniumAutomation\\ExpectedArtifacts","tariff_title_expectedlimg.png"+(datetime.datetime.now()).strftime("%Y-%m-%d_%H-%M-%S"))
    # actualimagepath = imagepath("SeleniumAutomation\\ActualArtifacts","tariff_title_actualimg.png"+(datetime.datetime.now()).strftime("%Y-%m-%d_%H-%M-%S"))
    # actual_image_path = imagepath("SeleniumAutomation\\ActualArtifacts", "tariff_title_actualimg.png")
    # expected_image_path = imagepath("SeleniumAutomation\\ExpectedArtifacts", "tariff_title_expectedimg.png")
    actual_image_path = imagepath(config['ActualImageStoragePath']['TariffPageTitleActualPath'], config['TariffPageTitleActualImageName'])
    expected_image_path = imagepath(config['ExpectedImageStoragePath']['TariffPageTitleExpectedPath'], config['ExpectedImageName']['TariffPageTitleExpectedImageName'])


    driver.get("https://en.orange.es/")

    driver.find_element(By.ID, "onetrust-reject-all-handler").click()
    wait = WebDriverWait(driver, 5)
    wait.until(expected_conditions.invisibility_of_element((By.CLASS_NAME, "ot-sdk-row")))
    titleImageLocator = driver.find_element(By.XPATH, "//img[@src = '/ss/Satellite?blobcol=urldata&blobkey=id&blobnocache=false&blobtable=MungoBlobs&blobwhere=1521466274512&ssbinary=true']")
    titleImageLocator.screenshot(actual_image_path)
    titleImageLocator.screenshot(expected_image_path)
    diff = compareimages(actual_image_path, expected_image_path)

    if diff.getbbox():
        print("images are as expected")

    print("resolve this2 main")

    driver.quit()