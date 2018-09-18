from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from pymongo import MongoClient

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://s.taobao.com')

wait = WebDriverWait(browser,2)
mongo=MongoClient()
db=mongo['Taobao']
football=db['football']

def save_to_mongo(data):
    try:
        football.insert(data)
    except:
        print('存储失败')
def crawl():
    source = pq(browser.page_source)
    items = source.find('#mainsrp-itemlist .items .item').items()
    for item in items:
        body={}
        body['image']=item.find('.pic .img').attr('data-src')
        body['price']=item('.price').text()[2:]
        body['person_buy']=item('.deal-cnt').text()[:-3]
        body['name']=item.find('.J_ClickStat').text()
        body['store']=item('.shopname').text()
        body['location']=item('.location').text()
        yield body
def get_page(page):
    input = wait.until(EC.presence_of_element_located((By.ID,'q')))
    input.send_keys('足球')
    enter = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J_SearchForm"]/div/div[1]/button')))
    enter.click()
    for i in range(page):
        #这里'>'是用来选取子节点用的
        current_page = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span'),str(i+1)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
        print(i+1)
        for index,item in enumerate(crawl()):
            # save_to_mongo(item)
            print(index,item)
        next_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.form .input.J_Input')))
        next_page.clear()
        next_page.send_keys(i+2)
        confirm = browser.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]')
        confirm.click()

if __name__=='__main__':
    get_page(1)