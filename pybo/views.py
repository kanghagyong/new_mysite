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
    
    item_list = ['TPBLMEO', 'TPBLPST', 'TPTKDFT', 'TPTKFOI', 'GSNTMIS']
    time.sleep(1)
    driver.get('https://www.redprinting.co.kr/ko/product/item/'+redid[0:2]+'/'+redid)
    if redid in item_list:
        price_text = driver.find_element_by_xpath("//div[@id='TOTAL_PRICE']").text
        if price_text == "":
            price_text = driver.find_element_by_name('TOTAL_PRICE').get_attribute("value")
        paper_text = ""
        paper_sub_text = ""
        paper_dosu = ""
        size_c_x = ""
        size_c_y = ""
        size_w_x = ""
        size_w_y = ""
        item_count = ""
        item_case = ""
    else:
        price_text = driver.find_element_by_xpath("//div[@id='TOTAL_PRICE']").text
        if price_text == "":
            price_text = driver.find_element_by_name('total_price').get_attribute("value")

        paper_text = driver.find_element_by_id('paperSelectBoxItText').text
        # paper_sub_text = driver.find_element_by_id('paper_sub_selectSelectBoxItText').text
        # paper_dosu = driver.find_element_by_id('soduSelectBoxItText').text
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

    driver.quit()
    data = {
        "price" : price_text,                    # 금액
        "paper_name" : paper_text,               # 용지명
        # "paper_sub_name" : paper_sub_text,       # 용지g수
        # "paper_dosu" : paper_dosu,               # 인쇄도수
        "size_cut_X" : size_c_x,                 # 재단사이즈x
        "size_cut_Y" : size_c_y,                 # 재단사이즈y
        "size_work_X" : size_w_x,                # 작업사이즈x
        "size_work_Y" : size_w_y,                # 작업사이즈y
        "item_count" : item_count,               # 수량
        "item_case" : item_case                  # 건수
    }
    return JsonResponse(data)

# ---------------------------------------------------------------------------- #

