from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def create_webdriver():
    return webdriver.Firefox()

def get_exd_detail(url,driver):
    data = dict()
    driver.get(url)
    try:
        telephone_element = driver.find_element(By.CLASS_NAME,"info-tel")
        data['telephone'] = telephone_element.text
    except NoSuchElementException:
        print(f"URL: {url}, has no telephone")


    try:
        mail_element = driver.find_element(By.CLASS_NAME,"info-mail")
        data['email'] = mail_element.text
    except NoSuchElementException:
        print(f"URL: {url}, has no Email")

    try:
        desc_element = driver.find_element(By.CLASS_NAME,"ex-foreword")
        data['description'] = desc_element.text
    except NoSuchElementException:
        print(f"URL: {url}, has no description")


    web_elements = driver.find_elements(By.CLASS_NAME,"border-icon")
    if web_elements:    
        for web_element in web_elements:
            href = web_element.get_attribute('href')
            if href:
               for social_media_name in ['facebook', 'twitter', 'linkedin', 'instagram']:
                if social_media_name in href:
                    data[social_media_name] = href
            else:
                print("Web not found.")




    return data

if __name__ == '__main__':
    test_driver = create_webdriver()
    exd_url = "https://cybersec.ithome.com.tw/2024/exhibition-page/2043"
    exd_data = get_exd_detail(
        url=exd_url,
        driver=test_driver
    )
    print(exd_data)
    test_driver.close()