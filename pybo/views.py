from django.http import HttpResponse, JsonResponse
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

    price_text = driver.find_element_by_id('TOTAL_PRICE').text
    paper_text = driver.find_element_by_id('paperSelectBoxItText').text
    paper_sub_text = driver.find_element_by_id('paper_sub_selectSelectBoxItText').text
    paper_dosu = driver.find_element_by_id('soduSelectBoxItText').text
    size_c_x = driver.find_element_by_name('CUT_WDT').get_attribute("value")
    size_c_y = driver.find_element_by_name('CUT_HGH').get_attribute("value")
    size_w_x = driver.find_element_by_name('WRK_WDT').get_attribute("value")
    size_w_y = driver.find_element_by_name('WRK_HGH').get_attribute("value")
    item_count = driver.find_element_by_name('number1').get_attribute("value")
    if item_count == "":
        item_count = driver.find_element_by_id('number1_selSelectBoxItText').text
        
    item_case = driver.find_element_by_name('number2').get_attribute("value")
    if item_case == "":
        item_case = driver.find_element_by_id('number2_selSelectBoxItText').text
    # print("금액은 {}입니다.".format(price_text))
    # print(driver.find_element_by_name('CUT_WDT'))
    driver.quit()
    data = {
        "price" : price_text,
        "paper_name" : paper_text,
        "paper_sub_name" : paper_sub_text,
        "paper_dosu" : paper_dosu,
        "size_cut_X" : size_c_x,
        "size_cut_Y" : size_c_y,
        "size_work_X" : size_w_x,
        "size_work_Y" : size_w_y,
        "item_count" : item_count,
        "item_case" : item_case
    }
    return JsonResponse(data)

# ---------------------------------------------------------------------------- #

