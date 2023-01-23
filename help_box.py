from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def func1():
    driver_path = "C:\Program Files (x86)\chromedriver.exe"
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(driver_path, options=chr_options)
    chr_driver.maximize_window()
    chr_driver.get("file:///C:/STUFF!!!/Python%20Projects/Class/GUI/main/StocksFinal.html")
