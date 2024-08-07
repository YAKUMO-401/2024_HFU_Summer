from selenium import webdriver
from selenium.webdriver.common.by import By

def create_webdriver():
    return webdriver.Firefox()

def get_exd_detail(url,driver):
    data = dict()
    driver.get(url)

    telephone_element = driver.find_element(By.CLASS_NAME,"info-tel")
    if telephone_element:
       data['telephone'] = telephone_element.text

    mail_element = driver.find_element(By.CLASS_NAME,"info-mail")
    if mail_element:
       data['email'] = mail_element.text


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

    desc_element = driver.find_element(By.CLASS_NAME,"ex-foreword")
    if desc_element:
        print("Desc:",desc_element.text)
    else:
        print("Desc not found.")


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