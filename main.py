from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = "E:/privatte/xscrapselenium/chromedriver/chromedriver.exe"
s = Service(chrome_driver)
options = ChromeOptions()
driver = webdriver.Chrome(service=s, options=options)
action = ActionChains(driver=driver)


fraze = input('Plis tinput what item you would like to search: ')


driver.get("https://www.x-kom.pl")
time.sleep(5)
action.key_down(Keys.TAB)
action.key_up(Keys.TAB)
action.key_down(Keys.TAB)
action.key_up(Keys.TAB)
action.key_down(Keys.TAB)
action.key_up(Keys.TAB)
action.key_down(Keys.ENTER)
action.key_up(Keys.ENTER)

search_fraze = driver.find_element(By.XPATH,
                                   """//*[@id="app"]/div[1]/header/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/input""")
# action.click(on_element=cookies)
action.click(on_element=search_fraze)
action.send_keys(fraze)
action.key_down(Keys.ENTER)
action.key_up(Keys.ENTER)
action.perform()

time.sleep(3)
by_price = driver.find_element(By.XPATH,
                                """//*[@id="react-select-id2--value"]/div[1]""")
action.click(on_element=by_price)
action.key_down(Keys.ARROW_DOWN)
action.key_up(Keys.ARROW_DOWN)
action.key_down(Keys.ARROW_DOWN)
action.key_up(Keys.ARROW_DOWN)
action.key_down(Keys.ENTER)
action.key_up(Keys.ENTER)
action.perform()

time.sleep(1)
names = driver.find_elements(By.XPATH,
                             """//*[@id="listing-container"]/div[1]/div/div[2]/div[2]/div[1]/a/h3/span""")
print(names[0].text)
