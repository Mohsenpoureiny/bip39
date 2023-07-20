from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
input('Install Extension...')
driver.get("moz-extension://73bd2b6e-4109-4f99-b8fa-81288a5be275/popup.html#/ImportMnemonicsTip")
input('Fine')