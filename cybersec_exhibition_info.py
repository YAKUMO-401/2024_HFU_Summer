import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium_cybersec_SC import get_exd_detail

def get_cybersec_exd_info(is_export_to_csv=True):
    url = "https://cybersec.ithome.com.tw/2024/exhibitionDirectory"

    response = requests.get(url)
    response

    soup = BeautifulSoup(response.text, "html.parser")
    exd_cards = soup.find_all("div", attrs={"class": "exd-card"})

    url_prefix = "https://cybersec.ithome.com.tw"
    exd_cards_info = list()

    for exd_card in exd_cards:

        href = url_prefix + exd_card.a["href"]

        exd_name = exd_card.h5.text

        if exd_card.h6: 
          exd_id = exd_card.h6.text.split("：")[1]
        else:
          exd_id = ""


    
        exd_cards_info.append({
            'exd_link': href,
            'exd_name': exd_name,
            'exd_id': exd_id
        })


    if is_export_to_csv:
       data = pd.DataFrame(exd_cards_info) 
       data.to_csv('cybersec_exd.csv')

    return exd_cards_info

if __name__ == "__main__":
    data = get_cybersec_exd_info(is_export_to_csv=False)
    print(data[:5])