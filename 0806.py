from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title

# https://selenium-python.readthedocs.io/locating-elements.html
elem = driver.find_element(By.NAME, "q") # 等同於BeautifulSoup的find -> 去找Python官網搜尋欄
# elem = driver.find_element(By.CLASS_NAME, "search-field")
# elem = driver.find_element(By.ID, "id-search-field")
time.sleep(5)

elem.clear()  # 清除搜尋欄
elem.send_keys("pycon") # 輸入 pycon 到搜尋欄
time.sleep(5)

elem.send_keys(Keys.RETURN) # 按下鍵盤的ENTER
time.sleep(20)


elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

