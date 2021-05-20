from django.http import HttpResponse
import requests
import json            #json import하기
from urllib.request import urlopen
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def item_price_get(request):
    redid = request.GET['redid']
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)

    # # https://workey.codeit.kr/costagram 접속
    time.sleep(1)
    driver.get('https://www.redprinting.co.kr/ko/product/item/ST/'+redid)

    price_text = driver.find_element_by_name('TOTAL_PRICE').text
    # print("금액은 {}입니다.".format(price_text))
    driver.quit()
    data = {
        "price" : price_text
    }
    return HttpResponse("{}".format(data))

# ---------------------------------------------------------------------------- #

