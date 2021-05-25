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
    
    item_list = ['TPBLMEO', 'TPBLPST', 'TPTKDFT', 'TPTKFOI', 'GSNTMIS', 'APCAFGR', 'APDRFGR', 'APDDFGR', 'APECSHO', 'APCASHO', 'APCASHS', 'APCTLTT', 'APCTLTW', 'APHDBCD', 'APHDLFW', 'APHDLFT', 'APSDACL', 'APSDFML', 'APSDFMT', 'APMNPPC', 'APMNPPO', 'APPRTAG', 'APSTNMT', 'APDSGRD', 'APDSBXL', 'APDSSHF', 'APSSBOX', 'APSSSLD', 'APSSTRY', 'APASCIR', 'APDSTRY', 'APDSSTR', 'APDSSTN', 'APFRBNT', 'APSTSGN', 'APHDBCD', 'APHDPHN', 'APFCDSK', 'APFCSLD', 'APVSFLW', 'APBSDPY', 'APBSPTN', 'APTRGRP', 'APTTACR', 'APSTCOF', 'APTSCOF', 'APAMCOF']
    
    time.sleep(1)
    url_default = 'https://www.redprinting.co.kr/ko/product/item/'+redid[0:2]+'/'+redid

    if redid == "TPBCDFT":
        url = url_default+'/detail/26243'
    elif redid == "TPBCCPN":
        url = url_default+'/detail/179004'
    elif redid == "TPWBDFT":
        url = url_default+'/detail/36982'
    elif redid == "TPPOCHR":
        url = url_default+'/detail/234897'
    elif redid == "FBDCMOS":
        url = url_default+'/detail/194064'
    elif redid == "FBDCGLS":
        url = url_default+'/detail/195780'
    elif redid == "GSWTANT":
        url = url_default+'/detail/995770'
    elif redid == "BTMGPNS":
        url = url_default+'/detail/505239'
    elif redid == "TPTKBND":
        url = url_default+'/detail/669995'
    elif redid == "TPWTDFT":
        url = url_default+'/detail/32374'
    elif redid == "GSTRTAG":
        url = url_default+'/detail/30947'
    elif redid == "GSFGMIN":
        url = url_default+'/detail/246348'
    elif redid == "TPLFSET":
        url = url_default+'/detail/256623'
    elif redid == "PRBNDGN":
        url = url_default+'/detail/234518'
    elif redid == "PHSTPAN":
        url = url_default+'/detail/173824'
    elif redid == "PHSTNOP":
        url = url_default+'/detail/228437'
    elif redid == "PHSTSQP":
        url = url_default+'/detail/167769'
    elif redid == "TPCASET":
        url = url_default+'/detail/253311'
    elif redid == "TPDCPST":
        url = url_default+'/detail/40374'
    elif redid == "GSNTBND":
        url = url_default+'/detail/938675'
    elif redid == "GSNTLTR":
        url = url_default+'/detail/942060'
    elif redid == "GSPNCLP":
        url = url_default+'/detail/1192362'
    elif redid == "GSPNFLT":
        url = url_default+'/detail/1276112'
    elif redid == "TPPOAWD":
        url = url_default+'/detail/29439'
    elif redid == "TPRNBND":
        url = url_default+'/detail/286280'
    elif redid == "GSCLMGN":
        url = url_default+'/detail/223345'
    elif redid == "GSMEMGN":
        url = url_default+'/detail/341125'
    elif redid == "GSSMSTP":
        url = url_default+'/detail/935948'
    elif redid == "GSSMTMP":
        url = url_default+'/detail/951107'
    elif redid == "GSSMRUB":
        url = url_default+'/detail/F1'
    elif redid == "GSSMWOD":
        url = url_default+'/detail/994421'
    elif redid == "GSSMWDR":
        url = url_default+'/detail/1155399'
    elif redid == "GSTTCRK":
        url = url_default+'/detail/256120'
    elif redid == "GSTTREZ":
        url = url_default+'/detail/283796'
    elif redid == "FBTWSWT":
        url = url_default+'/detail'
    elif redid == "FBPCLKB":
        url = url_default+'/detail/676886'
    elif redid == "AIECMNP":
        url = url_default+'/detail'
    elif redid == "FBPODFT":
        url = url_default+'/detail/406004'
    elif redid == "FBCLTSH":
        url = url_default+'/detail/525985'
    elif redid == "FBCLBSS":
        url = url_default+'/detail'
    elif redid == "FBDCTWL":
        url = url_default+'/detail/193980'
    elif redid == "GSCAPAS":
        url = url_default+'/detail/236824'
    elif redid == "GSFBSTK":
        url = url_default+'/detail/244371'
    elif redid == "GSLPSTK":
        url = url_default+'/detail/308317'
    elif redid == "GSLPPRT":
        url = url_default+'/detail/362191'
    elif redid == "GSLPCVR":
        url = url_default+'/detail/314600'
    elif redid == "GSWLMIN":
        url = url_default+'/detail/276827'
    elif redid == "GSWLCAD":
        url = url_default+'/detail/317114'
    elif redid == "GSWLNEC":
        url = url_default+'/detail/317525'
    elif redid == "GSCAPHN":
        url = url_default+'/detail/1116838'
    elif redid == "TPHPFLM":
        url = url_default+'/detail/357621'
    elif redid == "GSCAPOD":
        url = url_default+'/detail/360425'
    elif redid == "GSCABUZ":
        url = url_default+'/detail/983356'
    elif redid == "GSMODFT":
        url = url_default+'/detail/127811'
    elif redid == "GSCKDFT":
        url = url_default+'/detail/655754'
    elif redid == "ACTPKEY":
        url = url_default+'/detail/294141'
    elif redid == "GSSTKEY":
        url = url_default+'/detail/310362'
    elif redid == "GSCATIN":
        url = url_default+'/detail/312698'
    elif redid == "GSSBMTL":
        url = url_default+'/detail/46'
    elif redid == "GSCBSTK":
        url = url_default+'/detail/719969'
    elif redid == "GSCAMSK":
        url = url_default+'/detail/1106659'
    elif redid == "PHFRACR":
        url = url_default+'/detail/271588'
    elif redid == "ACNTHAP":
        url = url_default+'/detail/374855'
    elif redid == "BNSTDGN":
        url = url_default+'/detail/234319'
    elif redid == "AICNDGN":
        url = url_default+'/detail/984727'
    elif redid == "PHPRDFT":
        url = url_default+'/detail/223791'
    elif redid == "PHPKDFT":
        url = url_default+'/detail/308784'
    elif redid == "TPPHSET":
        url = url_default+'/detail/296202'
    elif redid == "PHBKBKS":
        url = url_default+'/detail/242508?sel_gbn=8x6'
    elif redid == "PHBKSMP":
        url = url_default+'/detail/242484?sel_gbn=8x6'
    elif redid == "PHBKPRM":
        url = url_default+'/detail/242496?sel_gbn=8x6'
    elif redid == "PHPLEDT":
        url = url_default+'/detail/697364'
    elif redid == "GSPZPHO":
        url = url_default+'/detail/197964'
    elif redid == "PHBKSTA":
        url = url_default+'/detail/262083'
    elif redid == "TPCLWLB":
        url = url_default+'/detail/760777'
    elif redid == "TPCLSTD":
        url = url_default+'/detail/600877'
    elif redid == "TPCLHOL":
        url = url_default+'/detail/600926'
    elif redid == "TPCLWAL":
        url = url_default+'/detail/600921'
    elif redid == "PHFRCWC":
        url = url_default+'/detail/27065'
    elif redid == "PHFRHAN":
        url = url_default+'/detail/27095'
    elif redid == "PHFRASH":
        url = url_default+'/detail/27274'
    elif redid == "PHFRSVL":
        url = url_default+'/detail/27331'
    elif redid == "PHFRFIR":
        url = url_default+'/detail/26732'
    elif redid == "PHFRMUL":
        url = url_default+'/detail/27118'
    elif redid == "PHFRALU":
        url = url_default+'/detail/343666'
    elif redid == "PHFRWOD":
        url = url_default+'/detail/355121'
    elif redid == "PHFRPAP":
        url = url_default+'/detail/272793'
    elif redid == "GSCRCUB":
        url = url_default+'/detail/359901'
    elif redid == "GSGLPAN":
        url = url_default+'/detail/181895'
    else:
        url = url_default
    driver.get(url)
    if redid in item_list:
        price_text = driver.find_element_by_xpath("//div[@id='TOTAL_PRICE']").text
        if price_text == "":
            price_text = driver.find_element_by_name('total_price').get_attribute("value")
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

